from selenium import webdriver
from time import sleep
import import_email
#driver = webdriver.Firefox()
#driver.implicitly_wait(10)
#def has_connection(driver):
#    try:
#        driver.find_element_by_xpath('//body[@class="neterror"]')
#        return True
#    except:
#        return False
        
prevnum=import_email.n
print(prevnum)
num=0
url= open("/home/tarunsparrot/tarun_urlnohtml.txt",'r') 
url_rpt = url.read().split()
print(url_rpt)
opt = webdriver.FirefoxOptions()
opt.set_preference('dom.popup_maximum', 90)
driver = webdriver.Firefox(options=opt)
#driver.implicitly_wait(10)
for link in url_rpt:
    print(link)
    num=num+1
    # Open a new window
    #driver.switch_to.new_window('tab')
    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[num])
    driver.get(link)
    timer = driver.find_element_by_id('timerDiv')
    print(timer)
    print(num)
    sleep(35)
    #status = driver.find_element_by_id("StatusImage")
    #while len(driver.find_element_by_id("StatusImage")) == 0:
    #    sleep(50)

    #if has_connection(driver)==True:
    #    print('no internet')
    #   sleep(10)
    #while len(status) != 0:
    #    sleep(10)

print(num)
