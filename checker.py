# write a programme that predicts a year if its a leap year

year = int(input(" Enter year:"))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    print(" is a leap year")

else:

    print("its not a leap year")




