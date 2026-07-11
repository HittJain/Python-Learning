print(" VARIABLES & DATA TYPES IN PYTHON\n")

print("1. Integer (int)")
age = 20
print("Code: age = 20")
print("Variable 'age' stores the whole number:", age)
print("Data Type:", type(age))
print()

print("2. Float (float)")
height = 5.9
print("Code: height = 5.9")
print("Variable 'height' stores the decimal number:", height)
print("Data Type:", type(height))
print()

print("3. String (str)")
name = "Rahul"
print('Code: name = "Rahul"')
print("Variable 'name' stores the text:", name)
print("Data Type:", type(name))
print()

print("4. Boolean (bool)")
is_student = True
print("Code: is_student = True")
print("Variable 'is_student' stores:", is_student)
print("Data Type:", type(is_student))
print()

print("5. List (list)")
subjects = ["Math", "Physics", "Python"]
print('Code: subjects = ["Math", "Physics", "Python"]')
print("A list stores multiple values:", subjects)
print("First subject is:", subjects[0])
print("Data Type:", type(subjects))
print()

print("6. Tuple (tuple)")
coordinates = (10, 20)
print("Code: coordinates = (10, 20)")
print("A tuple stores ordered values that cannot be changed.")
print("Value:", coordinates)
print("Data Type:", type(coordinates))
print()

print("7. Set (set)")
colors = {"Red", "Green", "Blue"}
print('Code: colors = {"Red", "Green", "Blue"}')
print("A set stores unique values.")
print("Value:", colors)
print("Data Type:", type(colors))
print()

print("8. Dictionary (dict)")
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Computer Science"
}
print("A dictionary stores key-value pairs.")
print("Student Details:", student)
print("Student Name:", student["name"])
print("Data Type:", type(student))
print()

print("========== END OF PROGRAM ==========")