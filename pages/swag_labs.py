
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):

    def exist_icon(self, locator):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def field_name(self, locator):
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def field_password(self, locator):
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True

