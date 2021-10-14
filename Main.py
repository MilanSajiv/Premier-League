from Package.Scraper import Scraper

years = {"pl20_21": range(58897, 58899), "pl19_20": range(46605, 46607)}

# for season_id in years.values():
#    Scraper.__url__(season_id)

for id_range in years.values():
   for match_id in id_range:
      Scraper.__url__(match_id)