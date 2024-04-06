from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class music():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)

        video = self.driver.find_element('xpath','//*[@id="meta"]')
        video.click()

    def wait_to_close(self):
        input("Press Enter to close the browser...")
        self.driver.quit()

# assist = music()
# assist.play('Arjit Singh Songs')
# assist.wait_to_close()
