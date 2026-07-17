# ==========================================================
# PYTHON STRINGS - COMPLETE LEARNING PROGRAM
# ==========================================================

def print_table(title, rows):
    print("=" * 160)
    print(f"{title:^160}")
    print("=" * 160)
    print(f"{'Concept':<35} | {'Description':<60} | {'Example':<50}")
    print("-" * 160)

    for row in rows:
        row = [str(item) if item is not None else "" for item in row]
        print(f"{row[0]:<35} | {row[1]:<60} | {row[2]:<50}")

    print("=" * 160)


# ==========================================================
# SUMMARY TABLE
# ==========================================================

rows = [
    ["Creating Strings", "Using single, double, triple quotes", "'hello', \"hi\""],
    ["Multiline Strings", "Using triple quotes", "'''multi line'''"],
    ["Indexing", "Access characters using index", "s[0], s[-1]"],
    ["Slicing", "Extract substring", "s[1:4]"],
    ["Looping", "Iterate string", "for ch in s"],
    ["Immutability", "Strings cannot change", "s[0]='H' ❌"],
    ["Delete String", "Delete using del", "del s"],
    ["Update String", "Create new string", "s = 'new'"],
    ["String Methods", "len, upper, strip", "s.upper()"],
    ["Concatenation", "Join strings", "a + b"],
    ["Repetition", "Repeat string", "a * 3"],
    ["Formatting", "f-string, format()", "f'{x}'"],
    ["Membership", "Check existence", "'a' in s"],
    ["Comparison", "Compare strings", "a == b"],
    ["Type Conversion", "int↔str, str→list", "str(5), int('5')"]
]

print_table("PYTHON STRINGS - COMPLETE OVERVIEW", rows)


# ==========================================================
# EXAMPLES START
# ==========================================================

print("\n\n=========== STRING EXAMPLES ===========\n")


# 1. CREATING STRINGS
print("1. CREATING STRINGS")
s1 = 'Hello'
s2 = "World"
s3 = '''Multi
Line
String'''
print(s1, s2)
print(s3)
print()


# 2. ACCESSING CHARACTERS (INDEXING)
print("2. INDEXING (POSITIVE & NEGATIVE)")
s = "Python"
print("Positive Index [0]:", s[0])
print("Negative Index [-1]:", s[-1])
print()


# 3. STRING SLICING
print("3. STRING SLICING")
print("s[0:4]:", s[0:4])
print("s[:3]:", s[:3])
print("s[2:]:", s[2:])
print("s[::-1] (reverse):", s[::-1])
print()


# 4. LOOPING THROUGH STRING
print("4. LOOPING THROUGH STRING")
for ch in s:
    print(ch, end=" ")
print("\n")


# 5. STRING IMMUTABILITY
print("5. STRING IMMUTABILITY")
try:
    s[0] = 'J'  # will raise error
except TypeError as e:
    print("Error:", e)
print("Strings cannot be changed directly\n")


# 6. DELETING A STRING
print("6. DELETING A STRING")
temp = "DeleteMe"
del temp
# print(temp)  # would give error
print("String deleted\n")


# 7. UPDATING A STRING
print("7. UPDATING A STRING")
s = "Hello"
s = "H" + s[1:]   # new string created
print("Updated:", s)
print()


# 8. COMMON STRING METHODS
print("8. STRING METHODS")
text = "  hello python  "
print("Length:", len(text))
print("Upper:", text.upper())
print("Strip:", text.strip())
print()


# 9. CONCATENATION & REPETITION
print("9. CONCATENATION & REPETITION")
a = "Hello"
b = "World"
print("Concatenation:", a + " " + b)
print("Repetition:", a * 3)
print()


# 10. STRING FORMATTING
print("10. STRING FORMATTING")

name = "Hitt"
age = 20

# f-string
print(f"My name is {name} and age is {age}")

# format()
print("My name is {} and age is {}".format(name, age))
print()


# 11. STRING MEMBERSHIP
print("11. MEMBERSHIP TESTING")
print("'P' in Python:", 'P' in "Python")
print("'z' not in Python:", 'z' not in "Python")
print()


# 12. STRING COMPARISON
print("12. STRING COMPARISON")
print("abc == abc:", "abc" == "abc")
print("abc > abd:", "abc" > "abd")  # lexicographical
print()


# 13. TYPE CONVERSIONS
print("13. TYPE CONVERSIONS")

# int → string
num = 100
s = str(num)
print("int to str:", s, type(s))

# string → int
s = "123"
num = int(s)
print("str to int:", num, type(num))

# string → list
s = "hello"
lst = list(s)
print("str to list:", lst)
print()


print("=========== END OF STRING PROGRAM ===========")