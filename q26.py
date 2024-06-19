st= input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

if st[:len(prefix)] == prefix:
    starts_with_prefix = True
else:
    starts_with_prefix = False
if st[-len(suffix):] == suffix:
    ends_with_suffix = True
else:
    ends_with_suffix = False
print(f"Does the string start with '{prefix}'? {starts_with_prefix}")
print(f"Does the string end with '{suffix}'? {ends_with_suffix}")

