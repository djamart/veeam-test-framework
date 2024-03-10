from pages.vacancies_page import VacanciesPage
from utils.base_class import BaseClass


class TestVacanciesPage(BaseClass):

    def test_number_of_vacancies_available_in_austin(self):
        vacancies_page = VacanciesPage(self.driver)
        vacancies_page.select_department("Sales")
        vacancies_page.assert_selected_department("Sales")
        vacancies_page.select_country("USA")
        vacancies_page.assert_selected_country("USA")
        vacancies_page.select_state("Texas")
        vacancies_page.assert_selected_state("Texas")
        vacancies_page.select_city("Austin")
        vacancies_page.assert_selected_city("Austin")
        vacancies_page.click_find_career_button()
        vacancies_page.find_number_available_vacancies(2)

    def test_number_of_vacancies_available_in_bucharest(self):
        vacancies_page = VacanciesPage(self.driver)
        vacancies_page.select_department("Sales")
        vacancies_page.assert_selected_department("Sales")
        vacancies_page.select_country("Romania")
        vacancies_page.assert_selected_country("Romania")
        vacancies_page.select_city("Bucharest")
        vacancies_page.assert_selected_city("Bucharest")
        vacancies_page.click_find_career_button()
        vacancies_page.find_number_available_vacancies(19)
