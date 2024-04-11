# Attachments
import requests

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
file = {'file': open('/Users/asoliz/projects/PythonBackendAutomation/files/face.jpeg', 'rb')}
r = requests.post(url, files=file)
print(r.status_code)
print(r.json())
