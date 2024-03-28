
from utils.utils import *



url = "https://tutorialsninja.com/demo/"
input_search_xpath = "//input[@name='search']"
search_button_classname= "input-group-btn"
title_product= "HP LP3065"
message_error_xpath = "//*[@id='content']/p[2]"

def open_webpage():
    openBrowser(url)
    

def click_on_search():
    click_element("xpath",input_search_xpath)
    
def send_keys_to_element(text_to_send):
    send_keys_element("xpath",input_search_xpath,text_to_send)
    
def click_on_search_button():
    click_element("classname",search_button_classname)
    
def validate_text(text_to_compare):
    assert_text_element("linktext",title_product,text_to_compare)

def validate_text_error(text_warning):
    assert_text_element("xpath",message_error_xpath,text_warning)