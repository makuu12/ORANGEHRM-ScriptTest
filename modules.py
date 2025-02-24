from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

class loginpage_modules:
    
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username="Admin", password="admin123"):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        # screenshot_path = self.take_screenshot(driver , folder_path = "ORANGEHRM-ScriptTest\Screenshots", file_name="001 Login.png")
        self.driver.find_element(By.CLASS_NAME, "oxd-button--main").click()
        time.sleep(10)   

class clickmodule:
    def __init__(self, driver):
        self.driver = driver
        
    def click_admin(self):
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Admin"]').click() 
        time.sleep(5)
        
    def click_pim(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        time.sleep(5)
        
    def click_leave(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
        time.sleep(5)
        
    def click_time(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
        time.sleep(5)
        
    def click_recruitment(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
        time.sleep(5)
        
    def click_myInfo(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
        time.sleep(5)
        
    def click_performance(self):
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
        time.sleep(5)
        
class moduleTabs:
    
    def __init__(self, driver):
        self.driver = driver
        
    def admin(self):
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Admin"]').click() 
        time.sleep(5)
        
    def pim(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="PIM"]').click()
        time.sleep(2)
        
    def leave(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Leave"]').click()
        time.sleep(2)
    def time(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="time"]').click()
        time.sleep(2)
        
    def recruitment(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Recruitment"]').click()
        time.sleep(2)
        
    def myInfo(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="My Info"]').click()
        time.sleep(2)
        
    def performance(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Performance"]').click()
        time.sleep(2)
        
    def dashboard(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Dashboard"]').click()
        time.sleep(2)
        
    def Directory(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Directory"]').click()
        time.sleep(2)
        
    def claim(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Claim"]').click()
        time.sleep(2)
        
    def buzz(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Buzz"]').click()
        time.sleep(2)
        
    def performance(self): 
        self.driver.find_element(By.XPATH, '//a[normalize-space()="Performance"]').click()
        time.sleep(2)
        
class func:
    
    def __init__(self, driver):
        self.driver = driver
        
    def addEmployee(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(5)

        self.driver.find_element(By.NAME, "firstName").send_keys("fname")
        self.driver.find_element(By.NAME, "middleName").send_keys("mname")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("lname")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("121222")

        elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-switch-input.oxd-switch-input--active.--label-right"))
        )
        self.driver.execute_script("arguments[0].click();", elem)

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys("username")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys("password123")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys("password123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
        time.sleep(5)
        

    def add_personalDetails(self): # Personal Details/Personal Details
        # Select an item from the table
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]'))
        # )
        # print("table found")
        # first_row = self.driver.find_element(By.XPATH, "(//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable'])[1]")
        # first_row.click()

        # PERSONAL DETAILS
        # Full name
        
        # Use this if you want to replace shitty strings
        # firstname.send_keys(Keys.CONTROL + "a") 
        # firstname.send_keys(Keys.BACKSPACE)
        
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstName").send_keys("first")
        self.driver.find_element(By.NAME, "middleName").send_keys("mid")
        self.driver.find_element(By.NAME, "lastName").send_keys("last")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("23453") # ID
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys("23453") # Other ID (Optional)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("23453") # Driver's license no (Optional)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2025-12-12") # license Expiry Date
        try: # Nationality
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Australian").click()

        except Exception as e:
            print(f"An error occurred: {e}")
            
        try: # Marital Status
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[1].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Single").click()

        except Exception as e:
            print(f"An error occurred: {e}")
        
        mGender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        fGender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label'
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("2000-12-12")
        self.driver.find_element(By.XPATH, mGender).click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click() # Save button 1

    def add_customFields(self): # Personal Details/Custom Fields
        try: # Blood Type
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[2].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "B+").click()

        except Exception as e:
            print(f"An error occurred: {e}")
        
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[2]/input').send_keys("test") # Test Field
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button').click() # Save button 2
    def add_pdAttachment(self): # Personal Details/Attachment
        # Will add some next time
        print("Hello world") 
        
    def add_contactDetails(self):
        # Address
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("Street 1")
        self.driver.find_element(By.XPATH, '<input data-v-1f99f73c="" class="oxd-input oxd-input--active">').send_keys("Street 2")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys("City")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input').send_keys("State/Provice")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys("1111")
        try: # Country
            dropdown = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']")
            dropdown[0].click()
            options_xpath = "//div[@role='option']"
            options = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, options_xpath))
            )
            next(option for option in options if option.text.strip() == "Algeria").click()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Telephone
        time.sleep(3)
        self.driver.find_element(By.XPATH, '<input data-v-1f99f73c="" class="oxd-input oxd-input--active" modelmodifiers="[object Object]">').send_keys("Home")
        self.driver.find_element(By.XPATH, '').send_keys("12345678") # Mobile
        self.driver.find_element(By.XPATH, '').send_keys("12345678") # Work
        
        # Email
        time.sleep(3)
        self.driver.find_element(By.XPATH, '').send_keys("sad@das.xyz") # Email
        self.driver.find_element(By.XPATH, '').send_keys("sad@gmail.com") # Other Email
        
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click() # Save button
        
        # Attachment
    
    
    def add_emergencyContacts(self):
        print("world")



# NOTESSSSS
# KENAT BYPASS THE LEAVE MODULE

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveModule")
# time.sleep(5)


# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a').click()
# time.sleep(5)
# # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/input').send_keys("m", Keys.ARROW_DOWN, Keys.ENTER)
# # time.sleep(5)

# dropdown_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div')
# dropdown_element.send_keys('M')
# select = Select(dropdown_element)
# select.select_by_index(0)
# time.sleep(5)
# dropdown_element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div')
# select = Select(dropdown_element)
# select.select_by_visible_text("Option Text")
# time.sleep(5)
# leave_period = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div')
# select = Select(leave_period)
# select.select_by_visible_text("2026-01-01 - 2026-31-12")

# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/input')
# # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[1]') # Cancel button
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]') # Save button

