# to parse json import the following
import json

# storing json as a string variable
courses = '{  "name" : "AlanSoliz",  "language" : [  "Java",  "Python"]}'

# the loads method will parse `courses` variable which is json string and returns dictionary data type - dict_courses
dict_courses = json.loads(courses)
print("`dict_courses` is a", type(dict_courses))

# now in order to display `name`
print(dict_courses['name'])

# to display the list
print(dict_courses['language'])

# store `language` as a list variable
list_language = dict_courses['language']
print("`list_language` is a", type(list_language))

# below gives us Python
print("Index 1 of list_language is:", list_language[1])

# above is how we have parsed json to access values

print(dict_courses['language'][1])

# Requirement - parse from json file and find price of a course
with open('/files/courses') as f:
    # load() converts file object to dictionary
    data = json.load(f)
    # this will loop through the list of 'courses'
    for course in data['courses']:
        # this will check if the 'title' is 'Cypress'
        if course['title'] == 'Cypress':
            print("The price for Cypress course is:", course['price'])
            # breaking the loop since no need to proceed
            break

# Requirement - compare two jsons
with open('/files/course1.json') as fi:
    # load() converts file object to dictionary
    data2 = json.load(fi)
    # assert if both files are equal which they are not and will error
    assert data == data2

# Requirement - parse from json file and extract website for Selenum Python
with open('/files/courses') as f:
    # load() converts file object to dictionary
    data = json.load(f)
    # this will loop through the list of 'courses'
    for course in data['courses']:
        # this will check if the 'title' is 'Selenium Python'
        if course['title'] == 'Selenium Python':
            print("The details for Selenium Python course is:", course['details']['site'])
            # breaking the loop since no need to proceed
            break
