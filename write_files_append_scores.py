file = open("sources/players.txt", "a")
file.write("\nDragonShark")
file.close()


# Use the code snippets above to create a program that performs the following:
#
# Prompts the user to enter their latest score
# Adds a new score entry to the end of the scores.txt file using the format shown below:
#
# 10293 recorded at: 30-04-2020 14:49:57


import datetime
current_time = datetime.datetime.now()
timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")

with open("sources/scores.txt", "a") as scores:
    score = input("Latest score: ")
    scores.write(f"\n{score} recorded at: {timestamp}")