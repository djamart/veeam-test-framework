import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators.vacancies_locators import VacanciesLocators


class VacanciesPage:

    def __init__(self, driver):
        self.driver = driver

    def select_department(self, department):
        selected_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        if selected_department.text != department:
            selected_department.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + department + '"]').click()

    def assert_selected_department(self, department):
        selected_department = self.driver.find_element(*VacanciesLocators.DEPARTMENT)
        assert department in selected_department.text

    def select_country(self, country):
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        if selected_country.text != country:
            selected_country.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + country + '"]').click()

    def assert_selected_country(self, country):
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        assert country in selected_country.text

    def select_state(self, state):
        selected_state = self.driver.find_element(*VacanciesLocators.STATE)
        if selected_state.text != state:
            selected_state.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + state + '"]').click()

    def assert_selected_state(self, state):
        selected_state = self.driver.find_element(*VacanciesLocators.STATE)
        assert state in selected_state.text

    def select_city(self, city):
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        if selected_country.text == "USA":
            selected_city = self.driver.find_element(*VacanciesLocators.CITY_USA)
        else:
            selected_city = self.driver.find_element(*VacanciesLocators.CITY)
        if selected_city.text != city:
            selected_city.click()
            ActionChains(self.driver).move_to_element(
                self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]')).perform()
            self.driver.find_element(By.XPATH, '//a[text()="' + city + '"]').click()

    def assert_selected_city(self, city):
        selected_country = self.driver.find_element(*VacanciesLocators.COUNTRY)
        if selected_country.text == "USA":
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
        print("Number of available positions:", available_positions)
        assert available_positions == expected_positions
