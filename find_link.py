from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://lab.fi/fi/haku?keywords=erasmus")
    time.sleep(3)

    links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Erasmus")

    print("Number of Erasmus links found:", len(links))

    for i, link in enumerate(links):
        print(
            i,
            "| Text:", link.text,
            "| URL:", link.get_attribute("href")
        )

finally:
    driver.quit()