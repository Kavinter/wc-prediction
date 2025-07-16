World Cup Predictor
Project Overview

This project is a Python-based application designed to predict the outcomes of FIFA World Cup matches. Using historical data, team statistics, and probabilistic models, it simulates match results and forecasts winners for each stage of the tournament, including group stages, knockouts, and finals.
Features

    Data Collection:

        Scrapes historical World Cup match results and fixtures from Wikipedia.

        Handles missing data with Selenium web scraping to fill gaps.

    Data Cleaning and Preparation:

        Merges multiple datasets, removes duplicates, and processes match scores.

        Calculates team strengths based on historical goals scored and conceded.

    Prediction Model:

        Implements a Poisson distribution-based algorithm to estimate match outcome probabilities.

        Predicts points for home and away teams in group matches.

        Simulates knockout rounds by iteratively determining winners and updating fixtures.

    Output:

        Generates CSV files for raw data, cleaned data, and match predictions.

        Prints final predicted winners of knockout rounds and the tournament.

Technologies Used

    Python 3

    Libraries:

        pandas (data handling)

        requests & BeautifulSoup (web scraping)

        selenium (dynamic web scraping for missing data)

        scipy.stats (Poisson distribution for predictions)

        pickle (data serialization)

How to Use

    Clone the repository:

git clone https://github.com/Kavinter/world-cup-predictor.git

Install required packages:

pip install pandas requests beautifulsoup4 selenium scipy

Run the scripts in order:

    Data scraping:
    Scrape historical data and save it locally.

    Data cleaning:
    Clean and preprocess the scraped data.

    Prediction:
    Run the prediction model to simulate the World Cup results.

Check generated CSV files:

    Raw data files (fifa_worldcup_data.csv, fifa_missing_data.csv)

    Cleaned dataset (cleaned_df_worldcup_data.csv)

    Match fixtures and predictions (fifa_worldcup_fixture.csv)

    Final predictions printed in console


File Structure

.
├── table_creation.py                # Creates and saves World Cup group tables (pickle)
├── bs_scraping.py                  # Scrapes World Cup match data using BeautifulSoup
├── selenium_missing_data_scraping.py  # Uses Selenium to scrape missing World Cup match data
├── data_scraping.py                # Cleans and merges raw World Cup data files
├── wc_prediction.py                # Predicts match outcomes and tournament progression
├── dict_table.pkl                  # Serialized group data table
├── fifa_worldcup_data.csv          # Raw match data CSV
├── fifa_missing_data.csv           # Missing matches scraped with Selenium
├── cleaned_df_worldcup_data.csv   # Cleaned and processed data CSV
├── fifa_worldcup_fixture.csv       # Match fixtures CSV
└── README.md                      # This documentation file    
