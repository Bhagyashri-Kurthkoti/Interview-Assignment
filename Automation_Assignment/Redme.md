**Interview Assignment**


The assignment project consists of test cases automated for https://www.saucedemo.com/ web application using a framework comprising of Selenium, Python, and Pytest. The framework is based on the Page Object 
Model design pattern to make the code maintainable, scalable, and easy to read. The HTML reports are generated after the test run for better visibility of the test results.

**Setup**

To run the tests, you will need to install the following dependencies:

* Python 3.x
* Selenium
* Pytest
* Pytest-html

**Project Structure**

The project follows the following directory structure:

Project Assignment
*     Configurations
  *     Config.ini
*     Logs
  *     automation_logs.log
*     Reports
  *     reports.html
*     Pages
  *     LoginInvalidCredential.py
  *     LoginSignUp.py
  *     OrderProducts.py
*     Tests
  *       conftest.py
  *       test_invalid_cred_login.py
  *       test_order.py
  *       test_signup.py
  *       test_valid_cred_login.py

**Logs**  

Logs folder consists of automation logs generated for every run.

**Tests**

The tests are defined within the package testCases.

**Page Objects**

The page objects are defined within the package pageObjects.

**Fixtures**

The fixtures are defined within the conftest.py file.

**HTML Reports**

The HTML reports are generated after the test cases run.

**Screenshots**

Screenshots folder consists of error screenshots for every test.

**Deployment**

To run the test cases, switch to the testCases folder from the current directory using the following command:

    cd testCases

To run all tests together, use the following command:

    pytest --html=<project_current_directory>/Reports/reports.html
Note: Replace <project_current_directory> with the actual directory path of the project.