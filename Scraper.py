from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import re
import requests

class Scraper: 
    '''
     Scraper
        ###
    '''
    def _get_url(self, id):
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(options=option)
        self.ROOT = f'https://www.premierleague.com/match/{id}'
        driver.get(self._init(self.ROOT))

    # def _Options(self):
    #     option = Options()
    #     option.headless = True
    #     driver = webdriver.Chrome(options=option)

    # def _date(self):
    #     option = Options()
    #     option.headless = True
    #     driver = webdriver.Chrome(options=option)
    #     date = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]').text
    #     date = datetime.strptime(date, '%a %d %b %Y').strftime('%m/%d/%Y')

    # def _teams(self):
    #     option = Options()
    #     option.headless = True
    #     driver = webdriver.Chrome(options=option)
    #     h_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
    #     a_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text
    #     return h_team, a_team

    # def _scores(self):
    #     option = Options()
    #     option.headless = True
    #     driver = webdriver.Chrome(options=option)
    #     scores = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
    #     h_goals = scores.split('-')[0]
    #     a_goals = scores.split('-')[1]
    #     return h_goals, a_goals

    def PL_Scraper(seasons):
        season_list = []
        for season_id in seasons.values():
            Scraper._get_url(season_id)
            option = Options()
            option.headless = True
            driver = webdriver.Chrome(options=option)

            try:
                date = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]').text
                date = datetime.strptime(date, '%a %d %b %Y').strftime('%m/%d/%Y')

                h_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
                a_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text

                scores = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
                h_goals = scores.split('-')[0]
                a_goals = scores.split('-')[1]

                button = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[2]/section[3]/div[1]/ul/ul/li[2]')
                button.click()
                sleep(1)

                df = pd.read_html(driver.page_source) 
                stats = df[-1] 

                driver.quit()
                
            except:
                driver.quit()
                continue
            h_stats = {}
            a_stats = {}

            home = stats[h_team]
            away = stats[a_team]
            stats = stats['Unnamed: 1']

            for row in zip(home, stats, away):
                h_stats[stat] = row[0]
                stat = row[1].replace(' ', '_').lower()
                a_stats[stat] = row[2]

            all_stats = ['Possession_%', 'Shots_on_target', 'Shots_Attempted', 'Touches', 'Passes_Completed',
                        'Tackles', 'Clearances', 'Corners', 'Offsides', 'Yellow',
                        'Red', 'Fouls']

            for stat in all_stats:
                if stat not in h_stats.keys():
                    h_stats[stat] = 0
                    a_stats[stat] = 0

            match = [date, h_team, a_team, h_goals, a_goals, h_stats['Possession_%'], a_stats['Possession_%'], h_stats['Shots_on_target'], a_stats['Shots_on_target'], h_stats['Shots_Attempted'], 
                    a_stats['Shots_Attempted'], h_stats['Touches'], a_stats['Touches'], h_stats['Passes_Completed'], a_stats['Passes_Completed'], h_stats['Tackles'], a_stats['Tackles'], h_stats['Clearances'], a_stats['Clearances'],
                    h_stats['Corners'], a_stats['Corners'], h_stats['Offsides'], a_stats['Offsides'], h_stats['Yellow'], a_stats['Yellow'], h_stats['Red'], a_stats['Red'], h_stats['Fouls'], a_stats['Fouls']]

            season_list.append(match)
            
            columns = ['Date', 'Home_Team', 'Away_Team', 'Home_Goals', 'Away_Goals']

            for stat in all_stats:
                columns.append(f'home_{stat}')
                columns.append(f'away_{stat}')

            dataset = pd.DataFrame(season_list, columns=columns)
            dataset.to_csv(f'{id}.csv', index=False)
        return('.csv file exported.')