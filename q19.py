st = input("Enter a string: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
result = ""
for char in st:
    if char not in punctuations:
        result += char
print("String without punctuations:", result)
