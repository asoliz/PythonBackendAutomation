# Created by Alan
  Feature: Verify if Books are added and deleted using Library API
# feature description here
  @cleanup @smoke # passed in cmd --tags=smoke
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added


  @cleanup @regression # passed in cmd --tags=regression
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      | isbn  | aisle |
      | fewod |  2342 |
      | fyrhg | 4786|


