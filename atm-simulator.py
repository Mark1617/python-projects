print('Welcome to this ATM')
restart = ('Y')
chances = 3
balance = 69420.12
while chances >= 0:
    pin = input('Please type your pin into the terminal: ')
    if pin == '1234':
        while restart not in ('n', 'no', 'NO', 'N'):
            print('You entered your pin correctly')
            print('press 1 to view your balance')
            print('press 2 to withdraw money')
            print('press 3 to pay into your account')
            print('press 4 to return your card\n')
            option = input('What would you like to choose: ')
            if option == '1':
                print(f'Your balance is {balance}')
                restart = input('Would you like to go back?: ')
                if restart in ('n', 'no', 'NO', 'N'):
                    print('Thankyou')
                    break
            elif option == '2':
                withdraw = input('How much would you like to withdraw: 5, 10, 20, 50, 100 or other amount?: ')
                if withdraw == 'other amount':
                    withdraw = input('How much would you like to withdraw?: ')
                balance = balance - float(withdraw)
                print(f'Your balance is now {balance}')
                restart = input('Would you like to go back?: ')
                if restart in ('n', 'no', 'NO', 'N'):
                    print('Thankyou')
                    break
            elif option == '3':
                pay_in = input('How much would you like to pay into your account?: ')
                balance = balance + float(pay_in)
                print(f'Your balance is now {balance}')
                restart = input('Would you like to go back?: ')
                if restart in ('n', 'no', 'NO', 'N'):
                    print('Thankyou')
                    break
            elif option == '4':
                print('Your card will be returned shortly...\n')
                print('Thankyou for using this ATM')
                break
            else:
                option = input('Please enter a correct number.')
                restart = ' Y '
    elif pin != '1234':
        print(f'Incorrect PIN, please try again, you have {chances} chance left')
        chances = chances - 1
        if chances == 0:
            print('You have ran out of chances, please contact your bank to unlock your account.')
            break
                
