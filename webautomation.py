from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()

# 1 - Navigate the URL
driver.get('http://automationexercise.com') 

# 2 - Verify that home page is visible successfully
home_icon = driver.find_element(By.CLASS_NAME, "fa-home")
assert home_icon.is_displayed()
print("Home page is visible (home icon found).")

# 3 -  Click on 'Signup / Login' button
loginButton = driver.find_element(By.CLASS_NAME, "fa-lock")
loginButton.click()
print("Login Button clicked")

# 4 -  Verify 'New User Signup!' is visible
element = driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
try:
    assert "New User Signup!" in element.text
    print("New User SignUp is visible")
except:
    print("Failed")

# 5 - Enter name and email address
name = driver.find_element(By.NAME, "name")
email = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[3]")
name.send_keys("Daniel")
email.send_keys("ayishhdaniel16@gmail.com")

# 6 - Click Sign Up Button
signupButton = driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/button")
signupButton.click()

# 8 - Verify that 'ENTER ACCOUNT INFORMATION' is visible
try:
    element2 = driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/h2/b")
    assert "ENTER ACCOUNT INFORMATION" in element2.text
    print("'Enter Account Information' is visible")
except: 
    print("'Enter Account Information' is NOT visible")

# 9 - Fill details: Title, Name, Email, Password, Date of birth
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="id_gender1"]').click()
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[4]/input").send_keys("password123")
day_select = Select(driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/div/div[1]/div/select"))
month_select = Select(driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/div/div[2]/div/select"))
year_select = Select(driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/div/div[3]/div/select"))
day_select.select_by_value("20")
month_select.select_by_value("9")
year_select.select_by_value("2003")

# 10 - Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/div[6]/div/span/input").click()

# 11 - Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/form/div[7]/div/span/input").click()

# 12 - Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/p[1]/input").send_keys("Muhammad Fariez Daniel")
driver.find_element(By.XPATH, '//*[@id="last_name"]').send_keys("Baharudin")
driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys("Jalan 12, 34A, Taman Ria")
driver.find_element(By.XPATH, '//*[@id="address2"]').send_keys("Petaling Jaya, Selangor")
country_select = Select(driver.find_element(By.XPATH, '//*[@id="country"]'))
country_select.select_by_value("United States")
driver.find_element(By.XPATH, '//*[@id="state"]').send_keys("Pennsylvania")
driver.find_element(By.XPATH, '//*[@id="city"]').send_keys("State College")
driver.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys("16803")
driver.find_element(By.XPATH, '//*[@id="mobile_number"]').send_keys("2232573728")

# 13 - Click 'Create Account button'
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/form/button').click()

# 14 - Verify that 'ACCOUNT CREATED!' is visible
try:
    element3 = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    assert "ACCOUNT CREATED!" in element3.text
    print("'ACCOUNT CREATED!' is visible")
except: 
    print("'ACCOUNT CREATED!' is not visible")

# 15 - Click 'Continue' button
driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()

# 16 - Verify that 'Logged in as username' is visible
try:
    element3 = driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    assert "Logged in as Daniel" in element3.text
    print("'Logged in as Daniel' is visible")
except: 
    print("'Logged in as Daniel' is not visible")

# 17 - Click 'Delete Account' button
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]').click()

# 18 - Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
try:
    element3 = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    assert "ACCOUNT DELETED!" in element3.text
    print("'ACCOUNT DELETED' is visible")
except: 
    print("'ACCOUNT DELETED' is not visible")

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()









time.sleep(100)
