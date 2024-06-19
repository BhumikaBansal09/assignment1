source_file = 'output.txt'
destination_file = 'destination.txt'
with open(source_file, 'r') as src:
    contents = src.read()
with open(destination_file, 'w') as dest:
    dest.write(contents)
print("content has been copied")
