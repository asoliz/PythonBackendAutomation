import json

courses = '{  "name" : "AlanSoliz",  "language" : [  "Java",  "Python"]}'

# loads method will parse json string and returns dictionary data type
dict_courses = json.loads(courses)

# to display name
print(dict_courses['name'])

# to display the list
print(dict_courses['language'])

# store list as a variable
list_language = dict_courses['language']

# below gives us Python
print(list_language[1])

# above is how we have parsed json to access values

print(dict_courses['language'][1])


# Requirement - parse from json file
with open('/Users/asoliz/projects/PythonBackendAutomation/files/courses') as f:
    # this will store data in the file as a dictionary
    data = json.load(f)
    for course in data['courses']:
        if course['title'] == 'Cypress':
            print(course['price'])
            break

with open('/Users/asoliz/projects/PythonBackendAutomation/files/course1.json') as fi:
    data2 = json.load(fi)
    assert data == data2
