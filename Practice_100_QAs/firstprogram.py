
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("http://www.facebook.com")
print("Aplication title is ",driver.title)
print("Aplication url is ",driver.current_url)
driver.quit()
