print(3*'---', 'Answer 5.3', 3*'---')

alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points!')

print()

alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points!')

print()


print(3*'---', 'Answer 5.4', 3*'---')

alien_color = 'green'

if alien_color == 'green':
    print('You just earned 5 points for shooting the alien!')
else:
    print('You just earned 10 points!')

print()

alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points for shooting the alien!')
else:
    print('You just earned 10 points!')

print()


print(3*'---', 'Answer 5.5', 3*'---')

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')

print()

alien_color = 'yellow'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')

print()

alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')

print()


print(3*'---', 'Answer 5.6', 3*'---')

age = 18

if age < 2:
    print('This person is a baby.')
elif age < 4:
    print('This person is a toddler.')
elif age < 13:
    print('This person is a kid.')
elif age < 20:
    print('This person is a teenager.')
elif age < 65:
    print('This person is an adult.')
else:
    print('This person is an elder.')

print()


print(3*'---', 'Answer 5.7', 3*'---')

favorite_fruits = ['Strawberry', 'Mango', 'Grape']

if 'Strawberry' in favorite_fruits:
    print('You really like strawberries!')

if 'Mango' in favorite_fruits:
    print('You really like mangoes!')

if 'Grape' in favorite_fruits:
    print('You really like grapes!')

if 'Pineapple' in favorite_fruits:
    print('You really like pineapples!')

if 'Banana' in favorite_fruits:
    print('You really like bananas!')

print()


print(3*'---', 'Answer 5.8', 3*'---')

users = ['Maria', 'John', 'Anna', 'Carlos', 'admin']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')

print()


print(3*'---', 'Answer 5.9', 3*'---')

users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('We need to find some users!')

print()


print(3*'---', 'Answer 5.10', 3*'---')

current_users = ['Maria', 'John', 'Anna', 'Carlos', 'Peter']

new_users = ['Maria', 'Lucas', 'ANNA', 'Beatrice', 'Rafael']

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} is already being used. Please choose another username.')
    else:
        print(f'{new_user} is available.')

print()


print(3*'---', 'Answer 5.11', 3*'---')

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')

print()


print(3*'---', 'Answer 5.12', 3*'---')

# The conditional tests from the previous exercises
# were reviewed and properly formatted.

age = 18

if age >= 18:
    print('You are an adult.')

print()


print(3*'---', 'Answer 5.13', 3*'---')

# Program ideas:
#
# - A simple choice-based game.
# - A study organizer.
# - A habit tracker.
# - A program to analyze college grades.
# - A simple expense tracker.