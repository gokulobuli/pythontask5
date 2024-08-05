from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (Chrome in this case)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the URL
    driver.get('https://jqueryui.com/droppable/')

    # Switch to the iframe where the draggable and droppable elements are located
    iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
    driver.switch_to.frame(iframe)

    # Locate the draggable and droppable elements
    draggable = driver.find_element(By.ID, 'draggable')
    droppable = driver.find_element(By.ID, 'droppable')

    # Perform drag and drop operation
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()

    print("Drag and drop operation completed.")

finally:
    # Ensure the WebDriver quits
    driver.quit()
