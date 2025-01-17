import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PostyConfig:
	exe = None
	useragent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	timeout = 10

	def __init__(self):
		filename = "chromedriver"
		self.exe = os.path.join(os.getcwd(), filename)

class PostyUser:
	address = "1900 E York St, Philadelphia, PA"

class PostySpec:
	home = "https://postmates.com"
	feed = "https://postmates.com/place-groups/postmates-plus-philadelphia"
	field = "input"
	button = "#e2e-go-button"
	homeRestaurant = "div[role=presentation]"
	restaurant = '[id^="e2e-feed-place-item"]'

class PostyDriver:
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

	def navigateTo(self, url):
		self.driver.get(url)

	def navigateToHome(self):
		self.navigateTo(self.spec.home)

	def navigateToFeed(self):
		self.navigateTo(self.spec.feed)

	def fillAddressInHome(self):
		field = self.driver.find_element_by_css_selector(self.spec.field)
		field.send_keys(self.user.address)

	def clickAddressInHome(self):
		button = self.driver.find_element_by_css_selector(self.spec.button)
		button.click()

	def waitUntilHomeLoads(self):
		r = None
		try:
			r = WebDriverWait(self.driver, self.config.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.spec.homeRestaurant)))
		finally:
			return r

	def findAllRestaurantElements(self):
		return self.driver.find_elements_by_css_selector(self.spec.restaurant)

	def convertRestaurantElementToString(self, ele):
		# name = ele.find_element_by_css_selector("img").get_attribute("alt")
		contents = ele.get_attribute('innerHTML')
		regex = "</?\\w+((\\s+\\w+(\\s*=\\s*(?:\".*?\"|'.*?'|[\\^'\">\\s]+))?)+\\s*|\\s*)/?>"
		trimmed = re.sub(regex, "", contents)
		cleaned = trimmed.replace("$", " $")
		return cleaned

	def quit(self):
		self.driver.quit()

class Posty:
	driver = None
	def __init__(self, driver=PostyDriver()):
		self.driver = driver

	def navigateToHomeAndGetFeedRestaurantStrings(self):
		self.driver.navigateToHome()
		self.driver.fillAddressInHome()
		self.driver.clickAddressInHome()
		self.driver.waitUntilHomeLoads()
		self.driver.navigateToFeed()

		restaurants	= self.driver.findAllRestaurantElements()
		strings = []
		for r in restaurants:
			strings.append(self.driver.convertRestaurantElementToString(r))
		return strings

	def quit(self):
		self.driver.quit()

if __name__ == "__main__":
	print("\n\nRunning Posty v1!! Here are all the restaurants I found nearby...\n")
	posty = Posty()
	places = posty.navigateToHomeAndGetFeedRestaurantStrings()
	for p in places: print("- " + p)
	posty.quit()
	print("See ya next time!\n\n")
