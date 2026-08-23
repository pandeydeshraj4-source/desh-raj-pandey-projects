def find_leap_year(y):
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        print("it's a leap year")
    else:
        print("it's not a leap year")
       
find_leap_year(2025)

#USING MATCH CASE 
y = int(input("enter year: "))

match y%4 == 0 and y%100 != 0 or y%400 == 0:
    case True:
        print("its a leap year")
    case _:
        print("not a leap year")

