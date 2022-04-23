Feature: Login to test Salesfore

  Scenario: Loign to test Salesforce with invalid credential          
    Given user with invalid credential                                     
    Then user cannot log in