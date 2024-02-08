day = int(input("Day : "))
month = int(input("Month : "))
year = int(input("Year : "))

#Feb 28 unless leap year is true it will be 29
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    Feb = 29
else:
    Feb = 28

last_day = [31,Feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# If it's the last day of the month
if day == last_day[month - 1]:
    # If it's December go next year and set month to Jan
    if month == 12:
        year += 1
        month = 1
    else: #go next month and set dat to day one
        month += 1
    day = 1
else: #just go next day
    day += 1

print(f"Day : {day} Month : {month} Year : {year}")
