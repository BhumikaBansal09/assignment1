st= input("Enter a string to write to a text file: ")
with open('output.txt', 'w') as file:
    file.write(st)

print("String written to output.txt")
