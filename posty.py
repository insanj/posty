import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup
opts = webdriver.ChromeOptions()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")

chromedriver = os.path.join(os.getcwd(), "chromedriver.exe")

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=opts)

# Step One
driver.get("https://postmates.com/feed")

# Step Two
field = driver.find_element_by_css_selector("input")
field.send_keys("1942 E York St, Philadelphia, PA")
button = driver.find_element_by_css_selector("#e2e-go-button")
button.click()

try:
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=presentation]")))
finally:
	restaurants = driver.find_elements_by_css_selector("div[role=presentation]")
	for r in restaurants:
		print("\n------- RESTAURANT --------")
		print(r.find_element_by_css_selector("img").get_attribute("alt"))
		# print(r.get_attribute('innerHTML'))
		contents = r.get_attribute('innerHTML')
		regex = "</?\\w+((\\s+\\w+(\\s*=\\s*(?:\".*?\"|'.*?'|[\\^'\">\\s]+))?)+\\s*|\\s*)/?>"
		trimmed = re.sub(regex, "", contents)
		print(trimmed)
	driver.quit()

