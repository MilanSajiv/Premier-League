from Package.Scraper import Scraper

years = {"pl20_21": range(58897, 58899), "pl19_20": range(46605, 46607)}

for season_id in years.values():
   Scraper.PL_Scraper(season_id)