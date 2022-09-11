from selenium.webdriver.common.by import By
from Config.Config import TestData
from Page.BasePage import BasePage

""" This class contains all the By-locators (web elements) as well as the page actions (create/edit/complete/delete)
    related to to-do's """


class ToDoPage(BasePage):
    """ By locators present on this page """
    TEXT_BAR = (By.XPATH, "//input[@placeholder='What needs to be done?']")
    ACTIVE_TODO_COUNT_FOOTER = (By.XPATH, "//span[@class='todo-count']/strong")
    ACTIVE_TODO_NAME_TEXT = (By.XPATH, "//div[@class='view']//label")
    TODO_EDIT_BOX = (By.XPATH, "//input[@class='edit']")
    TOGGLE_ALL = (By.XPATH, "//input[@class='toggle']")
    MOVE_TO_LOCATOR = (By.XPATH, "//ul[@class='todo-list']")
    DESTROY_LOCATOR = (By.XPATH, "//li[@class='completed']//button[@class='destroy']")
    SECTION_LOCATOR = (By.XPATH, "//section")

    """ Constructor """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ This method will click on the text box to enter the to do's """
    def click_on_the_entry_text_box(self):
        self.click_method(self.TEXT_BAR)

    """ This method will enter the name of the to-do in the text box """
    def enter_todo_text(self, text):
        self.send_keys_method(self.TEXT_BAR, text)

    """ This method is to press the Enter key on the text box """
    def enter_key_on_the_entry_text_box(self):
        self.enter_key(self.TEXT_BAR)

    """ This method will create to-do's based on the input list """
    def create_to_dos(self, input_list):
        self.click_on_the_entry_text_box()
        for element in input_list:
            self.enter_todo_text(element)
            self.enter_key_on_the_entry_text_box()

    """ This method will return the count value of the active to-do's """
    def count_available_for_active_to_dos(self):
        count = self.get_text(self.ACTIVE_TODO_COUNT_FOOTER)
        return count

    """ This method will return all the active to-do's in the form of list """
    def get_active_to_dos_by_name(self):
        list_to_do = self.get_text_of_multiple_elements_in_list(self.ACTIVE_TODO_NAME_TEXT)
        return list_to_do

    """ This method will find a to-do based on the name and will return its web element """
    def find_todo_web_element_by_name(self, input_text):
        todo_element = self.return_web_element_based_on_input_text(self.ACTIVE_TODO_NAME_TEXT, input_text)
        return todo_element

    """ This method will find a to-do based on its name and return the name in text format """
    def find_todo_text_by_name(self, input_text):
        todo_element = self.return_web_element_based_on_input_text(self.ACTIVE_TODO_NAME_TEXT, input_text)
        return todo_element.text

    """ This method will find a to-do and edit it based on the input values provided: 
        current to-do name and 
        new to-do name 
         """
    def find_todo_and_edit(self, current_todo_name, new_todo_name):
        web_element = self.find_todo_web_element_by_name(current_todo_name)
        self.action_class_move_to_element_double_click(web_element)
        todo_edit = self.get_web_element(self.TODO_EDIT_BOX)
        self.action_class_move_double_click_send_text_enter_key(todo_edit, new_todo_name)

    """ This method will complete a to-do task based on the input from the user """
    def select_todo_by_name(self, todo_name):
        self.driver.find_element(By.XPATH, "//label[text()='{}']/preceding-sibling::input".format(todo_name)).click()
        # click_task_locator = (By.XPATH, "//label[text()='{}']/preceding-sibling::input".format(todo_name))
        # self.click_method(click_task_locator)

    """ This method will check all the active to-do's """
    def select_all_active_todo(self):
        list_elements = self.get_web_elements(self.TOGGLE_ALL)
        for ele in list_elements:
            ele.click()

    """ This method will check the completion of a specific to-do by its name """
    def check_completed_todo_by_name(self, todo_name):
        completed_task_locator = (By.XPATH, "//label[text()='{}']/parent::div/parent::li[@class='completed']"
                                  .format(todo_name))
        val = self.is_element_displayed(completed_task_locator)
        return val

    """ This method will delete all the completed to-do's """
    def delete_all_completed_todo(self):
        web_element = self.get_web_element(self.MOVE_TO_LOCATOR)
        self.action_class_move_to_element(web_element)
        web_elements = self.get_web_elements(self.DESTROY_LOCATOR)
        for ele in web_elements:
            ele.click()

    """ This method will find the total count of sections html tags """
    def find_total_section_tags(self):
        elements = self.get_web_elements(self.SECTION_LOCATOR)
        return len(elements)
