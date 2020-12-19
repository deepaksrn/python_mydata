# Multiplication table for a given number
print('******** Multiplication Table ********')
a = int(input('Enter the number: '))
for i in range(1,21):
    print(a,'X',i,"=",a*i)
