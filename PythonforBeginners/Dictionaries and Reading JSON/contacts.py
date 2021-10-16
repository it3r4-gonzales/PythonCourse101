#example of a JSON data

contacts = {
    "number" :4,
    "students" :
    [
        {"name":"Bret Star" ,"email":"bretstar@example.com"},
        {"name":"Harry Potter" ,"email":"harry@example.com"},
        {"name":"Hermione Granger" ,"email":"granger@example.com"},
        {"name":"Ron Weasly" ,"email":"ron@example.com"}
    ]
}
#getting dictionary in nested dictionary
for student in contacts["students"]:
    print(student)

#getting the key value
for student in contacts["students"]:
    print(student["email"])

# getting the name values
for student in contacts["students"]:
    print(student["name"])





