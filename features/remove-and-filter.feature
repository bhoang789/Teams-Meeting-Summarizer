Feature: Remove and filter books

  As a reader with a growing reading list
  I want to remove books I no longer want to read and filter to what's relevant
  So that my list stays focused on what matters

  Scenario: Removing a book removes it from the list
    Given I have added books "Foundation" and "Dune"
    When I remove "Foundation"
    Then the list should contain only "Dune"

  Scenario: Removing a book not in the list leaves the list unchanged
    Given I have added book "Foundation"
    When I remove "Nonexistent book"
    Then the list should still contain "Foundation"

  # Design decision: this reading list models a set of titles, so adding a
  # book that's already present is idempotent. (A "log of entries" list would
  # allow the duplicate instead — both are valid; this scenario picks one.)
  Scenario: Adding a book already in the list keeps a single entry
    Given I have added book "Foundation"
    When I add book "Foundation"
    Then the list should contain only "Foundation"

  Scenario: Filtering unread books returns only those not yet read
    Given I have added books "Foundation" and "Dune"
    And I have marked "Foundation" as read
    When I filter to unread books
    Then I should see only "Dune"

  Scenario: Filtering read books returns only those marked as read
    Given I have added books "Foundation" and "Dune"
    And I have marked "Foundation" as read
    When I filter to read books
    Then I should see only "Foundation"

  Scenario: Clearing all read books removes them from the list
    Given I have added books "Foundation" and "Dune"
    And I have marked "Foundation" as read
    When I clear read books
    Then the list should contain only "Dune"
