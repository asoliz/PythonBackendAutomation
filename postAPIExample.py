import requests

from payLoad import addBookPayload

addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json=addBookPayload('genius'), headers={"Content-Type":"application/json"},)

print(addBook_response.json())
response_json = addBook_response.json()

bookId = response_json['ID']

deleteBook_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
  "ID": bookId
}, headers={"Content-Type":"application/json"},)
res_json = deleteBook_response.json()
print(res_json['msg'])

assert res_json['msg'] == "book is successfully deleted"
