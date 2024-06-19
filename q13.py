from datetime import date
birth_year=int(input("Enter your birth year"))
current_year = date.today().year
print(current_year - birth_year)