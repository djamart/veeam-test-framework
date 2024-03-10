from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestCareersPage:

    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://careers.veeam.com/vacancies")
        driver.maximize_window()
        driver.implicitly_wait(5)

        # Selects Sales department
        selected_department = driver.find_element(By.CSS_SELECTOR, "#department-toggler")
        default_department_text = selected_department.text
        expected_department_text = "Sales"
        if default_department_text != expected_department_text:
            selected_department.click()
            driver.find_element(By.XPATH, '//a[text()="' + expected_department_text + '"]').click()
        selected_department_text = selected_department.text
        # Checks department selected
        assert expected_department_text in selected_department_text

        # Selects USA country
        selected_country = driver.find_element(By.CSS_SELECTOR,
                                               ".vacancies-filter > div:nth-child(3) > div > div > button")
        default_country_text = selected_country.text
        expected_country_text = "USA"
        if default_country_text != expected_country_text:
            selected_country.click()
            driver.find_element(By.XPATH, '//a[text()="' + expected_country_text + '"]').click()
        selected_country_text = selected_country.text
        # Checks department selected
        assert expected_country_text in selected_country_text

        # Selects Texas State
        selected_state = driver.find_element(By.CSS_SELECTOR,
                                             ".vacancies-filter > div:nth-child(4) > div:nth-child(1) > div > div > button")
        default_state_text = selected_state.text
        expected_state_text = "Texas"
        if default_state_text != expected_state_text:
            selected_state.click()
            ActionChains(driver).move_to_element(
                driver.find_element(By.XPATH, '//a[text()="' + expected_state_text + '"]')).perform()
            driver.find_element(By.XPATH, '//a[text()="' + expected_state_text + '"]').click()
        selected_state_text = selected_state.text
        # Checks department selected
        assert expected_state_text in selected_state_text

        # Selects Austin City
        if selected_country_text == "USA":
            selected_city = driver.find_element(By.CSS_SELECTOR,
                                               ".vacancies-filter > div:nth-child(4) > div:nth-child(3) > div > button")
        else:
            selected_city = driver.find_element(By.CSS_SELECTOR,
                                               ".vacancies-filter > div:nth-child(3) > div:nth-child(4) > div > button")
        default_city_text = selected_city.text
        expected_city_text = "Austin"
        if default_city_text != expected_city_text:
            selected_city.click()
            driver.find_element(By.XPATH, '//a[text()="' + expected_city_text + '"]').click()
        selected_city_text = selected_city.text
        # Checks department selected
        assert expected_city_text in selected_city_text

        # Clicks Find a career
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-success").click()

        # Checks number of available positions
        card_elements = driver.find_elements(By.CLASS_NAME, "card-md-45")
        visible_card_elements = [element for element in card_elements if element.is_displayed()]
        available_positions = len(visible_card_elements)
        expected_positions = 2
        assert available_positions == expected_positions
