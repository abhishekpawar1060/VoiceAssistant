from selenium import webdriver
import time



class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")

        search = self.driver.find_element('id', 'searchInput')
        search.click()
        search.send_keys(query)  # Use send_keys instead of send_key
        enter = self.driver.find_element('xpath', '//*[@id="search-form"]/fieldset/button')
        enter.click()

    def wait_to_close(self):
        input("Press Enter to close the browser...")
        self.driver.quit()

