# Premier League Data Scraper and Analyzer

## Introduction
This project comprises Python scripts designed to extract and analyze data from the Premier League Official website. The extracted data spans multiple seasons, from 2011-12 to 2020-21, and serves as input for predictive modeling and statistical analysis in the realm of football.

## Motivation
The primary motivation behind this project is to leverage machine learning techniques to predict match outcomes and generate insights into team performance based on historical Premier League data. By scraping detailed match statistics, we aim to uncover patterns and trends that can inform strategic decisions and enhance the understanding of football dynamics.

## Features

### Premier League Scraper (PL_Scraper.py)
- Utilizes Selenium and pandas libraries to scrape match data from the Premier League Official website.
- Extracts information such as match date, teams, scores, possession, shots on target, and other relevant statistics.
- Stores scraped data in CSV files organized by season for further analysis.
### Main Script (Main.py)
- Orchestrates the scraping process by defining match IDs for specific seasons.
- Invokes the PL_Scraper class to scrape data for each match ID within the specified seasons.

## Usage
1. Clone the repository to your local machine.
2. Ensure you have Python installed along with the required libraries listed in requirements.txt.
3. Run Main.py to initiate the scraping process. Adjust the years dictionary within the script to specify the desired seasons.
4. Extracted data will be stored in CSV files within the Final_Results directory, ready for analysis.

## Example
```python
from Package.Scraper import Scraper

# Define match IDs for specific seasons
years = {"pl20_21": range(58897, 58899), "pl19_20": range(46605, 46607)}

# Scraping process
for id_range in years.values():
    for match_id in id_range:
        Scraper.scrape_match(match_id)
```
## Data
- Contains CSV files corresponding to each Premier League season.
- Each file provides detailed match descriptions, including date, teams, scores, possession, shots on target, and other statistics.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
