# ==========================================================
# PYTHON TUPLES
# ==========================================================

def print_table(title, rows):
    print("=" * 160)
    print(f"{title:^160}")
    print("=" * 160)
    print(f"{'Concept':<40} | {'Description':<60} | {'Example':<50}")
    print("-" * 160)

    for row in rows:
        row = [str(item) if item is not None else "" for item in row]
        print(f"{row[0]:<40} | {row[1]:<60} | {row[2]:<50}")

    print("=" * 160)


# ==========================================================
# SUMMARY TABLE
# ==========================================================

rows = [
    ["Creating Tuple", "Using () or comma-separated values", "(1,2,3)"],
    ["Mixed Datatypes", "Different data types allowed", "(1,'a',3.5)"],
    ["Accessing Elements", "Index-based access", "t[0], t[-1]"],
    ["Concatenation", "Combine tuples", "t1 + t2"],
    ["Slicing", "Extract part of tuple", "t[1:3]"],
    ["Deleting Tuple", "Delete entire tuple", "del t"],
    ["Tuple Unpacking", "Assign values to variables", "a,b = t"],
    ["Asterisk Unpacking", "Flexible unpacking", "a,*b = t"],
    ["Reversing Tuple", "Reverse elements", "t[::-1]"],
    ["List of Tuples → Dict", "Convert to dictionary", "dict(list_of_tuples)"],
    ["Namedtuple", "Tuple with named fields", "namedtuple('P', 'x y')"]
]

print_table("PYTHON TUPLES - COMPLETE OVERVIEW", rows)


# ==========================================================
# EXAMPLES START
# ==========================================================

print("\n\n=========== TUPLE EXAMPLES ===========\n")


# 1. CREATING TUPLES
print("1. CREATING TUPLES")

t1 = (1, 2, 3)
t2 = 4, 5, 6   # without parentheses
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print()


# 2. MIXED DATATYPES
print("2. MIXED DATATYPES")

t = (1, "Python", 3.5, True)
print("Mixed Tuple:", t)
print()


# 3. ACCESSING ELEMENTS
print("3. ACCESSING ELEMENTS")

print("First element:", t[0])
print("Last element:", t[-1])
print()


# 4. CONCATENATION
print("4. CONCATENATION")

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated:", t3)
print()


# 5. SLICING
print("5. SLICING")

t = (10, 20, 30, 40, 50)
print("t[1:4]:", t[1:4])
print("t[::-1] (reverse):", t[::-1])
print()


# 6. DELETING TUPLE
print("6. DELETING TUPLE")

temp = (1, 2, 3)
del temp
# print(temp)  # would cause error
print("Tuple deleted\n")


# 7. TUPLE UNPACKING
print("7. TUPLE UNPACKING")

t = (1, 2, 3)
a, b, c = t
print("a:", a, "b:", b, "c:", c)
print()


# 8. ASTERISK UNPACKING
print("8. ASTERISK UNPACKING")

t = (1, 2, 3, 4, 5)
a, *b, c = t
print("a:", a)
print("b:", b)  # list of middle elements
print("c:", c)
print()


# 9. REVERSING A TUPLE
print("9. REVERSING A TUPLE")

t = (1, 2, 3, 4)
rev = t[::-1]
print("Reversed:", rev)
print()


# 10. LIST OF TUPLES → DICTIONARY
print("10. LIST OF TUPLES → DICTIONARY")

pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print("Dictionary:", d)
print()


# 11. NAMEDTUPLE
print("11. NAMEDTUPLE")

from collections import namedtuple

# Define namedtuple
Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print("Point:", p)
print("x:", p.x)
print("y:", p.y)
print()


# ==========================================================
# IMPORTANT CONCEPT: IMMUTABILITY
# ==========================================================

print("12. TUPLE IMMUTABILITY")

t = (1, 2, 3)
try:
    t[0] = 10  # will give error
except TypeError as e:
    print("Error:", e)

print("Tuples cannot be changed (immutable)\n")


print("=========== END OF TUPLE PROGRAM ===========")