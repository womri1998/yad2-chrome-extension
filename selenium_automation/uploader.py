import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


BUTTON_CONTAINER_NAME = 'action-button_actionButtonContainer__2k0KY'
BUTTON_CLASS_NAME = 'bump-button_bumpButton__f0roc'
BUMP_LABEL_CLASS_NAME = 'action-button_actionButtonLabel__WWXHf'


class Yad2Bumper:
    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = Chrome(
            service=Service(),
            options=chrome_options
        )
        self.driver.get("https://www.yad2.co.il/my-ads")

    def scroll_down(self):
        scroll_pause_time = 0.5
        max_scrolls = 10
        last_heights = [self.driver.execute_script("return document.body.scrollHeight")] * max_scrolls
        reached_end = False
        while not reached_end:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_heights[-10]:
                reached_end = True
            last_heights = last_heights[1:] + [new_height]

    def bump_my_ads(self):
        bump_divs = self.driver.find_elements(By.CLASS_NAME, BUTTON_CONTAINER_NAME)
        bump_divs = [
            element for element in bump_divs
            if element.get_attribute('data-testid') == 'bump-ad-action-button'
        ]
        for i, div in enumerate(bump_divs):
            button = div.find_element(By.CLASS_NAME, BUTTON_CLASS_NAME)
            label = div.find_element(By.CLASS_NAME, BUMP_LABEL_CLASS_NAME).text
            if label == 'הקפצה':
                button.click()
                time.sleep(5)
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


if __name__ == '__main__':
    yad2bumper = Yad2Bumper()
    yad2bumper.scroll_down()
    yad2bumper.bump_my_ads()