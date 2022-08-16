Feature: Update and Return Book Order
    As the customer
    I want to be able to update my Info and return the book
    So that I could manage my account

    Background: The Customer Order is in The Record

    Scenario Outline: Updating Customer Name
        When the customer update their "<customerName>"
        Then the "<customerName>" is updated

    Examples: Customer Name
        | customerName |
        | Steve Levitt |
        | Sal Khan     |
        | Steph Dubner |

    Scenario: Returning Book Order
        When the customer return the book
        Then the orderId is deleted from the record