from Config.Config import TestData
from Page.ToDoPage import ToDoPage
from Test.test_Base import BaseTest

""" This class is to test the to-do edit """


class TestEdit(BaseTest):
    """ This test will check if a particular to-do is edited successfully """

    def test_edit_to_do_task(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_MULTIPLE_TODO)
        self.todo_page.find_todo_and_edit(TestData.TODO_TO_EDIT, TestData.NEW_TODO_NAME)
        expected = self.todo_page.find_todo_text_by_name(TestData.NEW_TODO_NAME)
        assert expected == TestData.NEW_TODO_NAME
