import requests

cookie = {'visit-month': 'February'}
# below will send explicitly the cookie stated
response = requests.get('http://httpbin.org/cookies', cookies=cookie)
print(response.text)

# Using Session Manager
# if there's a need for a common cookie, store a session with session() function
se = requests.session()
# add a common cookie with cookies.update() and pass the common cookie
se.cookies.update({'visit-year': '2024'})

# below will send common cookie along with explicitly stated cookie because we're using `se` session
response = se.get('http://httpbin.org/cookies', cookies=cookie)
print(response.text)
