Feature: Handle storing, retrieving and deleting customer details
    Scenario: Retreive user1 info
        Given app is running
        When I hit url with 'sridharc20'
        Then I should get a '200' response
        And the following user details are returned
            | name      |
            | Sridhar C |
    Scenario: Retreive user2 info
        Given app is running
        When I hit url with 'venu1'
        Then I should get a '200' response
        And the following user details are returned
            | name      |
            | Venu G    |