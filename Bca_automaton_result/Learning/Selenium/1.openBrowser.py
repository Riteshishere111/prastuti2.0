from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set path to chromeDriver
driver_path = "C:\\Windows\\chromedriver.exe"

# Creating a service instance
service = Service(driver_path)

# Start Chrome Using Service
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Close the browser
driver.quit()
