def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month not in range(1, 13):
    return "Invalid month."
  month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year):
    month_days[2] = 29
    return month_days[month]
  else:
    return month_days[month]


is_continue = True  
#🚨 Do NOT change any of the code below 
while is_continue:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)
    is_continue = input("Want to continue? Type 'y' or 'n' ").lower()
    if is_continue == 'n':
        is_continue = False
        print("Thank you. ")
