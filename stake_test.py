print('YOU ARE WELCOME TO FRESHTEKH\'S CASINO. GOODLUCKS! \n')
balance=int(input('initial_deposit: $'))
print(f'your balance is ${balance}\n')
print('how much do you want to stake')
stake=int(input(f'$ '))
import random as rd

while True:
    cars = ['Benz', 'Toyota', 'Audi', 'Tesla', 'BYD',"Lexus"]
    Ai_choice= rd.choice(cars)
    myGuess=input('Enter your guess Benz, Toyota, Audi, Tesla, BYD, Lexus: \n')

    print(Ai_choice)

    if myGuess == Ai_choice:
        balance +=  stake * 1.4
        print(f" Sharp\n your new balance is ${balance} keep bombing\nHow much do you want to stake" )
        stake=int(input(f'$ '))
    elif myGuess != Ai_choice:
        balance -= stake
        print(f'Wahala! your new balance is ${balance}\n How much do you want to stake')
        stake=int(input(f'$ '))
        
        if balance <= 0:

            print('Do you want to keep playing?')
            keep_playing = input('yes or no: ')
            if keep_playing == 'yes':
                balance = int(input('New Deposit: '))
            else:
                print('Game over! How you go do your life now')
                break
    else:
        print('invalid input')
