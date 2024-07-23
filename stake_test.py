print('YOU ARE WELCOME TO FRESHTEKH\'S CASINO. GOODLUCKS! \n')
balance=int(input('initial_stake: $'))
print(f'your balance is ${balance}')

import random as rd

while True:
    cars = ['Benz', 'Toyota', 'Audi', 'Tesla', 'BYD',"Lexus"]
    Ai_choice= rd.choice(cars)
    myGuess=input('Enter your guess Benz, Toyota, Audi, Tesla, BYD, Lexus: \n')

    print(Ai_choice)

    if myGuess == Ai_choice:
        balance += 3
        print(f" Sharp\n your new balance is ${balance} keep bombing\n" )
    elif myGuess != Ai_choice:
        balance -= 3
        print(f'Wahala! your new balance is ${balance}')
        if balance <= 0:
            
            print('Do you want to keep playing?')
            keep_playing = input('yes or no: ')
            if keep_playing == 'yes':
                balance = int(input('New stake: '))
            else:
                print('Game over! How you go do your life now')
                break
    else:
        print('invalid input')
                


