import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://careers.veeam.com/vacancies")
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    print("\n\n>>>>> End of Test Run!")
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
