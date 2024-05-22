from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class sauce_cookies:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15

    # Initialize the ChromeDriver
    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    # Open a website
    def open_website(self, url):
        self.driver.get(url)

   # Maximize the browser window
    def maximize_window(self):
        self.driver.maximize_window()

# Wait for an element to be clickable
    def click(self, locator, timeout=None):
        timeout = timeout or self.wait_timeout
        return WebDriverWait(self.driver, timeout).until( EC.element_to_be_clickable(locator))
# Login the Page
    def Login_Page(self):
        username_input = self.driver.find_element(By.ID,"user-name")
        username = "standard_user"
        username_input.send_keys(username)
        time.sleep(3)
        #password
        password_input = self.driver.find_element(By.ID,"password")
        password = "secret_sauce"
        password_input.send_keys(password)
        time.sleep(3)
        #login
        login_button = self.driver.find_element(By.ID,"login-button")
        login_button.click()

        # Get cookies before login
    def capture_cookies_before_login(self):
            self.cookies_before_login = self.driver.get_cookies()
            #print("Before login cookies:", self.cookies_before_login)

        # Get cookies after login
    def capture_cookies_after_login(self):
            self.cookies_after_login = self.driver.get_cookies()
            #print("After login cookies:", self.cookies_after_login)

    def display_cookies(self):
        if self.cookies_before_login:
          print("Cookies before login:")
        for cookie in self.cookies_before_login:
            print(cookie)
        else:
                print("No cookies captured before login.")

        if self.cookies_after_login:
            print("\nCookies after login:")
            for cookie in self.cookies_after_login:
             print(cookie)
        else:
             print("No cookies captured after login.")


# LogOut the Page
    def Logout(self):
        logout_button = self.driver.find_element(By.ID,"react-burger-menu-btn")
        logout_button.click()
        time.sleep(3)
        logout_link = self.driver.find_element(By.ID,"logout_sidebar_link")
        logout_link.click()
        time.sleep(3)

    def close(self):
        self.driver.close()

# Create object
sauce = sauce_cookies()

# Initialize the browser
sauce.initialize_driver()

# Navigate to URL
sauce.open_website("https://www.saucedemo.com/")
time.sleep(3)

# Maximize the window
sauce.maximize_window()

# Get cookies before login
sauce.capture_cookies_before_login()
time.sleep(3)

# Login to the page
sauce.Login_Page()
time.sleep(3)

# Get cookies after login
sauce.capture_cookies_after_login()
time.sleep(3)

# Display captured cookies
sauce.display_cookies()

# Logout from the page
sauce.Logout()
time.sleep(3)

# Close the browser
sauce.close()





