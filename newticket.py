from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import date
import time

driver = webdriver.Ie('C:\IEDriverServer')
driver.get('') #omitting URL for security reasons



LeftBar = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="WIN_0_304316340"]/div[1]'))
)

IncidentManagement = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="WIN_0_80098"]/div/div/div[2]/fieldset/div/div/div/div[10]/a/span'))
)


NewIncident = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="WIN_0_80098"]/div/div/div[2]/fieldset/div/div/div/div[10]/div[1]/div[2]/a/span'))
)

LeftBar.click()
IncidentManagement.click()
NewIncident.click()


CustomerField = driver.find_element_by_xpath('//div[@id="WIN_3_303530000"]/textarea')
CustomerField.click()
driver.execute_script('document.getElementById("arid_WIN_3_303530000").value="bijmoh";') #using JS to send text as sendkeys() method too slow
CustomerField.send_keys(Keys.ENTER)

ContactField = driver.find_element_by_id('arid_WIN_3_303497600')
driver.execute_script('document.getElementById("arid_WIN_3_303497600").value="bijmoh";')
ContactField.send_keys(Keys.ENTER)


NotesField = driver.find_element_by_id('arid_WIN_3_1000000151')
driver.execute_script("""var today = new Date();
var date = today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear()+'testnotes';
document.getElementById("arid_WIN_3_1000000151").value=date;""")

SummaryField = driver.find_element_by_id('arid_WIN_3_1000000000')
SummaryField.click()
driver.execute_script('document.getElementById("arid_WIN_4_1000000000").value="TestSummary";')
