from Config.Config import TestData
from Page.ToDoPage import ToDoPage
from Test.test_Base import BaseTest

""" This class is to check the deletion of to-do's """


class TestDelete(BaseTest):
    """ This method will test the deletion of all the completed to-do's """

    def test_deletion_of_all_completed_to_dos(self):
        self.todo_page = ToDoPage(self.driver)
        self.todo_page.create_to_dos(TestData.LIST_MULTIPLE_TODO)
        self.todo_page.select_all_active_todo()
        self.todo_page.delete_all_completed_todo()
        count = self.todo_page.find_total_section_tags()
        assert count == TestData.SECTION_TAGS_COUNT
