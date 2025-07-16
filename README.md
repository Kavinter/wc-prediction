# World Cup Predictor

This project is a data-driven Python application that predicts outcomes of FIFA World Cup matches and simulates tournament progression. Using historical match data, group stage results, and statistical modeling, it estimates match outcomes and advances teams through knockout rounds — all the way to the final.

## Features

- **Web Scraping**: Collects historical FIFA World Cup match results (from 1930–2022) using both BeautifulSoup and Selenium.
- **Data Cleaning & Preprocessing**: Cleans raw score data, handles missing entries, and structures it into usable datasets.
- **Group Stage Simulation**: Calculates group standings by simulating fixtures and assigning points based on Poisson-distributed outcomes.
- **Knockout Stage Prediction**: Simulates each knockout round (Round of 16 to Final) based on previous winners.
- **Statistical Modeling**: Uses team-level scoring/conceding averages to predict match results using the Poisson distribution.
- **Fixture Integration**: Integrates real 2022 FIFA World Cup fixture data for simulations.

## Technologies Used

- **Python** – Core language for logic, scraping, and processing.
- **Pandas** – For data manipulation and analysis.
- **BeautifulSoup (bs4)** – For static HTML scraping from Wikipedia.
- **Selenium** – For scraping dynamic content (e.g., 1990 data).
- **SciPy (Poisson Distribution)** – For probabilistic match outcome modeling.
- **Pickle** – To serialize and save group table data.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/world-cup-predictor.git
    cd world-cup-predictor
    ```

2. Install required packages:

    ```bash
    pip install pandas beautifulsoup4 lxml selenium scipy
    ```

3. Make sure [Geckodriver](https://github.com/mozilla/geckodriver/releases) is installed and properly referenced in your system path.

4. Run the scripts in the following order:

    ```bash
    python table_creation.py
    python bs_scraping.py
    python selenium_missing_data_scraping.py
    python data_scraping.py
    python wc_prediction.py
    ```

## File Structure
    .
    ├── table_creation.py                  # Creates and saves World Cup group tables (pickle)
    ├── bs_scraping.py                     # Scrapes World Cup match data using BeautifulSoup
    ├── selenium_missing_data_scraping.py  # Uses Selenium to scrape missing World Cup match data
    ├── data_scraping.py                   # Cleans and merges raw World Cup data files
    ├── wc_prediction.py                   # Predicts match outcomes and tournament progression
    ├── dict_table.pkl                     # Serialized group data table
    ├── fifa_worldcup_data.csv             # Raw match data CSV
    ├── fifa_missing_data.csv              # Missing matches scraped with Selenium
    ├── cleaned_df_worldcup_data.csv       # Cleaned and processed data CSV
    ├── fifa_worldcup_fixture.csv          # Match fixtures CSV
    └── README.md                          # This documentation file
