# Using Gherkin for End-to-End API Testing
## Introduction
Using the [keyword-drive-api-testing-framework](https://github.com/aifakhri/keyword-driven-api-testing-framework) to create Behaviour Driven Development (BDD) Testing with Gherkin syntax. The type of testing here is an end-to-end API testing type, where we imagine the [API from our use case](https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md) is used in a library application where the member can borrow, update and return the book available in the library.

There are two features that can be tested:
1. View or Checkout feature
2. Book Transaction feature


## How To Run
Currently only the view feature is available to test. To, test this feature, the following command can be used:
```Console
pytest -k test_view
```