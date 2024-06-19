l = []

print("Enter multiple lines of input (enter an empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    l.append(line)


for line in l:
    print(line)
