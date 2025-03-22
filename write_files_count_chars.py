

# Use the code snippets above to create a program that performs the following:
# ●	Reads the contents of the romeojuliet.txt file
# ●	Searches for all occurrences of the lower case letter ‘a’
# ●	Appends the text file with a message at the bottom in the following format:
#
# Letter: a
# Occurrences: 33


user_file = input("File to be checked (romeojuliet.txt): ").lower()

user_letter_lower = input("Letter to be counted: ").lower()
user_letter_upper = user_letter_lower.upper()

# Reviewed: This list is completely unnecessary.
user_letter = [user_letter_lower, user_letter_upper]

with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()


# Reviewed: The pop() could have just been user_letter_lower and user_letter_upper.
letter_count = file_read.count(user_letter.pop())
letter_count += file_read.count(user_letter.pop())

with open(f"sources/{user_file}", "a") as file:
    file.write(f"\nLetter: {user_letter_upper}{user_letter_lower}")
    file.write(f"\nTotal Occurrences: {letter_count}")

with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()

print(file_read)