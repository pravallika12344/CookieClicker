from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

chrome_driver_path = r"C:\Users\pathi\Videos\Documents\Desktop\projects\chromedriver.exe"

# Cookie Clicker URL
url = "https://orteil.dashnet.org/cookieclicker/"

options = webdriver.ChromeOptions()
# Add any additional options you need, such as headless mode or proxy settings

service = Service(chrome_driver_path)
service.start()

driver = webdriver.Chrome(service=service, options=options)

# Open the "Cookie Clicker" game
driver.get(url)

# Wait for the loader to disappear

# Check if the "big cookie" button is visible before clicking
cookie = driver.find_element(By.Id,"BigCookie")

# Scroll into view (optional, if needed)
driver.execute_script("arguments[0].scrollIntoView();", cookie)

# Perform the click using JavaScript
driver.execute_script("arguments[0].click();", cookie)



# Perform additional interactions with the game if needed

# Quit the WebDriver session (close the browser)
driver.quit()
