import pytest
from selenium import webdriver
from utilities.customLogger import LogGen

log = LogGen.getLogger()


def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome")


@pytest.fixture()
def setupBrowser(request):

    browserName = request.config.getoption("--browsername")

    if browserName == "chrome":
        log.info("*****Calling Chrome Browser From conftest file*******")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    elif browserName == "firefox":
        log.info("*****Calling Firefox Browser From conftest file*******")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    elif browserName == "IE":
        log.info("*****Calling IE Browser From conftest file*******")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    request.cls.driver = driver
    log.info("****Sending driver object from conftest to test file******")
