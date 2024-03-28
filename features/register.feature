Feature: Register Account functionality

    Scenario: Register with mandatory fields
        Given I navigate to Register Page
        When I enter details into mandatory fields
        And Click on Continue button
        Then Account should get created

    Scenario: Register with all fields
        Given I navigate to Register Page
        When I enter details into all fields
        And I click on Continue button
        Then Account should get created

    Scenario: Register with a duplicate email address
        Given I navigate to Register Page
        When I enter details into all fields except email fields
        And I enter existing email into field
        And I click on Continue button
        Then Proper warning message informing about duplicate account should be displayed


    Scenario: Register Without providing any details
        Given I navigate to Register Page
        When I dont enter anything into the fields
        And I click on Continue button
        Then Proper warning message for every mandatory fields should be displayed
