from behave import *
from stepDefinitions.searchStepDefinitions import *

@given(u'I navigate to Register Page')
def step_impl(context):
    pass


@when(u'I enter details into mandatory fields')
def step_impl(context):
    pass


@when(u'Click on Continue button')
def step_impl(context):
    pass


@then(u'Account should get created')
def step_impl(context):
    pass


@when(u'I enter details into all fields')
def step_impl(context):
    pass


@when(u'I click on Continue button')
def step_impl(context):
    pass


@when(u'I enter details into all fields except email fields')
def step_impl(context):
    pass


@when(u'I enter existing email into field')
def step_impl(context):
    pass


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    pass


@when(u'I dont enter anything into the fields')
def step_impl(context):
    pass


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    pass