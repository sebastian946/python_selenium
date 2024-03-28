from behave import *
from stepDefinitions.searchStepDefinitions import *

@given(u'I got navigate to Home Page')
def step_impl(context):
    open_webpage()


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    click_on_search()
    send_keys_to_element("HP")


@when(u'I click on search button')
def step_impl(context):
    click_on_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    validate_text("HP LP3065")


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    click_on_search()
    send_keys_to_element("Honda")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    validate_text_error("There is no product that matches the search criteria.")


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    click_on_search()
    send_keys_to_element("")