import os
import pytest
import csv
from selenium.webdriver.common.by import By
from src.pages.TestPage import TestPage
from src.utils.ConfigReader import get_config
from src.utils.Driver import get_driver

def data_read():
    location = os.path.join(os.path.dirname(__file__), "../resources/LoginCred.csv")
    with open(location, 'r') as file:
        obj = csv.DictReader(file)
        return [{"username": row["username"], "password": row["password"], "type": row["type"]} for row in obj]

def news_data_read():
    location = os.path.join(os.path.dirname(__file__), "../resources/NewsTestData.csv")
    with open(location, 'r') as file:
        obj = csv.DictReader(file)
        return [{"title_input": row["title_input"],
                 "news_type_input": row["news_type_input"],
                 "audience_input": row["audience_input"],
                 "use_date_input": row["use_date_input"],
                 "delete_date_input": row["delete_date_input"],
                 "text_input": row["text_input"],
                 "image_input": row["image_input"], } for row in obj]

@pytest.fixture()
def setup(request):
    config = get_config()
    driver = get_driver(config["browser_name"])
    driver.get(config["base_url"])
    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("admin_data",
                             [admin_entry for admin_entry in data_read() if admin_entry["type"] == "admin"])
    def test_admin_tasks(self, admin_data):
        testing_page = TestPage(self.driver)
        testing_page.admin_login(admin_data["username"], admin_data["password"])
        testing_page.go_to_news_page()

        news_data = news_data_read()
        for news_entry in news_data:
            testing_page.add_news(news_entry["title_input"],
                                  news_entry["news_type_input"],
                                  news_entry["audience_input"],
                                  news_entry["use_date_input"],
                                  news_entry["delete_date_input"],
                                  news_entry["text_input"],
                                  news_entry["image_input"])

        print(" All News Created Successfully.")
#=====================================================

    @pytest.mark.parametrize("kid_data", [kid_entry for kid_entry in data_read() if kid_entry["type"] == "kid"])
    def test_kid_view(self, kid_data):
        testing_page = TestPage(self.driver)
        testing_page.login(kid_data["username"], kid_data["password"])
        testing_page.go_to_kids_news()

        news_titles = testing_page.news_title()

        assert any(title.text.strip() == "Vakho News All" for title in news_titles), \
                "'Vakho News All' not found in any title."
        assert any(title.text.strip() != "Vakho News Teacher/Parent" for title in news_titles), \
                "Teacher/Parent News visible to Kid"

        print(" News is shown correctly for kid.")
    # =====================================================

    @pytest.mark.parametrize("admin_data",
                             [admin_entry for admin_entry in data_read() if admin_entry["type"] == "admin"])
    def test_teacher_view(self, admin_data):
        testing_page = TestPage(self.driver)
        testing_page.teacher_login(admin_data["username"], admin_data["password"])
        testing_page.go_to_teacher_news_page()

        news_titles = testing_page.news_title()
        assert any(
            title.text.strip() == "Vakho News All" and testing_page.has_non_empty_background(
                title.find_element(By.XPATH, "../div[@class='news-listing-img']")
            )
            for title in news_titles
        ), "'Vakho News All' not visible or has no background image."

        assert any(
            title.text.strip() == "Vakho News Teacher/Parent" and testing_page.has_non_empty_background(
                title.find_element(By.XPATH, "../div[@class='news-listing-img']")
            )
            for title in news_titles
        ), "'Vakho News Teacher/Parent' not visible or has no background image."

        testing_page.switch_to_admin()
        testing_page.go_to_news_page()

        news_rows = testing_page.get_news_rows()
        assert any(
            row.find_element(By.CSS_SELECTOR, ".table-news-title").text.strip() == "Vakho Future News" and
            row.find_element(By.CSS_SELECTOR, ".table-news-status .status-inactive").text.strip() == "არააქტიური"
            for row in news_rows
        ), "'Vakho Future News' not found or its status is not 'არააქტიური'"

        print(" All assertions passed successfully.")










