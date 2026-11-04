from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

try:

    file_path = Path("login.html").resolve().as_uri()

    driver.get(file_path)

    # Enter valid credentials
    driver.find_element(
        By.ID, "username"
    ).send_keys("admin")

    driver.find_element(
        By.ID, "password"
    ).send_keys("admin123")

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Verify successful login
    success_message = wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"),
            "Login successful"
        )
    )

    assert success_message

    print("Valid login test passed")

    # Clear the fields
    driver.find_element(
        By.ID, "username"
    ).clear()

    driver.find_element(
        By.ID, "password"
    ).clear()

    # Enter invalid credentials
    driver.find_element(
        By.ID, "username"
    ).send_keys("wronguser")

    driver.find_element(
        By.ID, "password"
    ).send_keys("wrongpass")

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Verify error message
    error_message = wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"),
            "Invalid username or password"
        )
    )

    assert error_message

    print("Invalid login test passed")

finally:

    driver.quit()