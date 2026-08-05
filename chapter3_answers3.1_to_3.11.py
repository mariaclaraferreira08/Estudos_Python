import emoji
import random

print(3*'---', 'Answer 3.1 and 3.3', 3*'---')
names = ['Mary', 'John', 'Anthony', 'Nikolai']
print(f'Name List: {names}')
print(f"Hi, i'm {random.choices(names)}")
#print(f"Hi, i'm {names[1]}, nice to meet you!")
#print(f"Hi, i'm {names[2]}, nice to meet you!")
#print(f"Hi, i'm {names[3]}, nice to meet you!")
print('\n')
cars = ['Lamborghini Aventador', 'Pagani', 'Mazda Miata',]
print(f'Cars list: {cars}')
print(emoji.emojize(f'I would like to own a {random.choices(cars)} :smiling_face_with_sunglasses:'))
print('\n')

print(3*'---', 'Answer 3.4 and 3.7', 3*'---')
#3.4
guests_List=['Jane Doe','John Doe','Richard Roe']
print(f'''
Dear {guests_List[0]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[1]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[2]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')

wontCome = guests_List.pop(2)
print(f'''
{wontCome} Answer: Thank you for the invitation, but will not be able to attend. 
In my place, i will send my daughter Eleonor \n''')

#3.5
#New guest = Eleonor
guests_List.append('Eleonor Roe')
print(f'New invites: {guests_List}\n')

    #New Invites
print(f'''
Dear {guests_List[0]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[1]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[2]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')

#New guest at dinner
#3.6
print(emoji.emojize('''
Me, thinking: :thinking_face: Hmm, I have a feeling I'm forgetting someone else... -
(thinking for a while longer until finally remembering) - :face_screaming_in_fear:
(Writing a new guest list :writing_hand:  (again...) \n'''))
    #New Invites 2.0
guests_List.insert(0,'Alvin Jones')
guests_List.insert(2, 'Simon Smith')
guests_List.append('Theodore Romanov')

print(f'New invites:{guests_List}')

print(f'''
Dear {guests_List[0]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[1]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[2]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[3]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[4]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')
print(f'''
Dear {guests_List[5]},
I have the honor of inviting you to dinner at my home -
789 Cherry Blossom Street, at 8:30PM.
I look forward to you presence.
''')

#3.7
print('~~~'*3,'The dinner was canceled', '~~~'*3)
removedGuest_1 = guests_List.pop()
removedGuest_2 = guests_List.pop()
removedGuest_3 = guests_List.pop()
removedGuest_4 = guests_List.pop()
print(f'''Dear {removedGuest_1}, For personal reasons, dinner has been canceled. Sorry for the inconvenience\n''')
print(f'''Dear {removedGuest_2}, For personal reasons, dinner has been canceled. Sorry for the inconvenience\n''')
print(f'''Dear {removedGuest_3}, For personal reasons, dinner has been canceled. Sorry for the inconvenience\n''')
print(f'''Dear {removedGuest_4}, For personal reasons, dinner has been canceled. Sorry for the inconvenience\n''')
    #Close friends
print('~~~'*3,'...But', '~~~'*3)
print(f"""
{guests_List[0]}, due to some reasons that aren't worth mentioning
I’ve reduced the guest list to just my closest ones. Therefore, I look forward to your presence.""")
print(f"""
{guests_List[1]}, due to some reasons that aren't worth mentioning
I’ve reduced the guest list to just my closest ones. Therefore, I look forward to your presence.""")

del guests_List[0]
del guests_List[0]
print(guests_List)

print(3*'---', 'Answer 3.8 and 3.11', 3*'---')

# 3.8
countryDreams = ['Brazil', 'Shangai', 'South Korea', 'Italy', 'Russian']
print(f'These are some of the countries I want to visit someday: {countryDreams}\n')
print(f'Normal order: {countryDreams}')
print(f'\tIn alphabet order: {sorted(countryDreams)}')
print(f'\tIn alphabet reverse order: {sorted(countryDreams,reverse=True)}')

countryDreams.reverse() # Random Order
print(f'\tRandom order: {countryDreams}')
countryDreams.reverse() # Original Order
print(f'\tOriginal order: {countryDreams}')