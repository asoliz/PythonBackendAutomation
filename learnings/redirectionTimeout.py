import requests

response = requests.get('http://rahulshettyacademy.com')
# history will show that there is a redirect of 301 then to 200
print(response.history)
print(response.status_code)

# adding allow_redirects to False will stop at the first status_code which will be 301
# useful when requirement is to validate no redirects occur
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False)
print(response.status_code)

# to give wait time for response - eg heavy commerce pages
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, timeout=3)
print(response.status_code)
