# ==========================================================
# PYTHON LISTS
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
    ["Creating List []", "Using square brackets", "[1,2,3]"],
    ["list() Constructor", "Create from iterable", "list('abc')"],
    ["Repeated Elements", "Using * operator", "[0]*5"],
    ["Indexing", "Access elements by index", "a[0], a[-1]"],
    ["Updating", "Modify elements", "a[1]=10"],
    ["append()", "Add element at end", "a.append(5)"],
    ["insert()", "Insert at position", "a.insert(1,100)"],
    ["extend()", "Add multiple elements", "a.extend([1,2])"],
    ["remove()", "Remove by value", "a.remove(2)"],
    ["pop()", "Remove by index", "a.pop()"],
    ["del", "Delete element/list", "del a[0]"],
    ["clear()", "Remove all elements", "a.clear()"],
    ["Looping", "Iterate list", "for i in a"],
    ["Nested List", "List inside list", "[[1,2],[3,4]]"],
    ["Multi-dimensional", "Matrix-style lists", "a[0][1]"]
]

print_table("PYTHON LISTS - COMPLETE OVERVIEW", rows)


# ==========================================================
# EXAMPLES START
# ==========================================================

print("\n\n=========== LIST EXAMPLES ===========\n")


# 1. CREATING LISTS
print("1. CREATING LISTS")

# Using square brackets
a = [1, 2, 3]
print("Square Brackets:", a)

# Using list() constructor
b = list("Python")
print("list() constructor:", b)

# Repeated elements
c = [0] * 5
print("Repeated elements:", c)
print()


# 2. INTERNAL REPRESENTATION & INDEXING
print("2. INDEXING & INTERNAL STRUCTURE")

a = [1, 2, 2, "Python"]
print("List:", a)

# Index-based access
print("a[0]:", a[0])     # first element
print("a[-1]:", a[-1])   # last element
print()


# 3. ADDING ELEMENTS
print("3. ADDING ELEMENTS")

a = [1, 2, 3]

# append()
a.append(4)
print("append:", a)

# insert()
a.insert(1, 100)
print("insert:", a)

# extend()
a.extend([5, 6])
print("extend:", a)
print()


# 4. UPDATING ELEMENTS
print("4. UPDATING ELEMENTS")

a[0] = 10
print("Updated list:", a)
print()


# 5. REMOVING ELEMENTS
print("5. REMOVING ELEMENTS")

a = [1, 2, 3, 4, 5]

# remove()
a.remove(3)
print("remove:", a)

# pop()
a.pop()
print("pop:", a)

# del
del a[0]
print("del:", a)

# clear()
a.clear()
print("clear:", a)
print()


# 6. ITERATING OVER LIST
print("6. ITERATING OVER LIST")

a = [10, 20, 30]

# simple loop
for item in a:
    print(item, end=" ")
print()

# using index
for i in range(len(a)):
    print(f"Index {i} -> {a[i]}")
print()


# 7. NESTED LIST
print("7. NESTED LIST")

nested = [[1, 2], [3, 4]]
print("Nested List:", nested)

# Accessing
print("nested[0]:", nested[0])
print("nested[0][1]:", nested[0][1])
print()


# 8. MULTI-DIMENSIONAL LIST (MATRIX)
print("8. MULTI-DIMENSIONAL LIST")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing matrix
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
print()


# 9. ADVANCED ITERATION (IMPORTANT)
print("9. ADVANCED ITERATION")

# enumerate()
a = ['a', 'b', 'c']
for index, value in enumerate(a):
    print(index, value)
print()


print("=========== END OF LIST PROGRAM ===========")