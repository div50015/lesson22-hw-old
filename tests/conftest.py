import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from dotenv import load_dotenv
import config
from utils import  allure_attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(config.options_cfg)

    with allure.step('init app session'):
        browser.config.driver_remote_url = config.remote_url
        browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    allure_attach.attach_bstack_screenshot()
    allure_attach.attach_bstack_page_source()
    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if config.context == 'bstack' :
        allure_attach.attach_bstack_video(session_id)

