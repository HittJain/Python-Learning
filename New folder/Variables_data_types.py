from tabulate import tabulate
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

from tabulate import tabulate
import time

print("=" * 100)
print("             PYTHON DATA TYPES - DSA BASICS")
print("=" * 100)

data = [
    ["Numeric", "int", "No", "x = 42"],
    ["Numeric", "float", "No", "y = 3.14"],
    ["Numeric", "complex", "No", "z = 2 + 3j"],
    ["Sequence", "str", "No", 'text = "Hello"'],
    ["Sequence", "list", "Yes", "nums = [1,2,3]"],
    ["Sequence", "tuple", "No", "point = (4,5)"],
    ["Sequence", "range", "No", "r = range(10)"],
    ["Mapping", "dict", "Yes", 'user = {"id":1}'],
    ["Set", "set", "Yes", "unique = {1,2,3}"],
    ["Set", "frozenset", "No", "frozen = frozenset([1,2])"],
    ["Boolean", "bool", "No", "is_valid = True"],
    ["Binary", "bytes", "No", "b = b'Raw'"],
    ["Binary", "bytearray", "Yes", "ba = bytearray(5)"],
    ["Binary", "memoryview", "Depends", "mv = memoryview(b'Raw')"],
    ["Special", "NoneType", "No", "empty = None"]
]

print(tabulate(
    data,
    headers=["Category", "Data Type", "Mutable", "Example"],
    tablefmt="fancy_grid"
))

input("\nPress ENTER to learn each data type...\n")

# ---------------- Integer ----------------
print("=" * 80)
print("INTEGER (int)")
print("=" * 80)

age = 20

print("Code:")
print("age = 20\n")

print("Explanation:")
print("- Stores whole numbers.")
print("- Used for counting, indexing, loops, etc.")
print("- Value:", age)
print("- Data Type:", type(age))

input("\nNext...")

# ---------------- Float ----------------
print("\n" + "=" * 80)
print("FLOAT (float)")
print("=" * 80)

height = 5.8

print("Code:")
print("height = 5.8\n")

print("Explanation:")
print("- Stores decimal numbers.")
print("- Used in mathematics and measurements.")
print("- Value:", height)
print("- Data Type:", type(height))

input("\nNext...")

# ---------------- String ----------------
print("\n" + "=" * 80)
print("STRING (str)")
print("=" * 80)

name = "Rahul"

print('Code:\nname = "Rahul"\n')

print("Explanation:")
print("- Stores text.")
print("- Strings are immutable.")
print("- Value:", name)
print("- First Character:", name[0])
print("- Data Type:", type(name))

input("\nNext...")

# ---------------- List ----------------
print("\n" + "=" * 80)
print("LIST")
print("=" * 80)

nums = [10,20,30]

print("Code:")
print("nums = [10,20,30]\n")

print("Before:", nums)

nums.append(40)

print("After append(40):", nums)

print("""
Explanation:
✓ Ordered
✓ Mutable
✓ Most important data type in DSA
✓ Arrays in Python are usually represented using lists
""")

input("\nNext...")

# ---------------- Tuple ----------------
print("\n" + "=" * 80)
print("TUPLE")
print("=" * 80)

point = (10,20)

print(point)
print(type(point))

print("""
Explanation:
✓ Ordered
✓ Immutable
✓ Faster than list
✓ Used when values should not change
""")

input("\nNext...")

# ---------------- Dictionary ----------------
print("\n" + "=" * 80)
print("DICTIONARY")
print("=" * 80)

student = {
    "name":"Rahul",
    "age":20
}

print(student)
print("Student Name:", student["name"])

print("""
Explanation:
✓ Stores Key : Value pairs
✓ Mutable
✓ Very important for Hash Maps
""")

input("\nNext...")

# ---------------- Set ----------------
print("\n" + "=" * 80)
print("SET")
print("=" * 80)

s = {1,2,2,3,4,4}

print(s)

print("""
Explanation:
✓ Duplicate values are removed automatically.
✓ Unordered
✓ Mutable
✓ Used in searching and hashing
""")

input("\nNext...")

# ---------------- Boolean ----------------
print("\n" + "=" * 80)
print("BOOLEAN")
print("=" * 80)

is_student = True

print(is_student)
print(type(is_student))

print("""
Explanation:
Only two values:
True
False

Used in if-else conditions.
""")

input("\nNext...")

# ---------------- None ----------------
print("\n" + "=" * 80)
print("NONETYPE")
print("=" * 80)

x = None

print(x)
print(type(x))

print("""
Explanation:
Represents 'no value'.
""")

print("\nCongratulations!")
print("You have completed Python Data Types.")
print("Next Topic in Striver's Sheet: Input/Output and Time Complexity.")