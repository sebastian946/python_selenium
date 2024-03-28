from utils.utils import *

url = "https://tutorialsninja.com/demo/"
drop_my_account_classname = "dropdown"
login_link_text = "Login"
logout_link_text= "Logout"
input_email_id = "input-email"
input_password_id = "input-password"
button_login_xpath = "//*[@id='content']/div/div[2]/div/form/input"
title_my_account_xpath = "//h2[text()='My Account']"
waning_login_xpath= "//*[@id='account-login']/div[1]/text()"

def open_webpage():
    openBrowser(url)
    
def click_drop_account():
    click_element("classname",drop_my_account_classname)
    
def click_link_text_login():
    click_element("linktext",login_link_text)
    
def click_link_text_logout():
    click_element("linktext",logout_link_text)

def click_input_email():
    click_element("id",input_email_id)
    
def send_key_input_email(key_to_send):
    send_keys_element("id",input_email_id,key_to_send)
    
def click_input_password():
    click_element("id",input_password_id)
    
def send_key_input_password(key_to_send):
    send_keys_element("id",input_password_id,key_to_send)
    
def click_button_login():
    click_element("xpath",button_login_xpath)
    
def validate_title_my_account():
    assert_text_element("xpath",title_my_account_xpath,"My Account")
    
def validate_waning_login():
    assert_text_element("xpath",title_my_account_xpath,"Warning: No match for E-Mail Address and/or Password.")