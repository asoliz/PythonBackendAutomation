import requests
import configparser
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


# requests.<typeOfRequest> is the method to send a request
# requires url, body, header
addBookUrl = getConfig()['API']['endpoint']+ApiResources.addBook
header = {"Content-Type":"application/json"}
addBook_response = requests.post(addBookUrl, json=addBookPayload('genius'), headers=header,)

# view then store the response as json a variable
print(addBook_response.json())
response_json = addBook_response.json()

# access to response is like accessing dictionary - key value pairs
# accessing bookID in this example is by passing the key 'ID' and storing it for future use
bookId = response_json['ID']

# to delete, use the delete api and pass the stored variable 'bookId'
deleteBookUrl = getConfig()['API']['endpoint']+ApiResources.deleteBook
deleteBook_response = requests.post(deleteBookUrl, json={"ID": bookId}, headers=header,)

# view then store the response
print(deleteBook_response.json())
res_json = deleteBook_response.json()

# validate the response
assert res_json['msg'] == "book is successfully deleted"

authUrl = 'https://api.github.com/user'
github_response = requests.get(authUrl, auth=('alansoliz@gmail.com', getPassword()))
print(github_response.json())
