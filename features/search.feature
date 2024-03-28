Feature: Search functionality

    @completed
    Scenario: Search for a valid product
        Given I got navigate to Home Page
        When I enter valid product into the Search box field
        And I click on search button
        Then Valid product should get displayed in Search results

    Scenario: Search for an invalid product
        Given I got navigate to Home Page
        When I enter invalid product into the Search box field
        And I click on search button
        Then Proper message should be displayed in Search results

    Scenario: Search withput entering any prpduct
        Given I got navigate to Home Page
        When I dont enter anything into Search box field
        And I click on search button
        Then Proper message should be displayed in Search results