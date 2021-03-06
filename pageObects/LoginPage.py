
class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_class = "//button[@type='submit']"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_class).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linkText).click()
