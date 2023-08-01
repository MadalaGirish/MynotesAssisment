import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(scope='class')
# def init_ff_driver(request):
#     ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = ff_driver
#     yield
#     ff_driver.close()

# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init__driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.cls.driver = web_driver
#     web_driver.implicitly_wait(10)
#     yield
#     web_driver.close()
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()