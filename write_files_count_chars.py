

# Use the code snippets above to create a program that performs the following:
# ●	Reads the contents of the romeojuliet.txt file
# ●	Searches for all occurrences of the lower case letter ‘a’
# ●	Appends the text file with a message at the bottom in the following format:
#
# Letter: a
# Occurrences: 33


user_file = input("File to be checked (romeojuliet.txt): ").lower()
user_letter = input("Letter to be counted: ").lower()

with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()

letter_count = file_read.count(user_letter)

with open(f"sources/{user_file}", "a") as file:
    file.write(f"\nLetter: {user_letter}")
    file.write(f"\nOccurrences: {letter_count}")

with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()

print(file_read)