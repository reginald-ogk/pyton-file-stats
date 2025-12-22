total = 0
count = 0

while True:
    user_input = input("Enter a number to add (0 to stop): ")

    if not user_input.isdigit():
        print("Please enter a valid whole number.")
        continue

    number = int(user_input)
    if number == 0:
        break

    total += number
    count += 1
    print(f"The total sum is: {total}")
    print(f"Numbers entered so far: {count}")

print(f"Final total is: {total}")