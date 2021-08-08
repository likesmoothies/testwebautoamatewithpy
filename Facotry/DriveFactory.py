from selenium import webdriver


class Driver_Factory:

    def __init__(self):
        pass

    def Get_Web_Driver(self,drivers="chrome"):
        if drivers == "firefox":
            return webdriver.Firefox()
        else :
            return webdriver.Chrome()


