# Required Libraries

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Setup Driver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#Handle Scrollbar
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#Click on Element Options
driver.find_element(By.XPATH,"//div[@class= 'card-up']").click()

#----------------------------------------CLick on Text Box-------------------------------------------------
driver.find_element(By.XPATH, "//a[@href='/text-box']").click()

time.sleep(5)

#Locating Text Box
driver.find_element(By.ID,"userName").send_keys("Test User")
driver.find_element(By.XPATH,"//input[@type = 'email']").send_keys("test@test.com")
driver.find_element(By.ID,"currentAddress").send_keys("123 Main Street, City")
driver.find_element(By.ID,"permanentAddress").send_keys("456 Elm Street, City")
driver.find_element(By.ID,"submit").click()

#Print the information
TexBox= driver.find_element(By.XPATH,"//div[@class='border col-md-12 col-sm-12']").text
print(TexBox)
time.sleep(5)
# driver.quit()

#-------------------------------#Click on Radio Button---------------------------------------------------
driver.find_element(By.XPATH,"//a[@href='/radio-button']").click()

#Locating Radio Button
#driver.find_element(By.XPATH,"//input[@id='yesRadio']").click()
driver.find_element(By.ID, "impressiveRadio").click()

# message= driver.find_element(By.XPATH,"//p[@class='mt-3']").text
# print(message)
message1= driver.find_element(By.XPATH,"//p[@class='mt-3']").text
print(message1)
time.sleep(5)

#-----------------------------------------------Buttons-----------------------------------------------------
#Navigate to the Buttons page
driver.find_element(By.XPATH,"//a[@href='/buttons']").click()
time.sleep(3)

actions = ActionChains(driver)

#Locate the double-click button
dub_Btn = driver.find_element(By.ID, "doubleClickBtn")
right_Click = driver.find_element(By.ID, "rightClickBtn")
click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']").click()

#perform click
actions.double_click(dub_Btn).perform()
actions.context_click(right_Click).perform()

#print the message
doubt_Click = driver.find_element(By.ID, "doubleClickMessage").text
Right_Click = driver.find_element(By.ID, "rightClickMessage").text
click_msg = driver.find_element(By.ID, "dynamicClickMessage").text
print(doubt_Click)
print(Right_Click)
print(click_msg)
time.sleep(5)
#--------------------------------------Alert_Handle-------------------------------------------------------
#click on Element option
#driver.find_element(By.XPATH,"//div[@class= 'card-up']").click()

#Handle scrollbar
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#click on Alert,frame & window option
driver.find_element(By.XPATH, "//div[contains(@class,'header-text') and contains(.,'Alerts, Frame')]").click()

#click on the alerts option
driver.find_element(By.XPATH, "//div[contains(@class,'element-list')]//span[text()='Alerts']").click()
#----------------------------------------Handle simple alerts----------------------------------------------------

driver.find_element(By.ID,"alertButton").click()
time.sleep(3)
#switch focus to alert pop up
alert= driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()
time.sleep(5)
#-----------------------------------Confirm Alert--------------------------------------------------------
driver.find_element(By.ID,"confirmButton").click()
time.sleep(3)

#switch focus to alert pop up
confirm_alert = driver.switch_to.alert
print("Confirm Alert:", confirm_alert.text)
#confirm_alert.accept()
confirm_alert.dismiss()

#Print the message
#result = driver.find_element(By.ID, "confirmResult").text
result_1 = driver.find_element(By.ID, "confirmResult").text
print(result_1)

time.sleep(5)

#-------------------------------------------Prompt Alert--------------------------------------
driver.find_element(By.ID,"promtButton").click()

prompt_alert= driver.switch_to.alert
print("Confirm Alert:", prompt_alert.text)
time.sleep(4)
#Enter Text
#prompt_alert.send_keys("Hello World")
#prompt_alert.accept()
prompt_alert.dismiss()


#Print the message
# result = driver.find_element(By.ID, "promptResult").text
# print(result)
print("You click on cancel")
time.sleep(2)
