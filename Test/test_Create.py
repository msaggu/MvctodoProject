from Config.Config import TestData
from Page.ToDoPage import ToDoPage
from Test.test_Base import BaseTest

""" This class is to check the creation of to-do's """


class TestCreate(BaseTest):
    """ This test will check if 1 to-do task is successfully created """

    def test_create_todo_list_with_one_item(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_ONE_TODO)
        expected = self.todo_page.get_active_to_dos_by_name()
        assert expected == TestData.LIST_ONE_TODO

    """ This test will check if multiple to-do's are successfully created """

    def test_create_todo_list_with_multiple_items(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_MULTIPLE_TODO)
        expected = self.todo_page.get_active_to_dos_by_name()
        assert expected == TestData.LIST_MULTIPLE_TODO
