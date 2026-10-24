"""Print multiplication tables until the user types q."""

while True:
    entry = input("Enter a whole number (or q to quit): ")
    if entry.lower() == "q":
        print("Goodbye.")
        break
    if not entry.isdigit():
        print("Please enter a whole number.")
        continue
    number = int(entry)
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
