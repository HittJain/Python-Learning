# =====================================================
# PYTHON FUNCTIONS - MASTER COMPLETE PROGRAM
# =====================================================

def print_table(title, rows):
    print("=" * 160)
    print(f"{title:^160}")
    print("=" * 160)
    print(f"{'Concept':<30} | {'Description':<50} | {'Example':<50}")
    print("-" * 160)

    for row in rows:
        row = [str(item) if item is not None else "" for item in row]
        print(f"{row[0]:<30} | {row[1]:<50} | {row[2]:<50}")

    print("=" * 160)


# =====================================================
# TABLE
# =====================================================

rows = [
    ["Built-in Function", "Predefined functions in Python", "print(), len(), sum()"],
    ["User-defined Function", "Created using def keyword", "def func(): pass"],
    ["Function Call", "Execute function", "func()"],
    ["Arguments", "Pass data to function", "func(x)"],
    ["Default Argument", "Has default value", "def f(x=10)"],
    ["Keyword Argument", "Named arguments", "f(x=5)"],
    ["*args", "Multiple positional arguments", "def f(*args)"],
    ["**kwargs", "Multiple keyword arguments", "def f(**kwargs)"],
    ["Lambda Function", "Anonymous one-line function", "lambda x: x*x"],
    ["Recursive Function", "Function calling itself", "factorial(n-1)"],
    ["Assign Function", "Store function in variable", "f = func"],
    ["Function inside Function", "Nested functions", "inner()"],
    ["Return Statement", "Returns value", "return x"],
    ["Return Function", "Function returns another function", "return inner"],
]

print_table("PYTHON FUNCTIONS - COMPLETE OVERVIEW", rows)


# =====================================================
# EXAMPLES
# =====================================================

print("\n\n=========== EXAMPLES ===========\n")


# 1. BUILT-IN FUNCTIONS
print("1. BUILT-IN FUNCTIONS")
print("Length:", len([1, 2, 3]))
print("Sum:", sum([1, 2, 3]))
print()


# 2. USER-DEFINED FUNCTION
print("2. USER-DEFINED FUNCTION")

def greet():
    print("Hello User!")

greet()
print()


# 3. FUNCTION WITH ARGUMENTS
print("3. FUNCTION WITH ARGUMENTS")

def add(a, b):
    print("Sum:", a + b)

add(5, 3)
print()


# 4. DEFAULT ARGUMENT
print("4. DEFAULT ARGUMENT")

def power(x, y=2):
    print(x ** y)

power(3)
power(3, 3)
print()


# 5. KEYWORD ARGUMENT
print("5. KEYWORD ARGUMENT")

def student(name, age):
    print(name, age)

student(age=20, name="Hitt")
print()


# 6. *args
print("6. *args")

def total(*nums):
    print("Sum:", sum(nums))

total(1, 2, 3, 4)
print()


# 7. **kwargs
print("7. **kwargs")

def info(**data):
    for k, v in data.items():
        print(k, ":", v)

info(name="Hitt", age=20)
print()


# 8. LAMBDA FUNCTION
print("8. LAMBDA FUNCTION")

square = lambda x: x * x
print("Square:", square(5))
print()


# 9. RECURSIVE FUNCTION
print("9. RECURSIVE FUNCTION")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
print()


# 10. ASSIGN FUNCTION TO VARIABLE
print("10. ASSIGN FUNCTION TO VARIABLE")

def say_hello():
    print("Hello!")

f = say_hello  # assigning function
f()
print()


# 11. FUNCTION INSIDE FUNCTION
print("11. FUNCTION INSIDE FUNCTION")

def outer():
    def inner():
        print("Inner function")
    inner()

outer()
print()


# 12. RETURN STATEMENT
print("12. RETURN STATEMENT")

def multiply(a, b):
    return a * b

print("Result:", multiply(4, 5))
print()


# 13. FUNCTION RETURNING FUNCTION
print("13. FUNCTION RETURNING FUNCTION")

def outer_func():
    def inner_func():
        return "Returned from inner function"
    return inner_func

result_func = outer_func()
print(result_func())
print()


# 14. PASS BY VALUE vs REFERENCE
print("14. PASS BY VALUE vs REFERENCE")

# Immutable (like value)
def change_num(x):
    x += 10
    print("Inside:", x)

num = 5
change_num(num)
print("Outside:", num)
print()

# Mutable (like reference)
def change_list(lst):
    lst.append(100)
    print("Inside:", lst)

my_list = [1, 2, 3]
change_list(my_list)
print("Outside:", my_list)
print()


print("=========== END ===========")