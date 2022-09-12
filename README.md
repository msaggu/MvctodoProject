
# **TodoMVC-AngularJS automation framework (proof of concept)**  
## The proof of concept automation framework is developed using Python, Selenium library and pytest testing framework.


## URL: 
## TodoMVC-AngularJS https://todomvc.com/examples/angular2/

## Pre-requisite(s):

- Make sure to have Python installed on your machine

- Install Selenium library: 
  ```python 
  pip install selenium
  ``` 

- Install pytest (testing framework): 
```python
pip install pytest
```

- Install web driver manager (to manage and launch web-browsers): 
```python
pip install webdriver-manager
``` 

- To generate HTML Report: 
```python
pip install pytest-html
```

The todomvc applicable is a single-page application where the user can perform the following operations: 
- create to-do tasks
- edit to-do tasks
- delete to-do tasks
- complete to-do tasks

The automation framework contains the following components:
- BasePage class under Page directory. This class uses the conftest fixture.
- ToDoPage class under the Page directory. This class defines all the locators and page actions for the main page
- conftest class under the Test directory. This class is responsible for the setup and Teardown operations
- test_Create class under the Test directory. This class is responsible for checking the to-do create actions defined under ToDoPage class utilizing 	assertions 
- test_Edit class under the Test directory. This class is responsible for checking the to-do edit actions defined under ToDoPage class utilizing 	assertions 
- test_Complete class under the Test directory. This class is responsible for checking the to-do completion actions defined under ToDoPage class utilizing 	assertions 
- test_Delete class under the Test directory. This class is responsible for checking the to-do delete actions defined under ToDoPage class utilizing 	assertions 

## How to Run:

To run an individual test class, cd to the Test folder and use the below command:
pytest "name of the test class" -v -s 
Ex - 
```python
pytest test_Create.py -v -s 
```

 


