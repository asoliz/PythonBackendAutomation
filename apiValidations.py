import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Rahul Shetty'})
formatted_response = response.json()
print(type(formatted_response))

for book in formatted_response:
    if book['isbn'] == 'undefined587':
        print(book)
        break

expected_book = {'book_name': 'Rahuls World', 'isbn': 'undefined587', 'aisle': '2529866'}

assert book == expected_book

