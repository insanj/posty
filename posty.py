import re
import os
from selenium import webdriver

# Setup
opts = webdriver.ChromeOptions()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")

chromedriver = os.path.join(os.getcwd(), "chromedriver.exe")

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=opts)

# Step One
driver.get("https://postmates.com/feed")

# Step Two
field = driver.getElementForSelector("input")
field.send_keys("1942 E York St, Philadelphia, PA")
field.submit()

# restaurants = driver.find_elements_by_css_selector("div[role=presentation]")
