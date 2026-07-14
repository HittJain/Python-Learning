# ==========================================================
# PYTHON CONDITIONAL STATEMENTS - COMPLETE REFERENCE
# ==========================================================

def print_table(title, rows):
    print("\n" + "=" * 120)
    print(f"{title:^120}")
    print("=" * 120)
    print(f"{'Statement':<15} | {'Description':<30} | {'Code Example':<40} | {'Output':<20}")
    print("-" * 120)

    for row in rows:
        output = "-" if row[3] is None else str(row[3])
        print(f"{row[0]:<15} | {row[1]:<30} | {row[2]:<40} | {output:<20}")

    print("=" * 120)


# ==========================================================
# BASIC VALUES
# ==========================================================
a = 10
b = 5


# ==========================================================
# 1. IF STATEMENT
# ==========================================================
if_example = [
    ("if", "Executes if condition is True", "if a > b: print('A is greater')", "A is greater"),
]

print_table("1. IF STATEMENT", if_example)


# ==========================================================
# 2. IF-ELSE STATEMENT
# ==========================================================
if_else_example = [
    ("if-else", "Two-way decision", "if a > b: print('A') else: print('B')", "A"),
]

print_table("2. IF-ELSE STATEMENT", if_else_example)


# ==========================================================
# 3. IF-ELIF-ELSE
# ==========================================================
if_elif_example = [
    ("if-elif-else", "Multiple conditions", 
     "if a < b: print('B') elif a == b: print('Equal') else: print('A')",
     "A"),
]

print_table("3. IF-ELIF-ELSE", if_elif_example)


# ==========================================================
# 4. NESTED IF
# ==========================================================
nested_if = [
    ("Nested if", "if inside if", 
     "if a > 0:\n    if a > b: print('A is larger positive')",
     "A is larger positive"),
]

print_table("4. NESTED IF", nested_if)


# ==========================================================
# 5. LOGICAL CONDITIONS
# ==========================================================
logical_conditions = [
    ("and", "Both conditions true", "if a>5 and b>2", True),
    ("or", "Any condition true", "if a>5 or b>10", True),
    ("not", "Reverse condition", "not(a>b)", False),
]

print_table("5. LOGICAL CONDITIONS", logical_conditions)


# ==========================================================
# 6. SHORT-HAND IF (TERNARY)
# ==========================================================
ternary = [
    ("Ternary", "One-line if-else", "result = 'A' if a>b else 'B'", "A"),
]

print_table("6. SHORT-HAND IF (TERNARY)", ternary)


# ==========================================================
# 7. PRACTICAL EXAMPLES
# ==========================================================
practical = [
    ("Even/Odd", "Check number type", "num=4 → even", "Even"),
    ("Voting", "Age >=18", "age=20 → eligible", "Eligible"),
    ("Grade", "Marks logic", "85 → Grade A", "Grade A"),
]

print_table("7. PRACTICAL EXAMPLES", practical)


# ==========================================================
# REAL EXECUTION (FOR UNDERSTANDING)
# ==========================================================
print("\n🔍 REAL EXECUTION OUTPUT:\n")

num = 4
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

age = 20
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")

marks = 85
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Fail")
