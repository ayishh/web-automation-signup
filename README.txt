
Web Automation Signup Project
=============================

This project automates the user sign-up flow on http://automationexercise.com using Selenium WebDriver in Python.

It performs actions like opening a browser, filling out a sign-up form, selecting drop-down values, checking boxes, and verifying successful account creation and deletion.

Files Included
--------------
- webautomation.py  : Main Python script for browser automation
- requirement.txt   : List of Python packages used (like Selenium)
- README.txt        : Project documentation (this file)

Tools & Technologies Used
--------------------------
- Language: Python
- Library: selenium
- Browser Driver: ChromeDriver
- Target Website: http://automationexercise.com

Requirements
------------
- Python 3.x installed
- Google Chrome browser
- Compatible ChromeDriver
- Install dependencies using:
  pip install -r requirement.txt

How to Run
----------
1. Open a terminal in the project directory
2. Ensure ChromeDriver is in your system PATH
3. Run the script using:
   python webautomation.py

Explanation of Key Concepts Used
--------------------------------

WebDriver Initialization:
    driver = webdriver.Chrome()
    driver.maximize_window()

Navigating and Validating Pages:
    driver.get('http://automationexercise.com')
    assert home_icon.is_displayed()

Finding Elements (By Methods):
    - By.CLASS_NAME
    - By.NAME
    - By.XPATH
    Examples:
        driver.find_element(By.CLASS_NAME, "fa-lock")
        driver.find_element(By.NAME, "name")
        driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")

Drop-downs (Select class):
    from selenium.webdriver.support.ui import Select
    day_select = Select(driver.find_element(...))
    day_select.select_by_value("20")

Wait for Stability:
    time.sleep(5)

Verifying Results with Assertions:
    assert "ACCOUNT CREATED!" in element.text

Steps Performed by Script
--------------------------
1. Visit automationexercise.com
2. Click Signup/Login
3. Fill out name and email
4. Click Sign Up
5. Fill in gender, password, DOB, checkboxes, address, and contact info
6. Click Create Account
7. Verify Account Created! message
8. Click Continue
9. Verify Logged in as [username]
10. Click Delete Account
11. Confirm Account Deleted!
12. End

Author
------
Muhammad Fariez Daniel


