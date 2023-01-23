import pytest

from web_test.helpers.resources import Resources


@pytest.mark.skip(reason='Not implemented yet')
@pytest.mark.layout
def test_login_page_layout():
    raise NotImplementedError


def test_successful_login(driver, login_page, valid_user):
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    """
    inventory_page = login_page.perform_successful_login(valid_user.username, valid_user.password)
    assert inventory_page.is_page_displayed()

    # to demonstrate how to verify that element is not displayed
    # assert login_page.is_element_not_displayed(login_page.LOGIN_BUTTON_LOCATOR)


def test_locked_out_login(driver, login_page, locked_out_user):
    login_page.perform_unsuccessful_login(locked_out_user.username, locked_out_user.password)
    assert login_page.login_button.is_displayed()
    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == Resources.LoginPage.ERROR_MESSAGE_FOR_LOCKED_OUT_USER
    assert login_page.username_error_marker.is_displayed()
    assert login_page.password_error_marker.is_displayed()


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_username():
    raise NotImplementedError


@pytest.mark.skip(reason='Not implemented yet')
def test_login_without_password():
    raise NotImplementedError
