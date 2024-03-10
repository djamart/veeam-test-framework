from selenium.webdriver.common.by import By


class VacanciesLocators:
    DEPARTMENT = (By.CSS_SELECTOR, "#department-toggler")
    COUNTRY = (By.CSS_SELECTOR, ".vacancies-filter > div:nth-child(3) > div > div > button")
    STATE = (By.CSS_SELECTOR, ".vacancies-filter > div:nth-child(4) > div:nth-child(1) > div > div > button")
    CITY_USA = (By.CSS_SELECTOR, ".vacancies-filter > div:nth-child(4) > div:nth-child(3) > div > button")
    CITY = (By.CSS_SELECTOR, ".vacancies-filter > div:nth-child(3) > div:nth-child(4) > div > button")
    FIND_CAREER_BUTTON = (By.CSS_SELECTOR, ".btn.btn-outline-success")
    VACANCY_CARDS = (By.CLASS_NAME, "card-md-45")
