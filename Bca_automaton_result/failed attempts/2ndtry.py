from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# 🛠️ SETUP SELENIUM
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 🖥️ Open the Result Page
driver.get("https://exam.bujhansi.ac.in/frmViewCampusCurrentResult.aspx")

# 🏫 Wait for "Result Type" dropdown and select "Main"
try:
    result_type_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlResultType"))
    )
    Select(result_type_dropdown).select_by_visible_text("Main")

    # 📚 Select "B.C.A. Hons" from "Course"
    course_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlCourse"))
    )
    Select(course_dropdown).select_by_visible_text("B.C.A. (Hons.) I Semester")

    print("✅ Selected Result Type & Course")

except Exception as e:
    print(f"❌ Error selecting dropdowns: {e}")
    driver.quit()
    exit()

# 📄 List of Roll Numbers to Check
roll_numbers = ["241341133138", "241341133139", "241341133140"]  # Replace with real roll numbers
results = []

# 🔄 Loop Through Each Roll Number
for roll_no in roll_numbers:
    print(f"🔍 Fetching result for Roll No: {roll_no}")

    try:
        # 📝 Wait for Roll Number input field
        roll_no_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtRollNo"))
        )
        roll_no_input.clear()
        roll_no_input.send_keys(roll_no)

        # ✅ Click Submit
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "btnSubmit"))
        )
        submit_button.click()

        # ⏳ Wait for result to load
        time.sleep(3)

        # 📊 Extract Student Name & Marks
        try:
            student_name = driver.find_element(By.ID, "lblStudentName").text
            marks = driver.find_element(By.ID, "lblMarks").text
            results.append([roll_no, student_name, marks])
            print(f"✅ {student_name}: {marks}")
        except:
            print(f"⚠️ No result found for Roll No: {roll_no}")
            results.append([roll_no, "Not Found", "Not Found"])

    except Exception as e:
        print(f"❌ Error fetching result for {roll_no}: {e}")

    time.sleep(1)  # Small delay before next roll number

# 💾 Save Results to Excel
df = pd.DataFrame(results, columns=["Roll No", "Student Name", "Marks"])
df.to_excel("BCA_Results.xlsx", index=False)

print("\n✅ All results saved to **BCA_Results.xlsx**")
driver.quit()
