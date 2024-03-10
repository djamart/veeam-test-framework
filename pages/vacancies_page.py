from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from locators.vacancies_locators import VacanciesLocators
from utils.base_class import BaseClass


class VacanciesPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def select_department(self, department):
        default_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        if default_department.text != department:
            default_department.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]').click()
        selected_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        assert department in selected_department.text

    def select_country(self, country):
        default_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        if default_country.text != country:
            default_country.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]').click()
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        assert country in selected_country.text

    def select_state(self, state):
        default_state = self.driver.find_element(*VacanciesLocators.STATE)
        if default_state.text != state:
            default_state.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]').click()
        selected_state = self.driver.find_element(*VacanciesLocators.STATE)
        assert state in selected_state.text

    def select_city(self, city):
        default_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        if default_country.text == "USA":
            default_city = self.driver.find_element(*VacanciesLocators.CITY_USA)
        else:
            default_city = self.driver.find_element(*VacanciesLocators.CITY)
        if default_city.text != city:
            default_city.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]').click()
        if default_country.text == "USA":
            selected_city = self.driver.find_element(*VacanciesLocators.CITY_USA)
        else:
            selected_city = self.driver.find_element(*VacanciesLocators.CITY)
        assert city in selected_city.text

    def click_find_career_button(self):
        self.driver.find_element(*VacanciesLocators.FIND_CAREER_BUTTON).click()

    def find_number_available_vacancies(self, expected_positions):
        card_elements = self.driver.find_elements(*VacanciesLocators.VACANCY_CARDS)
        visible_card_elements = [element for element in card_elements if element.is_displayed()]
        available_positions = len(visible_card_elements)
        assert available_positions == expected_positions
        vacancies = str(available_positions)
        log = self.get_logger()
        log.info("Number of available positions matches the expected value: " + vacancies)
