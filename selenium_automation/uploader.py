import time
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Yad2Uploader:
    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = Chrome(
            service=Service(),
            options=chrome_options
        )
        self.driver.get("https://www.yad2.co.il/my-ads")
        self.main_window = self.driver.current_window_handle

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

    def get_my_ads_links(self) -> list[str]:
        link_objects = self.driver.find_elements(By.CLASS_NAME, 'grid_shadowLink__gzEug')
        return [link_object.get_attribute("href") for link_object in link_objects]

    def



if __name__ == '__main__':
    pass