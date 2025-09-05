from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 🛠️ SETUP SELENIUM
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 🖥️ Open the Result Page
driver.get("https://exam.bujhansi.ac.in/frmViewCampusCurrentResult.aspx")
time.sleep(3)  # Wait for page load

try:
    # 🎯 Select "Main" in Result Type
    result_type_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlResultType"))
    )
    Select(result_type_dropdown).select_by_visible_text("Main")
    time.sleep(2)  # Small delay

    # 🎯 Select Course
    course_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlCourse"))
    )
    
    # # 🔍 Print Available Courses
    # options = [opt.text for opt in Select(course_dropdown).options]
    # print(f"Available Courses: {options}")

    Select(course_dropdown).select_by_visible_text("B.C.A. (Hons.) I Semester")
    print("✅ Selected Result Type & Course")

except Exception as e:
    print(f"❌ Error selecting dropdowns: {e}")
    driver.quit()
    exit()
    

