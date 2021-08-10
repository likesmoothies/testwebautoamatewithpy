from Page import WebPage


class Dashboards(WebPage):
    def __init__(self,driver):
        super().__init__(driver)
        self.title = 'h1'
        self.buttonlogin = "//button[contains(text(),'Log in')]"

    def start (self):
        self.VerifyDashboard()


    def VerifyDashboard(self):
        self.driver.find_element('xpath',self.buttonlogin).click()
        self.wait('time',10)
#        self.
        self.isElementExist('xpath', self.title)
        print("success")

