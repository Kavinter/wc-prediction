World Cup Predictor

This project is a data-driven Python application that predicts outcomes of FIFA World Cup matches and simulates tournament progression. Using historical match data, group stage results, and statistical modeling, it estimates match outcomes and advances teams through knockout rounds — all the way to the final.
Features

    Web Scraping: Collects historical FIFA World Cup match results (from 1930–2022) using both BeautifulSoup and Selenium.

    Data Cleaning & Preprocessing: Cleans raw score data, handles missing entries, and structures it into usable datasets.

    Group Stage Simulation: Calculates group standings by simulating fixtures and assigning points based on Poisson-distributed outcomes.

    Knockout Stage Prediction: Simulates each knockout round (Round of 16 to Final) based on previous winners.

    Statistical Modeling: Uses team-level scoring/conceding averages to predict match results using the Poisson distribution.

    Fixture Integration: Integrates real 2022 FIFA World Cup fixture data for simulations.

Technologies Used

    Python: Core language for logic, scraping, and processing.

    Pandas: For data manipulation and analysis.

    BeautifulSoup: For static HTML scraping from Wikipedia.

    Selenium: For scraping dynamic content when needed.

    SciPy (Poisson Distribution): For probabilistic match outcome modeling.

    Pickle: To serialize and save group table data.

How to Use

Clone the repository:

git clone https://github.com/yourusername/world-cup-predictor.git

Run the scripts in the following order for full simulation:

    table_creation.py – Creates group tables from 2022 World Cup.

    bs_scraping.py – Scrapes match results from 1930 to 2018 using BeautifulSoup.

    selenium_missing_data_scraping.py – Scrapes missing 1990 data with Selenium.

    data_scraping.py – Cleans, merges, and processes the full dataset.

    wc_prediction.py – Runs predictions for group and knockout stages and prints the final results.

Make sure to install the required packages:

pip install pandas beautifulsoup4 lxml selenium scipy

For Selenium to work, ensure you have Geckodriver installed and updated in your system path.
File Structure

.
├── table_creation.py                  # Creates and saves World Cup group tables (pickle)
├── bs_scraping.py                     # Scrapes World Cup match data using BeautifulSoup
├── selenium_missing_data_scraping.py # Uses Selenium to scrape missing World Cup match data
├── data_scraping.py                   # Cleans and merges raw World Cup data files
├── wc_prediction.py                   # Predicts match outcomes and tournament progression
├── dict_table.pkl                     # Serialized group data table
├── fifa_worldcup_data.csv             # Raw match data CSV
├── fifa_missing_data.csv              # Missing matches scraped with Selenium
├── cleaned_df_worldcup_data.csv       # Cleaned and processed data CSV
├── fifa_worldcup_fixture.csv          # Match fixtures CSV
└── README.md                          # This documentation file
