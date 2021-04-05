import random
list = []
list.append('You will sink with the Titanic')
list.append('You shall be rich')
list.append('You will be stuck in the Github Artic Code Vault')
list.append('You shall never die')
list.append('The dark will come over you')
list.append('It will always rain from now on')
list.append('You will have 100 children')
list.append('You will be a nerd at coding')
list.append('You shall be happy')
list.append('Your favorite thing will break')
print('Welcome to the Hut of Fortune')
input('What is your age? ')
print('Ok')
input('What is your name? ')
print('Thanks')
print('Your future is...')
print(random.choice(list))
answer = input('Do you want to play again?')
while answer == 'Yes' or answer == 'yes' or answer == 'y' or answer == 'Y': 
    print('Your future is...')
    print(random.choice(list))
    answer = input('Do you want to play again?')
if answer == 'No' or answer == 'no' or answer == 'n' or answer == 'N':
    print('Bye, you shall be riddled')
else:
    print('Error this is not a valid entry')