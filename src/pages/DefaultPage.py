from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DefaultPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, text, timeout = 10):
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def click(self, locator, timeout = 10):
        element = self.find_element(locator, timeout)
        element.click()

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.driver.execute_script("window.scrollBy(0, -document.body.scrollHeight);")

    def click_out_of_view(self, locator, timeout = 10):
        element = self.find_element(locator, timeout)
        self.scroll()
        self.actions.move_to_element(element)
        element.click()

    def has_non_empty_background(self, locator):
        style = locator.get_attribute('style')
        return 'background: url(' in style and 'uploads/' in style

    def get_news_rows(self):
        return self.driver.find_elements(By.XPATH, "//tr[td[contains(@class, 'table-news-title')]]")