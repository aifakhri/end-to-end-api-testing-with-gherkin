from pytest_bdd import scenarios, parsers, given, when, then



# Scenario
scenarios('../features/ordering.feature')


# Given script
@given('the member has decided the "<bookName>" they want to order')
def book_info(books, bookName):
    get_books = books.getting_books()
    book_data = get_books.json()
    for book in book_data:
        if book["name"] == bookName:
            bookId = book["id"]
            return bookId

#When Script
@when('the member send the order with their "<memberName>"')
def send_order(order, apiToken, book_info, membername):
    order.setup_auth_headers(apiToken)
    order.setup_

# Then script
@then('the customer get the information about the book "<bookName>"')
def check_book_info(book_detail, bookName):
    pass