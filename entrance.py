entrance=input(' Movement detected \n welcome to SQI coding school \n Who are you? \n 1. Staff \n 2. Student \n 3. Visitor \n input:-')

if entrance == '1':
    print('Welcome to work, have a great day')
elif entrance == '2':
    payment=input("Welcome to class today, Are you fully paid? \n1. yes \n2. no \n3. no payment at all:-")
    if payment == '1':
        print('Senior man you have fully paid, enjoy your class today')
    elif payment == '2':
        print('you played sportybet with our balance abi? make sure you pay fully')
    elif payment=='3':
        print('Mr man dont even bother to touch this door')
    else:
        print('invalid selection, input 1, 2, or 3')

elif entrance=='3':
    print('welcome anonymous we are happy to meet you')
else:
    print('invalid selection, are you a thief?')

    