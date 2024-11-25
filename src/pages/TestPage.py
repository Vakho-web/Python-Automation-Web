from selenium.webdriver.common.by import By
from src.pages.DefaultPage import DefaultPage
from selenium.webdriver.support.ui import Select

class TestPage(DefaultPage):
    uname = (By.ID, 'urname')
    pword = (By.ID, 'urpass')
    login_button = (By.XPATH, "//input[@type='submit' and @value='ავტორიზაცია']")
    admin_button = (By.XPATH, "//button[@type='submit' and @name='choose_admin']")
    news_page = (By.XPATH, "//a[@class='menu-item-link' and .//div[@class='menu-item-title' and contains(normalize-space(.), 'სიახლის დამატება')]]")
    add_button = (By.XPATH, "//a[@href='?m=new&sm=new_new']")
    title = (By.ID, "title")
    news_type = (By.ID, "type")
    audience = (By.ID, "audience")
    use_date = (By.ID, "publish_date")
    delete_date = (By.ID, "unpublish_date")
    text = (By.XPATH, "//div[@class='ql-editor ql-blank' and @contenteditable='true']")
    image = (By.ID, "image")
    submit_button = (By.XPATH, "//input[@class='submit-button btn form-submit-btn' and @value='შენახვა' and @type='submit']")
    kid_news_button = (By.XPATH, "//a[@href='?m=news']")
    home_button = (By.XPATH, "//a[@href='?m=profile']")
    teacher_button = (By.NAME, "choose_teacher")
    teacher_news_page = (By.XPATH, "//a[@href='?m=news']")
    image_element = (By.XPATH, "//a[h2[@class='news-listing-title' and text()='1']]/div[@class='news-listing-img']")
    switch_to_admin_button = (By.NAME, "switch_to_admin")

    def get_news_type_dropdown(self):
        news_type_element = self.find_element(self.news_type)
        return Select(news_type_element)

    def get_audience_dropdown(self):
        audience_element = self.find_element(self.audience)
        return Select(audience_element)

    def enter_username(self, username):
        self.send_keys(self.uname, username)

    def enter_password(self, password):
        self.send_keys(self.pword, password)

    def click_login_button(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def admin_login(self, username, password):
        self.login(username, password)
        self.click(self.admin_button)

    def teacher_login(self, username, password):
        self.login(username, password)
        self.click(self.teacher_button)

    def go_to_news_page(self):
        self.click_out_of_view(self.news_page)

    def go_to_teacher_news_page(self):
        self.click_out_of_view(self.teacher_news_page)

    def add_news(self, title_input, news_type_input, audience_input, use_date_input, delete_date_input, text_input, image_input):
        self.click(self.add_button)
        self.send_keys(self.title, title_input)
        news_type_dropdown = self.get_news_type_dropdown()
        news_type_dropdown.select_by_value(news_type_input)
        audience_dropdown = self.get_audience_dropdown()
        audience_dropdown.select_by_value(audience_input)
        self.send_keys(self.use_date, use_date_input)
        self.send_keys(self.delete_date, delete_date_input)
        self.send_keys(self.text, text_input)
        self.send_keys(self.image, image_input)
        self.click(self.submit_button)

    def go_to_kids_news(self):
        self.click(self.kid_news_button)

    def news_title(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "h2.news-listing-title")

    def switch_to_admin(self):
        self.scroll_up()
        self.click(self.home_button)
        self.click(self.switch_to_admin_button)
