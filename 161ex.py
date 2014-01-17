from sys import argv

script, filename = argv

file = raw_input("Which file do you want to ennumerate? ")

read_file = open(file)

print read_file.read()
