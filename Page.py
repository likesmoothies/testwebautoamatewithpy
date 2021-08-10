import logging
import Config
import time
class WebPage():
    def __init__(self, driver, conf=None):
        "CONFIG"
        if conf == None:
            conf = Config.Config()
        self.driver = driver
        self.conf = conf

    def getText(self, by, name, idx=0):
        '''Get text by 'by' and name 'name'
        Parameters:
        -----------
        by: str
            Mechanism used to locate elements within a screen/document.
            'id', 'class name', 'name', tag name', 'xpath', 'partial link text'
        name: str
            Name of element to be found
        idx: int (optional, default = 0)
            Return idx-th text if there are multiple elements with same name. Set idx to -1 to return a list of text.

        Example:
        -----------
        getText('id', 'com.samsung.android.rajaampat:id/title')
            get first text from element with id = com.samsung.android.rajaampat:id/title, return in string
        getText('class name', 'android.widget.TextView')
            get first text from element with class name = android.widget.TextView, return in string
        getText('class name', 'android.widget.TextView', -1)
            get all texts that have android.widget.TextView as their class name, return in array
        return empty array [] if not found
        '''
        # IF IDX = -1  then return as array
        if idx == -1:
            return [individualElement.text for individualElement in self.driver.find_elements(by, name)]
        else:
            # IF IDX != -1, then return single item
            # By default, first item will be returned
            return self.driver.find_elements(by, name)[idx].text

    def isElementExist(self, by, name):
        '''To check whether an element is exist. Return True if exist, return False if otherwise

        Parameters:
        -----------
        by: str
            Mechanism used to locate elements within a screen/document.
        name: str
            Name of element to be found
        '''
        if self.driver.find_elements(by, name):
            return True
        else:
            return False

    def clear(self, by, name):
        '''To clear a textfield

        Parameters:
        -----------
        by: str
            Mechanism used to locate elements within a screen/document.
        name: str
            Name of element to be found
        '''
        try:
            self.driver.find_element(by, name).clear()
        except Exception as e:
            logging.error("Failed to clear %s by %s. %s" % (name, by, e))

    def wait(self, type, name):
        '''
        Performs wait, depends on type Supported type: time, element type

        Parameters:
        -----------
        type: str
            wait method: 'time', By
        name: str/int

        Example:
        -----------
        wait('time', timeInSecond)
            wait for timeInSeconds
        wait(by, elementName)
            wait until element is shown (by id, by class name)
        '''
        if type == 'time':
            time.sleep(name)
        else:
            while not self.driver.find_elements(type, name):
                time.sleep(1)