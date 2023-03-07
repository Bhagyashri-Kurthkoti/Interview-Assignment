
# Interview Assignment

The assignment project consists of test cases automated for https://www.saucedemo.com/ web application using a framework comprising of Selenium, Python, and Pytest. The framework is based on the Page Object Model design pattern to make the code maintainable, scalable, and easy to read. The HTML reports are generated after the test run for better visibility of the test results.


Setup:

To run the tests, you will need to install the following dependencies:

    Python 3.x
    Selenium 
    Pytest
    Pytest-html

## Project Structure
The project follows the following directory structure:

__Project Assignment__
  - Configurations
    - Config.ini
  - Logs
    - automation_logs.log
  - Reports
    - reports.html
  - Screenshots
  - Fixtures
    - conftest.py
  - Pages
    - LoginInvalidCredential.py
    - LoginSignUp.py
    - OrderProducts.py
  - Tests
    - conftest.py
    - test_invalid_cred_login.py
    - test_order.py
    - test_signup.py
    - test_valid_cred_login.py
  - utilities
    - customLogger.py
    - random_user_credentials.py
    - readProperties.py
  
__Logs__  

Logs folder consists of automation logs generated for every run.

__Page Objects__

The page object files are defined within the pageObjects package.

__Tests__

The tests are defined within the testCases package. 

**Screenshots**

Screenshots folder consists of error screenshots for every test.

__Fixtures__

The fixtures are defined in the conftest.py file. 

__HTML Reports__

The HTML reports are generated after the test cases run.

__utilities__

The utility files are present within utilities package. 

## Deployment

To run the test cases, switch to the testCases folder from the current directory using the following command:

```bash
cd testCases
```
To run all tests together use command, 
```bash
pytest --html=project_current_directory\Reports\reports.html

