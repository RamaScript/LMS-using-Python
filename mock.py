name = input("entrt your name  :")
count = 0
temp = list(name)
for i in temp : 
    for j in temp:
        if(i==j):
            count += 1
            temp.remove(j)
    print(f'occurance of {i} in {name} is : {count}')

# name = input("Enter your name: ")
# temp = list(name)  # Convert the string to a list for modification
# count_dict = {}  # Dictionary to store the counts of each character

# for i in temp:
#     if i in count_dict:
#         continue  # Skip if the character is already counted
#     count = temp.count(i)
#     count_dict[i] = count
#     print(f'Occurrence of {i} in {name} is: {count}')
