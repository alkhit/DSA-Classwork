def is_leap(year: int) -> bool:
    leap = False


    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap

year = int(input("Enter a year: "))
print(is_leap(year))
