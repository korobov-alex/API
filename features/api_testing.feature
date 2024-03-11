Feature: Testing API endpoints

  Scenario: Add a product with correct data
    Given the API is available
      When I add a product with correct data
      Then the product is successfully added

  Scenario: Add a product with negative price
    Given the API is available
      When I add a product with negative price
      Then the API returns an error

  Scenario: Change status to False if product amount is 0
    Given the API is available
      When I change a product date to amount 0
      Then the product status is False

  Scenario: Check if history of changes is returned by ID
    Given the API is available
      When I request the history of changes for a specific ID
      Then the API returns the history of changes