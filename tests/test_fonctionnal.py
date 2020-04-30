from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(chrome_options=options)

class SeleniumTest(StaticLiveServerTestCase):
    pass