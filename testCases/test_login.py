from pageObects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login(BaseClass):

    log = LogGen.getLogger()
    log.info("*************** Test_001_Login Started******************")
    log.info("******Collecting data from config.ini file")
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    log.info("******Data from config.ini file collected")

# Test for verifying the title of login screen
    def test_login_page_title(self):
        self.log.info("**********Starting test_login_page_title *************")
        self.log.info("*****Got Driver Object assigning task to driver object started")
        self.driver.get(self.baseURL)
        login_page_title = self.driver.title
        if login_page_title == "Your store. Login":
            self.log.info("***Title of the login page  validated******")
            assert True
            self.driver.close()
        else:
            self.log.error("*****Title of the login page not correct*******")
            self.driver.save_screenshot(".\\Screenshots\\test_login_page_title.png")
            self.driver.close()
            self.log.info("**********test_login_page_title Ended With Error*************")
            assert False
        self.log.info("************Completed test_login_page_title**************")

    def test_login(self):
        self.log.info("**********test_login Started*************")
        self.log.info("*****Got Driver Object assigning task to driver object strated")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        homepage_title = self.driver.title
        if homepage_title == "Dashboard / nopCommerce administration":
            self.log.info("*****Log in successful******")
            assert True
            self.driver.close()
        else:
            self.log.error("*****Log in not successful******")
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.log.info("**********test_login_page_title Ended With Error*************")
            assert False
