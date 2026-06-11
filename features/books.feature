Feature: Manage reading list

  As a reader with books I want to read
  I want to add books, mark them as read, and list them
  So that I can keep track of what I want to read and what I've finished

  Scenario: Adding a book captures its title
    Given I have a new book titled "Foundation"
    When I inspect the book
    Then its title should be "Foundation"

  Scenario: Newly added books are not marked as read
    Given I have a new book titled "Foundation"
    When I inspect the book
    Then it should not be marked as read

  Scenario: Marking a book as read flags it as read
    Given I have a new book titled "Foundation"
    When I mark the book as read
    Then it should be marked as read

  Scenario: Listing books returns all of them
    Given I have added books "Foundation" and "Dune"
    When I list the books
    Then I should see both "Foundation" and "Dune"
