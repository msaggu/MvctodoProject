import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

""" This file is responsible for setup and tear down methods provided on the basis of the defined scope """


@pytest.fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        request.cls.driver = web_driver
        yield
        web_driver.close()
