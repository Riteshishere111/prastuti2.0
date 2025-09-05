import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Open Chrome and target page
driver = webdriver.Chrome()
driver.get("https://exam.bujhansi.ac.in/frmViewCampusCurrentResult.aspx")

# Find the roll number input field
roll_number = driver.find_element(By.NAME, "txtUniqueID")
roll_number.send_keys("241341133143")

# Find and select the course
course = driver.find_element(By.NAME, "ddlCourse")
select = Select(course)
select.select_by_visible_text("B.C.A. (Hons.) I Semester")  # Change this to match the actual option

#Find and select 
Result_type= driver.find_element(By.NAME, "ddlResultType")
select = Select(Result_type)
select.select_by_visible_text("Main")

#Find and select Submit 
submit=driver.find_element(By.NAME, "btnGetResult")
submit.click()

# NOTE EVERYTHING ABOVE WORKS FINE

# Getting Result Data
data = {
    "roll_number":driver.find_element(By.ID, "lblRollNo").text,
    "enroll_number" : driver.find_element(By.ID, "lblenrollNo").text,
    "student_name" : driver.find_element(By.ID, "lblCandidateName").text,
    "father_name" : driver.find_element(By.ID, "lblFatherName").text,
    "mother_name" : driver.find_element(By.ID, "lblMotherName").text
}

df = pd.DataFrame([data])
df.to_excel("Students_result.xlsx", index = True)



time.sleep(10)

driver.close()

print("Data saved to student_result.xlsx successfully!")