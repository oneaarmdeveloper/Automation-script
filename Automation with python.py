from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver (Make sure chromedriver.exe is in the same folder)
driver = webdriver.Chrome()

# Open the form URL
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

# Pause to allow elements to load
time.sleep(10)

# Fill in first and last name
driver.find_element(By.NAME, "firstname").send_keys("Chukwuebuka")
driver.find_element(By.NAME, "lastname").send_keys("Anselm")

# Select gender (Male)
driver.find_element(By.ID, "sex-0").click()

# Select experience (3 years)
driver.find_element(By.ID, "exp-2").click()

# Enter today's date
driver.find_element(By.ID, "datepicker").send_keys("02-10-2025")

# Select profession (Automation Tester)
driver.find_element(By.ID, "profession-1").click()

# Select tool (Selenium WebDriver)
driver.find_element(By.ID, "tool-2").click()

# Submit the form
driver.find_element(By.ID, "submit").click()

# Pause to see the result
time.sleep(10)

# Close the browser
driver.quit()
