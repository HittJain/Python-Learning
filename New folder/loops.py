# ==============================
# PYTHON LOOPS COMPLETE PROGRAM
# ==============================

def print_table(title, rows):
    print("=" * 150)
    print(f"{title:^150}")
    print("=" * 150)
    print(f"{'Loop Type':<20} | {'Category':<15} | {'Description':<40} | {'Code Example':<40} | {'Output':<20}")
    print("-" * 150)

    for row in rows:
        row = [str(item) if item is not None else "" for item in row]
        print(f"{row[0]:<20} | {row[1]:<15} | {row[2]:<40} | {row[3]:<40} | {row[4]:<20}")

    print("=" * 150)


# ==============================
# TABLE DATA
# ==============================

rows = [
    ["while", "Conditional", "Runs while condition is True", "while i<=3", "1 2 3"],
    ["for", "Iteration", "Iterates over sequence", "for i in range()", "0 1 2"],
    ["nested loops", "Control Flow", "Loop inside loop", "for i:\n for j:", "(i,j)"],
    ["break", "Control Flow", "Stops loop early", "if i==3: break", "0 1 2"],
    ["continue", "Control Flow", "Skips iteration", "if i==2: continue", "0 1 3 4"],
    ["pass", "Placeholder", "Does nothing", "pass", "No output"],
    ["else", "Control Flow", "Runs after loop ends", "for...else", "Done"],
    ["infinite while", "Special", "Runs forever", "while True", "Controlled stop"],
    ["range()", "Utility", "Generates numbers", "range(1,5)", "1..4"],
    ["enumerate()", "Utility", "Index + value", "enumerate(list)", "(i,val)"],
    ["zip()", "Utility", "Parallel iteration", "zip(a,b)", "(x,y)"]
]

# Print table
print_table("PYTHON LOOPS COMPLETE TABLE", rows)


# ==============================
# EXAMPLES SECTION
# ==============================

print("\n\n================ EXAMPLES =================\n")

# 1. WHILE LOOP
print("1. WHILE LOOP:")
i = 1
while i <= 3:
    print(i, end=" ")
    i += 1
print("\n")

# 2. FOR LOOP
print("2. FOR LOOP:")
for i in range(3):
    print(i, end=" ")
print("\n")

# 3. NESTED LOOP
print("3. NESTED LOOP:")
for i in range(2):
    for j in range(2):
        print(f"({i},{j})", end=" ")
print("\n")

# 4. BREAK
print("4. BREAK:")
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
print("\n")

# 5. CONTINUE
print("5. CONTINUE:")
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
print("\n")

# 6. PASS
print("6. PASS:")
for i in range(3):
    pass
print("Loop executed (no output inside loop)\n")

# 7. ELSE WITH LOOP
print("7. ELSE WITH LOOP:")
for i in range(3):
    print(i, end=" ")
else:
    print("Done")
print()

# 8. INFINITE LOOP (CONTROLLED)
print("\n8. INFINITE LOOP (STOPPED):")
count = 0
while True:
    print("Run", count)
    count += 1
    if count == 1:
        break

# 9. RANGE
print("\n9. RANGE():")
for i in range(1, 5):
    print(i, end=" ")
print("\n")

# 10. ENUMERATE
print("10. ENUMERATE():")
fruits = ["apple", "banana"]
for i, v in enumerate(fruits):
    print(i, v)

# 11. ZIP
print("\n11. ZIP():")
a = [1, 2]
b = [3, 4]
for x, y in zip(a, b):
    print(x, y)

print("\n============= END OF PROGRAM =============")