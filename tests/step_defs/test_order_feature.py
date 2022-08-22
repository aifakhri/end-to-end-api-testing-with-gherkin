from pytest_bdd import scenarios, given, when, then, parsers



# Scenario
scenarios('../features/ordering.feature')


# Given script
@given(parsers.parse('the member has decided the "{bookName}" they want to order'), \
    target_fixture="given_book_id")
def given_book_id(books, bookName):
    get_books = books.getting_books()
    book_data = get_books.json()

    for book in book_data:
        if book["name"] == bookName:
            return book["id"]

@given(parsers.parse('the "{memberName}" wants to return the book'), target_fixture="order_record")
@given(parsers.parse('the current {memberName} is in the order record'), target_fixture="order_record")
def order_record(orders, memberName):
    get_records = orders.getting_all_ordered_book_records()
    record_data = get_records.json()
    
    # For the sake of testing, If the customer is not in the record yet The submit the new record
    if len(record_data) != 0:
        for data in record_data:
            if data["customerName"] == memberName:
                return data["id"]
            else:
                orders.setup_request_body(bookId="1", customerName=memberName)
                response = orders.submitting_book_order()
                print(response)
                return response.json()["orderId"]
    elif len(record_data) == 0:
        orders.setup_request_body(bookId="1", customerName=memberName)
        response = orders.submitting_book_order()
        print(response)
        return response.json()["orderId"]

#When Script
@when(parsers.parse('the member send the order with their "{memberName}"'))
def submitting_order(orders, given_book_id, memberName):
    orders.setup_request_body(bookId=given_book_id, customerName=memberName)
    orders.submitting_book_order()


@when(parsers.parse('the member want to update their "{newName}"'))
def updating_member_data(orders, order_record, newName):
    orders.updating_ordered_book_record(customerName=newName, orderId=order_record)


# Then script
@then(parsers.parse('"{memberName}" order is recorded'))
def check_order_id(orders, memberName, given_book_id):
    get_order = orders.getting_all_ordered_book_records()
    order_data = get_order.json()    
    data_len = len(order_data) - 1
    assert order_data[data_len]["customerName"] == memberName
    assert order_data[data_len]["bookId"] == given_book_id


@then(parsers.parse('the "{newName}" is updated in the record'))
def check_updated_member_name(orders, order_record, newName):
    response = orders.getting_single_ordered_book_record(orderId=order_record)
    record = response.json()
    assert record["customerName"] == newName

@then("the order is deleted from the record")
def delete_order(orders, order_record):
    orders.deleting_ordered_book_record(orderId=order_record)
    
    check_order = orders.getting_single_ordered_book_record(orderId=order_record)

    check_order = check_order.json()
    assert order_record in check_order["error"]
    