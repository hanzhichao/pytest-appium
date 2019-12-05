from appium import webdriver
import pytest


@pytest.fixture(scope='session')
def appium(variables):
    if not variables:
        pytest.skip('no variables file')
    caps = variables.get('caps')
    server = variables.get('server')
    if not caps or not server:
        pytest.skip('no "caps" or "server" in variables')
    try:
        driver = webdriver.Remote(server, caps)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        driver.implicitly_wait(10)
        yield driver
        driver.quit()


@pytest.fixture(scope='function', autouse=True)
def launch_close_app(appium):
    appium.launch_app()
    yield
    appium.close_app()
