#checking leap year
year=int(input("Enter a year:"))
if year%400==0:
    print("Leap year")
elif year%100==0:
    print("not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("not a Leap year")
