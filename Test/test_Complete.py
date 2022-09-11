from Config.Config import TestData
from Page.ToDoPage import ToDoPage
from Test.test_Base import BaseTest

""" This class is to test the completion of to-do's """


class TestComplete(BaseTest):
    """ This method will check if a specific to-do is completed successfully """

    def test_complete_a_specific_to_do(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_MULTIPLE_TODO)
        self.todo_page.select_todo_by_name(TestData.TASK_TO_BE_COMPLETED)
        value = self.todo_page.check_completed_todo_by_name(TestData.TASK_TO_BE_COMPLETED)
        assert value == TestData.BOOL_TRUE

    """ This method will check the successful completion of all the to-do's """

    def test_complete_all_to_do(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_MULTIPLE_TODO)
        self.todo_page.select_all_active_todo()
        count = self.todo_page.count_available_for_active_to_dos()
        assert count == TestData.COMPLETED_TODO_ALL_COUNT_FOOTER
