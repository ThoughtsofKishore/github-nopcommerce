from pageObects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils


class Test_002_DDT_Login(BaseClass):

    log = LogGen.getLogger()
    log.info("*************** Test_002_DDT_Login******************")
    log.info("******Collecting data from config.ini file")
    baseURL = ReadConfig.getURL()
    path = ".\\TestData\\LoginData.xlsx"

# DDT Test for Login Screen

    def test_login_DDT(self):
        self.log.info("**********test_login Started*************")
        self.log.info("*****Got Driver Object assigning task to driver object strated")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(file=self.path, sheetName="Sheet1")
        self.columns = ExcelUtils.getColumnCount(file=self.path, sheetName="Sheet1")

        lst_status = []
        for r in range(2, self.rows+1):
            self.user = ExcelUtils.readData(file=self.path, sheetName="Sheet1", rownum=r, columnnum=1)
            self.password = ExcelUtils.readData(file=self.path, sheetName="Sheet1", rownum=r, columnnum=2)
            self.exp = ExcelUtils.readData(file=self.path, sheetName="Sheet1", rownum=r, columnnum=3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.log.info("****Pass*****")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.log.info("******Fail*****")
                    self.lp.clickLogout()
                    lst_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.log.info("*****Fail******")
                    self.lp.clickLogout()
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.log.info("*****Pass*******")

        if "fail" not in lst_status:
            self.log.info("Login DDT test passed...")
            self.driver.close()
            assert True
        else:
            self.log.error("Login DDT test failed")
            self.driver.close()
            assert False

        self.log.info("*****End of the DDT Login Test***********")
        self.log.info("******Completed  test_login_DDT********* ")
