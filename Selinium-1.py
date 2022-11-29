from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.google.com")

print(driver.title)

search = driver.find_element(By.CLASS_NAME,"gLFyf")
search.send_keys("swTesting")
search.send_keys(Keys.RETURN)

time.sleep(5)

try:
    searchResults = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rso"))
    )

    results = searchResults.find_elements(By.CLASS_NAME, "MjjYud")
    for r in results:
        print(r.text) 

    print("done")
except:
    print("Failed")
    driver.quit()

