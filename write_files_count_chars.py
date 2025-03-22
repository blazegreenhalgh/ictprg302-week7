

# Use the code snippets above to create a program that performs the following:
# ●	Reads the contents of the romeojuliet.txt file
# ●	Searches for all occurrences of the lower case letter ‘a’
# ●	Appends the text file with a message at the bottom in the following format:
#
# Letter: a
# Occurrences: 33


user_file = input("File to be checked (romeojuliet.txt): ").lower()
user_letter_input = input("Letter to be counted: ")

caps_sensitive = input("Caps sensitive? ").lower()

if caps_sensitive[0] == 'y':
    caps_sensitive = True
else:
    caps_sensitive = False


with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()

def letter_counter(caps, letter):
    if caps:
        letter_count = file_read.count(letter)
    else:
        letter_upper = letter.upper()
        letter_lower = letter.lower()
        letter_count = file_read.count(letter_upper)
        letter_count += file_read.count(letter_lower)

    return letter_count

total_count = letter_counter(caps_sensitive, user_letter_input)


with open(f"sources/{user_file}", "a") as file:
    if caps_sensitive:
        file.write(f"\n Letter: {user_letter_input} - Total Occurrences: {total_count} ({"Lowercase" if user_letter_input.islower() else "Uppercase"})")
    else:
        file.write(f"\n Letter: {user_letter_input} - Total Occurrences: {total_count} (All)")

with open(f"sources/{user_file}", "r") as file:
    file_read = file.read()

print(file_read)