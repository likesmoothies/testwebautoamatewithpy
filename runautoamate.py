import Facotry.PageFactory
from Facotry.DriveFactory import  Driver_Factory
from Config import Config

driveObj = Driver_Factory.Get_Web_Driver("chrome")
ConfigObj = Config()

testObj = driveObj.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
testObj = Facotry.PageFactory.PageObject("Dashboard",driveObj)
testObj.start()
testObj = driveObj.quit()