import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def PostyConfig(Object):
	exe = os.path.join(os.getcwd(), "chromedriver.exe")
	useragent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	timeout = 10

def PostyUser(Object):
	address = "1942 E York St, Philadelphia, PA"

def PostySpec(Object):
	home = "https://postmates.com"
	field = "input"
	button = "#e2e-go-button"
	restaurant = "div[role=presentation]"

def PostyDriver(Object):
	config = None
	user = None
	spec = None
	driver = None

	def __init__(self, config=PostyConfig(), user=PostyUser(), spec=PostySpec()):
		self.config = config
		self.user = user
		self.spec = spec
		self.setup()

	def setup(self):
		opts = webdriver.ChromeOptions()
		opts.add_argument(self.config.useragent)
		self.driver = webdriver.Chrome(executable_path=self.config.exe, chrome_options=opts)

	def navigateToHome(self):
		self.driver.get(self.spec.home)

	def fillAddressInHome(self):
		field = self.driver.find_element_by_css_selector(self.spec.field)
		field.send_keys(self.user.address)

	def clickAddressInHome(self):
		button = self.driver.find_element_by_css_selector(self.spec.button)
		button.click()

	def waitUntilFeedLoads(self):
		r = None
		try:
			r = WebDriverWait(self.driver, self.config.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.spec.restaurant)))
		finally:
			return r

	def quit(self):
		self.driver.quit()

def Posty(Object):
	driver = None
	def __init__(self, driver=PostyDriver()):
		self.driver = driver

	def navigateToHomeAndGetToFeed(self):
		self.driver.navigateToHome()
		self.driver.fillAddressInHome()
		self.driver.clickAddressInHome()

		result = self.driver.waitUntilFeedLoads()
		restaurants = self.driver.find_elements_by_css_selector("div[role=presentation]")
		for r in restaurants:
			print("\n------- RESTAURANT --------")
			print(r.find_element_by_css_selector("img").get_attribute("alt"))
			# print(r.get_attribute('innerHTML'))
			contents = r.get_attribute('innerHTML')
			regex = "</?\\w+((\\s+\\w+(\\s*=\\s*(?:\".*?\"|'.*?'|[\\^'\">\\s]+))?)+\\s*|\\s*)/?>"
			trimmed = re.sub(regex, "", contents)
			print(trimmed)

	def quit(self):
		self.driver.quit()

if __name__ == "__main__":
	p = Posty()
	p.navigateToHomeAndGetToFeed()
	p.quit()
