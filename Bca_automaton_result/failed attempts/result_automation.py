from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


#Setup Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Open the Result Page
driver.get("https://exam.bujhansi.ac.in/frmViewCampusCurrentResult.aspx")

#Select "Main" from "Result Type"
Select(driver.find_element(By.ID, "ddlResultType")).select_by_visible_text("Main")

#Select "B.C.A Hons" from "Course"
Select(driver.find_element(By.ID, "ddlCourse")).select_by_visible_text("B.C.A. (Hons.) I Semester")

#List of Roll Numbers to Check
roll_numbers = ["241341133138", "241341133143", "241341133154"] #Add real roll numbers here 
results= []

#Loop Through Each Roll number
for roll_no in roll_numbers:
    print(f"Fetching result for Roll No: {roll_no}")

    #Enter Roll Number
    roll_no_input = driver.find_element(By.ID, "txtRollNo")
    roll_no_input.clear()
    roll_no_input.send_keys(roll_no)

    #Click Submit
    driver.find_element(By.ID, "btnSubmit").click()
    time.sleep(2)   #wait for the result to load

    #Extract Student Name & Result

    try:
        student_name = driver.find_element(By.ID, "lblStudentName").text
        marks = driver.find_element(By.ID, "lblMarks").text
        results.append([roll_no, student_name, marks])
    except:
        print(f"No result found for Roll No: {roll_no}")
        results.append([roll_no, "Not Found", "Not Found"])

        time.sleep(1)
    
    # Save Results to Excel
    df = pd.DataFrame(results, column=["Roll No", "Student Name", "Marks"])
    df.to_excel("BCA_Results.xlsx", index=False)

    print("Results saved to BCA_Results.xlsx")
    driver.quit()
