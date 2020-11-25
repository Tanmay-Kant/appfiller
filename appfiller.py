from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#Author: Tanmay Kant
#For all jobs.lever.co applications

websiteInput = input('Enter website to autofill internship application: ')
chromedriver_location = "/Users/tanmay/projects/appfiller/chromedriver"
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")
driver = webdriver.Chrome(chromedriver_location)
driver.get(websiteInput)
time.sleep(5)


driver.find_element_by_id("resume-upload-input").send_keys("/Users/tanmay/projects/appfiller/resume-2020.pdf")
time.sleep(5)

input_field = driver.find_element_by_xpath("//input[@name='org']")
driver.execute_script("arguments[0].value = ''", input_field)
input_field.send_keys('Computer Engineering Student at UIUC')

input_field = driver.find_element_by_xpath("//input[@name='phone']")
driver.execute_script("arguments[0].value = ''", input_field)
input_field.send_keys('4088056437')

input_field = driver.find_element_by_xpath("//input[@name='urls[LinkedIn]']")
driver.execute_script("arguments[0].value = ''", input_field)
input_field.send_keys('https://www.linkedin.com/in/tanmay-kant/')
githubPresent = False
try: git_input_field = driver.find_element_by_xpath("//input[@name='urls[GitHub]']")
except Exception:
    pass
else:
    githubPresent = True
try: driver.execute_script("arguments[0].value = ''", git_input_field)
except Exception:
    pass
try: git_input_field.send_keys('https://github.com/Tanmay-Kant')
except Exception:
    pass
if githubPresent == False:
    try: port_input_field = driver.find_element_by_xpath("//input[@name='urls[Portfolio]']")
    except Exception:
        pass
    try: driver.execute_script("arguments[0].value = ''", port_input_field)
    except Exception:
        pass
    try: port_input_field.send_keys('https://github.com/Tanmay-Kant')
    except Exception:
        pass

try: select = Select(driver.find_element_by_xpath("//select[@name='eeo[gender]']"))
except Exception:
    pass
try: select.select_by_visible_text('Male')
except Exception:
    pass
    
try: select = Select(driver.find_element_by_xpath("//select[@name='eeo[race]']"))
except Exception:
    pass
try: select.select_by_visible_text('Asian (Not Hispanic or Latino)')
except Exception:
    pass

try: select = Select(driver.find_element_by_xpath("//select[@name='eeo[veteran]']"))
except Exception:
    pass
try: select.select_by_visible_text('I am not a veteran')
except Exception:
    pass
try: select.select_by_visible_text('I am not a protected veteran')
except Exception:
    pass

try: select = Select(driver.find_element_by_xpath("//select[@name='eeo[disability]']"))
except Exception:
    pass
try: select.select_by_visible_text("No, I don't have a disability, or a history/record of having a disability")
except Exception:
    pass


    
input_field = driver.find_element_by_xpath("//textarea[@name='comments']")
driver.execute_script("arguments[0].value = ''", input_field)
input_field.send_keys('This application was auto-filled by a Selenium Python Script.')

try: docUploadButton =  driver.find_element_by_xpath("//button[@data-automation-id='label']")
except Exception:
    pass

try: docUploadButton
except NameError: pass
else:
    if docUploadButton.is_displayed() == True:
        docUploadButton.click()
        print("Made it through test case 1")
        
time.sleep(10)

print("Made it through test case 2")
