#ex.2 membership app
print("=== Membership Application ===")

fname = str(input("Please enter the applican't first name: "))
lname = str(input("Last name: "))
year, month, date = input("Your birthday (year month date): ").split()
year = int(year)
date = int(date)
bless = str(input("Your blessing: "))
age = 2020 - year
print(f"Welcome {fname}, {lname} ({year} / {month} / {date}), age {age} {bless}")
