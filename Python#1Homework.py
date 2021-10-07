month = int(input('Month: '))
year = int(input('Year: '))

months_30=[4,6,9,11]
months_31=[1,3,5,7,8,10,12]

if month in months_30:
    print(30)
elif month in months_31:
    print(31)
else:
    if year%4==0 and year%100!=0 or year%400==0:
        print(29)
    else:
        print(28)