# import logging
# from selenium import webdriver
# from datetime import datetime
# from src.pages.LoginPage import LoginPage
# from selenium.common.exceptions import NoSuchElementException
#
# timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# log_filename = f'D:\\Downloads\\Coding\\Code\\Pycharm\\HomeworkProject\\reports\\logs\\log_{timestamp}.log'
#
# logging.basicConfig(
#     filename=log_filename,
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s',
# )
#
# logging.info("Logging system initialized")
#
# try:
#     driver = webdriver.Chrome()
#     logging.info("Driver opened")
#     driver.get("https://e-school.ge/")
#     logging.info("Webpage opened")
#     login_page = LoginPage(driver)
#     login_page.login("tap@gmail.com", "123")
#     logging.info("Login Successful")
#
# except NoSuchElementException as e:
#     logging.error(f"Something went wrong: {e}")
# except AssertionError as e:
#     logging.error(f"Something went wrong: {e}")
# except:
#     logging.error("Something went wrong")
# finally:
#     driver.quit()
#     logging.info("Driver closed")