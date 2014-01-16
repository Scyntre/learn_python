from sys import argv

script, filename = argv
#txt = open(filename)
txt = raw_input("Filename?: ")

txt_first = open(txt)

print txt_first.read()
txt_first.close()
print "Here's your file %r:" % filename

print "Type the next filename: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()

