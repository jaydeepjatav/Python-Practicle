#Define the year
year=int(input("Enter a year :"))

#condition for leap year
if(year%400==0)or(year%100!=0)and(year%4==0):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
