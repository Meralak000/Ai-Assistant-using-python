from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class info:
    def __init__(self):
        chrome_path = Service(executable_path = 'chromedriver.exe')
        self.driver = webdriver.chrome(Service=chrome_path )
        
    def getInfo(self,query):
        self.query = query
        self.driver.get(url = 'https://wikipedia.org')
assist = info()        
assist.getInfo("hello")