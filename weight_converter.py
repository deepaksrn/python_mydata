weight = float(input("Enter your weight : "))
unit = str(input("(K)g or (L)bs : "))
if unit == "k" or unit == "K":
   print("Your weight in pounds is : ", weight * 2.2046226218)
else:
    print("Your weight in Kilo is : ", weight * 0.45359237)

print("Thank you !!")