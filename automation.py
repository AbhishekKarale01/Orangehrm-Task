from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import logging
import time
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def automate_orangehrm(
        username,
        password,
        first_name,
        last_name,
        employee_id):

    driver = None

    result = {
        "status": False,
        "message": "",
        "employee": {},
        "employee_list": []
    }

    try:

        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)

        wait = WebDriverWait(driver, 20)

        driver.get(URL)

        logging.info("Website opened")

        # LOGIN

        wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "username")
            )
        ).send_keys(username)

        driver.find_element(
            By.NAME,
            "password"
        ).send_keys(password)

        driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        logging.info("Login successful")

        # PIM

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        ).click()

        logging.info("PIM opened")

        # ADD EMPLOYEE

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(.,'Add Employee')]")
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "firstName")
            )
        ).send_keys(first_name)

        driver.find_element(
            By.NAME,
            "lastName"
        ).send_keys(last_name)

        emp_id_input = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "(//input[contains(@class,'oxd-input')])[5]"
                )
            )
        )

        emp_id_input.clear()
        emp_id_input.send_keys(employee_id)

        driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        logging.info("Employee added")

        time.sleep(3)

        result["employee"] = {
            "first_name": first_name,
            "last_name": last_name,
            "employee_id": employee_id
        }

        # EMPLOYEE LIST

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(.,'Employee List')]"
                )
            )
        ).click()

        time.sleep(3)

        rows = driver.find_elements(
            By.XPATH,
            "//div[@role='row']"
        )

        employee_data = []

        for row in rows[1:]:

            try:

                cols = row.find_elements(
                    By.XPATH,
                    ".//div[@role='cell']"
                )

                if len(cols) >= 3:

                    emp = {
                        "employee_id": cols[1].text,
                        "name": cols[2].text
                    }

                    employee_data.append(emp)

            except:
                pass

        result["employee_list"] = employee_data

        # EXPORT

        pd.DataFrame(employee_data).to_excel(
            "employee_list.xlsx",
            index=False
        )

        logging.info("Excel exported")

        # LOGOUT

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.CLASS_NAME,
                    "oxd-userdropdown-tab"
                )
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[text()='Logout']"
                )
            )
        ).click()

        logging.info("Logout successful")

        result["status"] = True
        result["message"] = "Automation completed successfully"

        return result

    except Exception as e:

        logging.exception(e)

        result["message"] = str(e)

        return result

    finally:

        if driver:
            driver.quit()