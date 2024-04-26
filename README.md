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
1. Clone the repository to your local machine:
```python
git clone https://github.com/MilanSajiv/Premier-League.git
```

2. Run the main script to initiate the data scraping process and generate match statistics:
```python
python Main.py
```
3. Follow the prompts to specify the seasons for which you want to scrape match data.
5. Once the scraping process is complete, the script will store the extracted data in CSV files within the Final_Results directory.
6. Use the generated CSV files to conduct further analysis, develop machine learning models, or visualize the data using your preferred tools or libraries.

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
