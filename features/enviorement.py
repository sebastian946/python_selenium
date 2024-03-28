from utils.utils import close_browser
from behave import after_scenario


@after_scenario
def after_scenario(context,scenario):
    close_browser()
