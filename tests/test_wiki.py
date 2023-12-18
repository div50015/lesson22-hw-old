import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import config
from utils import data


def test_onboarding_screen():
    allure.dynamic.parameter('context', config.context)
    with step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(data.check_txt[0]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 2'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(data.check_txt[1]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 3'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(data.check_txt[2]))

    with step('Going next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Verify content page 4'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.text(data.check_txt[3]))
