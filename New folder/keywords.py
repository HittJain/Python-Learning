# ==========================================================
# PYTHON KEYWORDS - COMPLETE REFERENCE
# ==========================================================

import keyword

def print_table(title, rows):
    print("\n" + "=" * 120)
    print(f"{title:^120}")
    print("=" * 120)
    print(f"{'Keyword':<12} | {'Category':<20} | {'Description':<35} | {'Code Example':<30} | {'Output':<15}")
    print("-" * 120)

    for row in rows:
        output = "-" if row[4] is None else str(row[4])
        print(f"{row[0]:<12} | {row[1]:<20} | {row[2]:<35} | {row[3]:<30} | {output:<15}")

    print("=" * 120)


# Get all keywords dynamically
keywords = keyword.kwlist


# ==========================================================
# KEYWORD INFORMATION (SAFE DATA - NO print() USED)
# ==========================================================
keyword_info = {
    "False": ("Literal", "Boolean false value", "False", "False"),
    "True": ("Literal", "Boolean true value", "True", "True"),
    "None": ("Literal", "Represents no value", "None", "None"),

    "and": ("Logical", "Logical AND operator", "True and False", True and False),
    "or": ("Logical", "Logical OR operator", "True or False", True or False),
    "not": ("Logical", "Logical NOT operator", "not True", not True),

    "if": ("Conditional", "Condition check", "if 5>2: print('Yes')", "Yes"),
    "elif": ("Conditional", "Else if condition", "elif condition", "-"),
    "else": ("Conditional", "Else block", "else block", "-"),

    "for": ("Loop", "For loop", "for i in range(3): print(i)", "0 1 2"),
    "while": ("Loop", "While loop", "while x<3", "-"),
    "break": ("Loop Control", "Exit loop", "break", "-"),
    "continue": ("Loop Control", "Skip iteration", "continue", "-"),
    "pass": ("Control", "Do nothing", "pass", "-"),

    "def": ("Function", "Define function", "def f(): return 1", "Function created"),
    "return": ("Function", "Return value", "return x", "-"),
    "lambda": ("Function", "Anonymous function", "lambda x: x+1", "-"),

    "class": ("OOP", "Define class", "class A:", "Class created"),

    "try": ("Exception", "Try block", "try:", "-"),
    "except": ("Exception", "Handle error", "except:", "-"),
    "finally": ("Exception", "Always runs", "finally:", "-"),
    "raise": ("Exception", "Raise error", "raise ValueError", "-"),

    "import": ("Module", "Import module", "import math", "-"),
    "from": ("Module", "Import specific", "from math import sqrt", "-"),
    "as": ("Module", "Alias name", "import numpy as np", "-"),

    "with": ("Context", "Resource management", "with open()", "-"),

    "global": ("Scope", "Global variable", "global x", "-"),
    "nonlocal": ("Scope", "Outer scope variable", "nonlocal x", "-"),

    "in": ("Membership", "Check presence", "'a' in 'apple'", 'a' in 'apple'),
    "is": ("Identity", "Same object check", "x is y", "-"),

    "yield": ("Generator", "Yield value", "yield x", "-"),

    "assert": ("Debug", "Check condition", "assert x>0", "-"),

    "del": ("Memory", "Delete variable", "del x", "-"),
}


# ==========================================================
# BUILD TABLE
# ==========================================================
rows = []

for kw in keywords:
    if kw in keyword_info:
        category, desc, code, output = keyword_info[kw]
    else:
        category, desc, code, output = ("General", "Reserved keyword", "-", "-")

    rows.append((kw, category, desc, code, output))


# ==========================================================
# DISPLAY
# ==========================================================
print_table("PYTHON KEYWORDS COMPLETE LIST", rows)


# ==========================================================
# SUMMARY
# ==========================================================
print("\n SUMMARY")
print(f"Total Keywords: {len(keywords)}")
print("✔ All keywords included")
