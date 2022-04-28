# dictionary: key , value pairs
from os import symlink


student = {"name": "rohan", "age": 18, "subject": ["Science", "Maths"]}

# we can access values with keys
print(student["name"])

# but if we try to access any value which is not in dictionary we will get value error , so in order to prevent that we can use get method , and if we want to add default value for cases where key is not found - we can add a second argument

print(student.get('age'))
print(student.get('phone'))  # output - None

print(student.get('height', 'not found'))  # instead of none we get not found
