# library for API requests needed for GET, POST, DELETE, ETC
import requests

# GET request made and stored in `response`
response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Rahul Shetty'})

# storing response in json format with .json() method - comes from `requests` library
formatted_response = response.json()  # converts to a `list` data type
print(type(formatted_response))
# you can assert that status code is successful
assert response.status_code == 200
assert response.headers['Content-Type'] == "application/json;charset=UTF-8"

for book in formatted_response:
    if book['isbn'] == 'undefined587':
        print(book)
        break

expected_book = {'book_name': 'Rahuls World', 'isbn': 'undefined587', 'aisle': '2529857'}

assert book == expected_book

