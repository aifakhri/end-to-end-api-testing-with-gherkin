@view
Feature: Viewing Books
    As a member of a library
    I want to be able to get book info
    So that I can checkout the book I want

    Scenario Outline: Checkout Books
    Given the book "<bookTitle>" is selected by the member
    Then the member can see the detail of the book

    Examples: Book Title
    | bookTitle             |
    | The Russian           |
    | The Vanishing Half    |
    | Viscount Who Loved Me |