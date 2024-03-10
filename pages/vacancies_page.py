from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from locators.vacancies_locators import VacanciesLocators
from utils.base_class import BaseClass


class VacanciesPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def select_department(self, department):
        log = self.get_logger()
        default_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        log.info("Default department displayed on the page: " + default_department.text + ".")
        if default_department.text != department:
            default_department.click()
            log.info("Department button dropdown clicked.")
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]').click()
        selected_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        log.info("Selected department: " + selected_department.text + ".")
        assert department == selected_department.text, "Selected department doesn't match the expected."

    def select_country(self, country):
        log = self.get_logger()
        default_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        log.info("Default country displayed on the page: " + default_country.text + ".")
        if default_country.text != country:
            default_country.click()
            log.info("Country button dropdown clicked.")
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]').click()
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        log.info("Selected country: " + selected_country.text + ".")
        assert country == selected_country.text, "Selected country doesn't match the expected."

    def select_state(self, state):
        log = self.get_logger()
        default_state = self.driver.find_element(*VacanciesLocators.STATE)
        log.info("Default state displayed on the page: " + default_state.text + ".")
        if default_state.text != state:
            default_state.click()
            log.info("State button dropdown clicked.")
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]').click()
        selected_state = self.driver.find_element(*VacanciesLocators.STATE)
        log.info("Selected state: " + selected_state.text + ".")
        assert state == selected_state.text,  "Selected state doesn't match the expected."

    def select_city(self, city):
        log = self.get_logger()
        default_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        # Workaround to select a city within a state in USA
        if default_country.text == "USA":
            default_city = self.driver.find_element(*VacanciesLocators.CITY_USA)
        else:
            default_city = self.driver.find_element(*VacanciesLocators.CITY)
        log.info("Default city displayed on the page: " + default_city.text + ".")
        if default_city.text != city:
            default_city.click()
            log.info("City button dropdown clicked.")
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]').click()
        if default_country.text == "USA":
            selected_city = self.driver.find_element(*VacanciesLocators.CITY_USA)
        else:
            selected_city = self.driver.find_element(*VacanciesLocators.CITY)
        log.info("Selected city: " + selected_city.text + ".")
        assert city == selected_city.text, "Selected city doesn't match the expected."

    def click_find_career_button(self):
        log = self.get_logger()
        self.driver.find_element(*VacanciesLocators.FIND_CAREER_BUTTON).click()
        log.info("Find a career button clicked.")

    def find_number_available_vacancies(self, expected_positions):
        log = self.get_logger()
        card_elements = self.driver.find_elements(*VacanciesLocators.VACANCY_CARDS)
        visible_card_elements = [element for element in card_elements if element.is_displayed()]
        available_positions = len(visible_card_elements)
        assert available_positions == expected_positions, "Number of available positions doesn't match the expected value."
        vacancies = str(available_positions)
        expected_vacancies = str(expected_positions)
        log.info("Number of available positions (" + vacancies + ") matches the expected value (" + expected_vacancies + ").")
