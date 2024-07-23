# n = int(input('Enter a number : '))
# a = []
# for i in range(1,n+1):
#     if(n%i == 0):
#         a.append(i)
# print(a)

n = int(input('Enter a number : '))
rev=0

while n > 0 :
    temp = n % 10
    n = n // 10
    rev = rev + temp 
