from pytest_bdd import scenarios, given, then, parsers



scenarios("../features/view.feature")



# Given Step
@given(parsers.parse(
    'the book "{bookTitle}" is selected by the member'),
    target_fixture="select_book",
)
def select_book(books, bookTitle):
    get_book = books.getting_books()
    book_data = get_book.json()
    for book in book_data:
        if book['name'] == bookTitle:
            return str(book["id"])


# Then Step
@then('the member can see the detail of the book')
def view_book_detail(books, select_book):
    view_book = books.getting_books(bookId=select_book)
    book_info = view_book.json()
    assert book_info['price'] != 0
    assert book_info["author"] != ""