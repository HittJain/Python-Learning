# ==========================================================
# PYTHON OPERATORS - COMPLETE REFERENCE (39 OPERATORS)
# ==========================================================

def print_table(title, rows):
    print("\n" + "=" * 110)
    print(f"{title:^110}")
    print("=" * 110)
    print(f"{'Operator':<10} | {'Description':<30} | {'Code Example':<35} | {'Output':<20}")
    print("-" * 110)

    for op, desc, code, output in rows:
        print(f"{op:<10} | {desc:<30} | {code:<35} | {str(output):<20}")

    print("=" * 110)


a = 10
b = 3

# ==========================================================
# 1. ARITHMETIC OPERATORS (7)
# ==========================================================
arithmetic = [
    ("+", "Addition", "10 + 3", a + b),
    ("-", "Subtraction", "10 - 3", a - b),
    ("*", "Multiplication", "10 * 3", a * b),
    ("/", "Division (float)", "10 / 3", round(a / b, 2)),
    ("//", "Floor Division", "10 // 3", a // b),
    ("%", "Modulus", "10 % 3", a % b),
    ("**", "Exponentiation", "10 ** 3", a ** b),
]

print_table("1. ARITHMETIC OPERATORS (7)", arithmetic)


# ==========================================================
# 2. ASSIGNMENT OPERATORS (13)
# ==========================================================
assignment = []

x = 10; assignment.append(("=", "Assign", "x = 10", x))

x = 10; x += 3; assignment.append(("+=", "Add & Assign", "x += 3", x))
x = 10; x -= 3; assignment.append(("-=", "Subtract & Assign", "x -= 3", x))
x = 10; x *= 3; assignment.append(("*=", "Multiply & Assign", "x *= 3", x))
x = 10; x /= 3; assignment.append(("/=", "Divide & Assign", "x /= 3", round(x, 2)))
x = 10; x //= 3; assignment.append(("//=", "Floor Divide & Assign", "x //= 3", x))
x = 10; x %= 3; assignment.append(("%=", "Modulus & Assign", "x %= 3", x))
x = 10; x **= 3; assignment.append(("**=", "Exponent & Assign", "x **= 3", x))

x = 10; x &= 3; assignment.append(("&=", "Bitwise AND Assign", "x &= 3", x))
x = 10; x |= 3; assignment.append(("|=", "Bitwise OR Assign", "x |= 3", x))
x = 10; x ^= 3; assignment.append(("^=", "Bitwise XOR Assign", "x ^= 3", x))
x = 10; x >>= 1; assignment.append((">>=", "Right Shift Assign", "x >>= 1", x))
x = 10; x <<= 1; assignment.append(("<<=", "Left Shift Assign", "x <<= 1", x))

print_table("2. ASSIGNMENT OPERATORS (13)", assignment)


# ==========================================================
# 3. COMPARISON OPERATORS (6)
# ==========================================================
comparison = [
    ("==", "Equal to", "10 == 3", a == b),
    ("!=", "Not equal to", "10 != 3", a != b),
    (">", "Greater than", "10 > 3", a > b),
    ("<", "Less than", "10 < 3", a < b),
    (">=", "Greater or equal", "10 >= 3", a >= b),
    ("<=", "Less or equal", "10 <= 3", a <= b),
]

print_table("3. COMPARISON OPERATORS (6)", comparison)


# ==========================================================
# 4. LOGICAL OPERATORS (3)
# ==========================================================
logical = [
    ("and", "Logical AND", "True and False", True and False),
    ("or", "Logical OR", "True or False", True or False),
    ("not", "Logical NOT", "not True", not True),
]

print_table("4. LOGICAL OPERATORS (3)", logical)


# ==========================================================
# 5. IDENTITY OPERATORS (2)
# ==========================================================
x = [1, 2]
y = [1, 2]
z = x

identity = [
    ("is", "Same object", "x is z", x is z),
    ("is not", "Different object", "x is not y", x is not y),
]

print_table("5. IDENTITY OPERATORS (2)", identity)


# ==========================================================
# 6. MEMBERSHIP OPERATORS (2)
# ==========================================================
membership = [
    ("in", "Value in sequence", "'a' in 'apple'", 'a' in 'apple'),
    ("not in", "Value not in sequence", "'x' not in 'apple'", 'x' not in 'apple'),
]

print_table("6. MEMBERSHIP OPERATORS (2)", membership)


# ==========================================================
# 7. BITWISE OPERATORS (6)
# ==========================================================
bitwise = [
    ("&", "AND", "10 & 3", a & b),
    ("|", "OR", "10 | 3", a | b),
    ("^", "XOR", "10 ^ 3", a ^ b),
    ("~", "NOT", "~10", ~a),
    ("<<", "Left Shift", "10 << 1", a << 1),
    (">>", "Right Shift", "10 >> 1", a >> 1),
]

print_table("7. BITWISE OPERATORS (6)", bitwise)


# ==========================================================
# SUMMARY
# ==========================================================
print("\n TOTAL SUMMARY")
print("Categories: 7")
print("Total Operators: 39")