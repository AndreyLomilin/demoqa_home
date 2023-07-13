import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    # browser.get('https://demoqa.com/')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()