# library for API requests needed for GET, POST, DELETE, ETC
import requests

# cookie = {'visit-month': 'February'}
# response = requests.get('http://rahulshettyacademy.com/', allow_redirects=False, cookies=cookie, timeout=)
# # print(response.history)
# print(response.status_code == 200)

# se = requests.session()
# se.cookies.update(cookie)
# cookieResponse = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2023'})
# print(cookieResponse.text)

# Attachments

url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
file = {'file': open('/Users/asoliz/Desktop/pic.jpg', 'rb')}
r = requests.post(url, files=file)
print(r.status_code)
print(r.json())
