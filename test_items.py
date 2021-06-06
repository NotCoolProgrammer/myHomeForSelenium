import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_availability(browser):
    browser.get(link)

    button = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    # для корректной проверки выполненного задания раскомментируйте строчку ниже
    # time.sleep(30)
    assert button > 0, 'Нет такой кнопки'
