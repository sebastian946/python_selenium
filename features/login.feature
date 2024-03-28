Feature: Login Functionality
    
    @validate
    Scenario: Login with valid credentials
        Given I navigated to Login Page
        When I enter valid email "prueba@gmail.com" address and valid password into the fields "1234567"
        And I click on login button
        Then I should get logged in

    Scenario: Login with invalid email and valid password
        Given I navigated to Login Page
        When I enter invalid email "dontexist@gmail.com" address and invalid password into the fields "12356"
        And I click on login button
        Then I should get a proper warning message

    Scenario: Login with valid email and invalid password
        Given I navigated to Login Page
        When I enter valid email address "prueba@gmail.com" and invalid password into the fields "12345"
        And I click on login button
        Then I should get a proper warning message

    Scenario: Login with invalid email and valid password
        Given I navigated to Login Page
        When I enter invalid email address "dontexist@gmail.com" and valid password into the fields "1234567"
        And I click on login button
        Then I should get a proper warning message

    Scenario: Login withoud entering any credentials
        Given I navigated to Login Page
        When I dont enter anything into the email and password fields
        And I click on login button
        Then I should get a proper warning message