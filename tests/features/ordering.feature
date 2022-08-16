Feature: Ordering and Getting Book
    As a customer of the book store
    I want to check the available books on the store and check the book detail
    So that I could order the book

    Scenario Outline: Find all books in the store
    Given the customer request the list of books
    When the customer select the specific book with "<bookId>" 
    Then the customer get the information about the book

    Examples: Book
        | bookId |
        | 1      |
        | 2      |
        | 6      |
        
    Scenario Outline: Ordering Book
    Given the customer has decided the book they want to order
    When the customer fill registration form with their "<customerName>"
    Then the customer get a valid orderId

    Examples: Customer
        | customerName |
        | Andy Dwyer   |
        | Jim Halpert  |
        | Kevin        |
    
