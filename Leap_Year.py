def isLeapYear(Year):
  if Year % 100 ==0:
    if Year % 400 ==0:
      return "Leap year"
    else:
      return "Not a leap year"
  if Year % 2 ==0:
    return "Leap year"
  else:
    return "Not a leap year"


Input = int(input("Enter a year: "))
print(isLeapYear(Input))
