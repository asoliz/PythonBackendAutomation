import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):  # context becomes a global variable that can be used in the subsequent methods - when, then
    # creating variable of generic header
    context.header = {"Content-Type": "application/json"}
    # POST /addBookUrl.php
    # to add, use the addbook api and pass body and header
    # storing addBookUrl from `configurations.py` class, `properties.ini` and `resources.py`
    context.addBookUrl = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.payLoad = addBookPayload("wowss", "3242")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.addBookUrl, json=context.payLoad, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    # print status response and validate
    # print(context.addBook_response)
    assert context.addBook_response.status_code == 200

    # print then store the json response as json a variable to validate
    # print(context.addBook_response.json())
    addResponse_json = context.addBook_response.json()
    assert addResponse_json['Msg'] == "successfully added"

    # access to response is like accessing dictionary - key value pairs
    # storing bookId for e2e validation
    context.bookId = addResponse_json['ID']


@given('the Book details with {isbn} and {aisle}')  # arguments need to change from <> to {}
def step_impl(context, isbn, aisle):  # parameters are set from given step
    # creating variable of generic header
    context.header = {"Content-Type": "application/json"}
    # POST /addBookUrl.php
    # to add, use the addbook api and pass body and header
    # storing addBookUrl from `configurations.py` class, `properties.ini` and `resources.py`
    context.addBookUrl = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.payLoad = addBookPayload(isbn, aisle)  # arguments are being passed through feature file
