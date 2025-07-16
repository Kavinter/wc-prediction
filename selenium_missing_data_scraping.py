from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

path = r"C:\Users\Kavinter\Desktop\za skolu\Selenium vezba\geckodriver.exe"

service = Service(executable_path=path)


driver = webdriver.Firefox(service=service)


driver.get("https://en.wikipedia.org/wiki/1990_FIFA_World_Cup")


rows = driver.find_elements(By.CSS_SELECTOR, 'tbody > tr[style="font-size:90%"]')

home = []
score = []
away = []

for row in rows:

    tds = row.find_elements(By.TAG_NAME, "td")
    if len(tds) >= 3:

        home.append(tds[0].find_element(By.TAG_NAME, "a").text.strip())

        score.append(tds[1].find_element(By.TAG_NAME, "b").text.strip())

        away.append(tds[2].find_element(By.TAG_NAME, "a").text.strip())


driver.quit()

dict_football = {"home": home, "score": score, "away": away}
df_football = pd.DataFrame(dict_football)
df_football["year"] = 1990
df_football.to_csv("fifa_missing_data.csv", index=False)
