from behave import *
from stepDefinitions.loginStepDefinitions import *

@given(u'I navigated to Login Page')
def step_impl(context):
    open_webpage()
    click_drop_account()
    click_link_text_login()


@when(u'I enter valid email "{email}" address and valid password into the fields "{password}"')
def step_impl(context,email,password):
    click_input_email()
    send_key_input_email(email)
    send_key_input_password(password)


@when(u'I click on login button')
def step_impl(context):
    click_button_login()


@then(u'I should get logged in')
def step_impl(context):
    validate_title_my_account()
    click_link_text_logout()
    


@when(u'I enter invalid email "{email}" address and invalid password into the fields "{password}"')
def step_impl(context,email,password):
    click_input_email()
    send_key_input_email(email)
    send_key_input_password(password)


@then(u'I should get a proper warning message')
def step_impl(context):
    validate_waning_login()


@when(u'I enter valid email address "{email}" and invalid password into the fields "{password}"')
def step_impl(context,email,password):
    click_input_email()
    send_key_input_email(email)
    send_key_input_password(password)


@when(u'I enter invalid email address "{email}" and valid password into the fields "{password}"')
def step_impl(context,email,password):
    click_input_email()
    send_key_input_email(email)
    send_key_input_password(password)


@when(u'I dont enter anything into the email and password fields')
def step_impl(context):
    click_input_email()