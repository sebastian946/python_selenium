from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Ejecutar reporte behave -f allure_behave.formatter:AllureFormatter -o "report" features/reports

driver = webdriver.Chrome()
typeLocators = {
    "name" : By.NAME,
    "classname" : By.CLASS_NAME,
    "xpath": By.XPATH,
    "id": By.ID,
    "linktext": By.LINK_TEXT
}
@staticmethod
def openBrowser(url):
    try:
        driver.maximize_window()
        driver.get(url)
    except Exception as e:
        print("Error occurred while opening the browser: ", e)
        
@staticmethod
def wait_element_clickable(type_location,location):
    wait = WebDriverWait(driver,10)
    return wait.until(EC.visibility_of_element_located((type_location,location)))
        
@staticmethod
def click_element(type_locator,location):
    try:
        type_location = typeLocators.get(type_locator.lower())
        wait_element_clickable(type_location,location)
        driver.find_element(type_location,location).click()
    except NoSuchElementException:
        print("Element not found: ", location)
    
@staticmethod
def send_keys_element(type_locator, location, string_key):
    try:
        type_location = typeLocators.get(type_locator.lower())
        driver.find_element(type_location,location).send_keys(string_key)
    except NoSuchElementException:
        print("Element not found: ", location)

@staticmethod
def assert_text_element(type_locator, location, compare_text):
    try:
        type_location = typeLocators.get(type_locator.lower())
        text_element = driver.find_element(type_location,location).text
        return text_element == compare_text
    except NoSuchElementException:
        print("Element not found: ", location)
        return False
        

@staticmethod
def close_browser():
    try:
        driver.quit()
    except Exception as e:
        print("Error occurred while closing the browser: ", e)

