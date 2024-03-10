# Selenium with Python Test Framework

This is a Selenium-based Python test framework created for the purpose of a skill assessment. It is designed to automate web browser interactions for testing web applications.

## Prerequisites
- Python 3.x installed on your system
- pip package manager installed

## Installation
1. Clone this repository to your local machine:

    ```
    git clone https://github.com/djamart/veeam-test-framework.git
    ```

2. Navigate to the project directory:

    ```
    cd veeam-test-framework
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run your test cases using Pytest.
2. Example command to run tests with Pytest with html report:

    ```
    pytest -v -s --html=report.html
    ```

## Project Structure
- `tests/`: Directory to store test scripts
- `utils/`: Directory containing utility functions for test setup and teardown
- `locators/`: Directory for storing locators (CSS selectors, XPaths)
- `pages/`: Directory containing methods to interact with webpages.
- `report.html`: Report created by Pytest-html
