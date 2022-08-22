@transaction
Feature: Book Transaction
    As a member of the library
    I want to checkout the available book
    So that I could order the book

    @order_book    
    Scenario Outline: Ordering Book
    Given the member has decided the "<bookTitle>" they want to order
    When the member send the order with their "<memberName>"
    Then "<memberName>" order is recorded

    Examples: Members
        | bookTitle               | memberName   |
        | The Russian             | Andy Dwyer   |
        | The Vanishing Half      | Jim Halpert  |
        | Viscount Who Loved Me   | Angela       |

    @update_info
    Scenario Outline: Updating Order
    Given the current "<memberName>" is in the order record
    When the member want to update their "<newName>"
    Then the "<newName>" is updated in the record

    Examples: Names
        | memberName   | newName       |
        | Andy Dwyer   | Leslie Knope  |
        | Jim Halpert  | Michael Scott |
        | Angela       | Annie         |

    @return_book
    Scenario Outline: Returning a book
    Given the "<memberName>" wants to return the book
    Then the order is deleted from the record

    Examples: Member Book List
        | memberName     |
        | Leslie Knope   |       
        | Michael Scott |
        | Annie         |