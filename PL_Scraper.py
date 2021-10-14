from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import re
import requests

options = Options()
options.headless = True

class Scraper:
    '''
    
    
    '''
    def __init__(self, match_id: int, driver_path: str):
        self.match_id = match_id
        self.driver_path = driver_path

        self.driver = webdriver.Chrome(options=options, executable_path=(driver_path))

    def __url__(self):
        url = f'https://www.premierleague.com/match/{self.match_id}'
        self.driver.get(url)

        try:
            date = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]').text
            date = datetime.strptime(date, '%a %d %b %Y').strftime('%m/%d/%Y')

            h_team = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
            a_team = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text

            scores = self.driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
            h_goals = scores.split('-')[0]
            a_goals = scores.split('-')[1]

            df = pd.read_html(self.driver.page_source) 
            stats = df[-1] 
        except:
            self.driver.quit()

        season_list = []
        
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
