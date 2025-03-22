file = open("sources/quick.txt", "r")

quicktext = file.read()

print(quicktext)

file.close()


file_romeo = open("sources/romeojuliet.txt", "r")

print(file_romeo.read())

file_romeo.close()