from lib2to3.pgen2 import driver
from zoneinfo import available_timezones
from selenium import webdriver
import time
from itertools import product
from string import ascii_lowercase
import pandas as pd
from pandasgui import show
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://transact3.dmv.ny.gov/PlatesPersonalized/") #go to website
time.sleep(10)

#sets up buttons to click
passenger_button = driver.find_element(id, "passenger")
time.sleep(3)
passenger_button.click() 
plate_num_box = driver.find_element(id, "txtPlateNum")
continue_button = driver.find_element(By.NAME, "btnSubmit")



#All possible 3 letter combos
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]    

#True for unavailable
result = driver.findElement(By.XPATH("/html/body/div[1]/div[5]/div/div/div[3]")).isDisplayed() 

#Initialize lists
available = []
unavailable = [] 

#loop through each combo, add combos that don't work to unavailable, vice versa
time.sleep(5)
for combo in keywords: 
    plate_num_box.send_keys(combo)
    time.sleep(5)
    continue_button.click()
    if result == True:
        unavailable.append(combo)
    else:
        available.append(combo)
    time.sleep(5)
    driver.back

#initialize dict to be converted to df
table = {
    'Combos': keywords,
    'Available': available,
    'Unavailable': unavailable
}

#dataframe, df to gui, gui that includes df
df = pd.DataFrame(table)
gui = show(table)
data = gui.get_dataframes()

#Results
time.sleep(5)
print(data.keys())
print(data["df"])


driver.close()





