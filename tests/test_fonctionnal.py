from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model

from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True

class SeleniumChromeFunctionalTestCases(StaticLiveServerTestCase):
    """Tests fonctionnels utilisant le navigateur Web GoogleChrome."""

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(username="jerem", password="Jerem33")


    def tearDown(self):
        self.driver.close()

    def test_user_can_disconnect_and_connect(self):
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys("jerem")
        self.driver.find_element_by_css_selector('#id_password').send_keys("Jerem33")
        self.driver.find_element_by_css_selector('#button-submit').click()

        logout = self.driver.find_element_by_css_selector('#button-logout')

        self.assertEqual(logout.text, "", "Le bouton de déconnexion devrait être disponible.")
    