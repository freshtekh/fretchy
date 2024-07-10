name = 'FRESHTEKH'
# print(len(name))
# print(name[5])
# print(name[0:5])

# function or method of a string
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())

user = input('YES OR NO: ')
print(user)
if user.upper().strip() == 'YES':
    print('YES')
elif user.lower().strip() == 'no':
    print('NO')
else:
    print('Invalid option')