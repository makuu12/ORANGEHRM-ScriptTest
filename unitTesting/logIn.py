from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login: # Select all modules from the sidebar menu

    # -------------- Usage -------------- #
    # from unitTesting import logIn
    # 
    # l = logIn.login()
    # l.setup()
    # l.login()
    # -------------- Usage -------------- #
    
    def __init__(self):
        self.driver = None
    
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Setup initialized...")

    def login(self):
        time.sleep(5)
        username = "Admin"
        password = "admin123"
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Login Successful")
        