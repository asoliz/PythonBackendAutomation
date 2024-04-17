import requests  # # library for API requests needed for GET, POST, DELETE, ETC
import configparser
from payLoad import *
from utilities.configurations import *
from utilities.resources import *

# requests.<typeOfRequest> is the method to send a request - GET, POST, DELETE

# creating variable of generic header
header = {"Content-Type": "application/json"}

# POST /addBookUrl.php
# to add, use the addbook api and pass body and header
# storing addBookUrl from `configurations.py` class, `properties.ini` and `resources.py`
addBookUrl = getConfig()['API']['endpoint'] + ApiResources.addBook

# storing response to POST /addBook
addBook_response = requests.post(addBookUrl, json=buildBookPayloadFromCSV(), headers=header, )

# print status response and verify
print(addBook_response)
assert addBook_response.status_code == 200

# print then store the json response as json a variable
print(addBook_response.json())
addResponse_json = addBook_response.json()
# Validate the response
assert addResponse_json['Msg'] == "successfully added"

# access to response is like accessing dictionary - key value pairs
# storing bookId for e2e validation
bookId = addResponse_json['ID']

# DELETE /DeleteBook.php
# to delete, referencing `configuration.py`, `properties.ini` and `resources.py`
deleteBookUrl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
# use the delete api and pass the stored variable 'bookId'
deleteBook_response = requests.post(
    deleteBookUrl,
    json={"ID": bookId},  # using the stored bookID from addBookUrl
    headers=header, )

# print status response and verify
print(deleteBook_response)
assert deleteBook_response.status_code == 200

# print then store the response
print(deleteBook_response.json())
deleteResponse_json = deleteBook_response.json()
# Validate the response
assert deleteResponse_json['msg'] == "book is successfully deleted"

# GET /GetBook.php
# to get, referencing `configuration.py`, `properties.ini` and `resources.py`
getBookUrl = getConfig()['API']['endpoint'] + ApiResources.getBook
# use the getBook api and pass bookId as part of `ID` params
getBook_response = requests.get(getBookUrl,
                                params={'ID': bookId})

# print status response and verify
print(getBook_response)
assert getBook_response.status_code == 404

# print then store the response
print(getBook_response.json())
getResponse_json = getBook_response.json()
# Validate the response that deleted book cannot be found
assert getResponse_json['msg'] == "The book by requested bookid / author name does not exists!"
