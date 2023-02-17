import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opt
from selenium.webdriver.firefox.options import Options as ff_opt


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
        help="Choose browser: chrome or firefox. Default chrome"
    )
    parser.addoption(
        '--language', action='store', default=None,
        help='Choose language, default en: i.g. --language=ru'
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')

    if browser_name == 'chrome':
        chr_options = chr_opt()
        chr_options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        browser = webdriver.Chrome(options=chr_options)

    if browser_name == 'firefox':
        ff_options = ff_opt()
        ff_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=ff_options)

    browser.implicitly_wait(10)
    yield browser
    browser.quit()




"""import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb")

@pytest.fixture(scope="function")
def browser(request):
    languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print(
            "\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans "
            "en-gb".format(
                language))
        pytest.fail("Wrong Language")

    yield browser
    print("\nquit browser..")
    browser.quit()"""


"""import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):


    user_language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()"""







'''@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()'''
