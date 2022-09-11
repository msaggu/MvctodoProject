import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
This class contains generic methods and utilities
"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """ This method will locate and click the web element 
        :parameter - by locator 
        """
    def click_method(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """ This method will locate the web element and send keys to it 
        :parameter - by locator and inout text 
        """
    def send_keys_method(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """ This method will find the web element and press the ENTER key 
        :parameter - by locator
        """
    def enter_key(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    """ This method will return the web element based on the by locator 
        :parameter - by locator 
        :return - web element 
        """
    def get_web_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    """ This method will return the web elements based on the by locator 
            :parameter - by locator 
            :returns - List of web elements 
            """
    def get_web_elements(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))

    """ This method will find the text of the web element 
        :parameter - by locator
        :return - text """
    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    """ This method will check if the web element is displayed 
        :parameter - by locator
        :return - Boolean """
    def is_element_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    """ This method will return the list of to-do's by its names 
        :parameter - by locator
        :returns - List of to-do's by its name """
    def get_text_of_multiple_elements_in_list(self, by_locator):
        text_list = []
        list_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        for ele in list_elements:
            text_list.append(ele.text)
        return text_list

    """ This method will return the web element of to-do 
            :parameter - by locator, name of the to-do
            :returns - to-do web element """
    def return_web_element_based_on_input_text(self, by_locator, input_text):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        for ele in elements:
            if ele.text == input_text:
                return ele

    """ This method will check if a to-do is present 
        :parameter - by locator, name of the to-do
        :return - Boolean """
    def is_todo_present(self, by_locator, input_text):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        for ele in elements:
            if ele.text == input_text:
                return True

    """ This action class will move to a web element 
        :parameter - web element """
    def action_class_move_to_element(self, web_element):
        action = ActionChains(self.driver)
        action.move_to_element(web_element)
        action.perform()

    """ This action class will move to a web element and double click on it 
        :parameter - web element """
    def action_class_move_to_element_double_click(self, web_element):
        action = ActionChains(self.driver)
        action.move_to_element(web_element)
        action.double_click(web_element)
        action.perform()

    """ This action class will move to a web element, double click on it and send text 
        :parameter - web element, text value """
    def action_class_move_double_click_send_text_enter_key(self, web_element, text):
        action = ActionChains(self.driver)
        action.move_to_element(web_element)
        action.double_click(web_element)
        action.send_keys(text)
        action.send_keys(Keys.ENTER)
        action.perform()





