# Using Gherkin for End-to-End API Testing
## Introduction
Using the [keyword-drive-api-testing-framework](https://github.com/aifakhri/keyword-driven-api-testing-framework) to create Behaviour Driven Development (BDD) Testing with Gherkin syntax. The type of testing here is an end-to-end API testing type, where we imagine the [API from our use case](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md) is used in a library application where the member can borrow, update and return the book available in the library.

There are two features that can be tested:
1. View or Checkout feature
2. Book Transaction feature


## How To Run
To run all the tests use this command:
```Console
pytest
```
To run only view feature use this command:
```Console
pytest -m view
```
To run only transaction feature use this command:
```Console
pytest -m transaction
```

## Notes
If you have plenty of orders at the endpoint you could delete all the orders by using the ``delete_all_order.py`` script.