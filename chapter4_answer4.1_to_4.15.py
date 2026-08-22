print(3*'---', 'Answer 4.1 and 4.2', 3*'---')

pizzas = ['Quatro queijos', 'Calabresa', 'Mussarela']

print(pizzas)

for favorites_pizzas in pizzas:
    print(f'Eu gosto de pizza de {favorites_pizzas}')
print('Na verdade, gosto de qualquer sabor... menos pizza doce... ou havaiana\n')

roedores = ['Hamster', 'Preá', 'Twisted']

print(roedores)
for pet in roedores:
    print(f'Um {pet} daria um ótimo animal de estimação.')
print('Qualquer um desses animais seria um ótimo animal de estimação!\n')

print(3*'---', 'Answer 4.3 and 4.12', 3*'---')
print('Contando até 20')
for num in range(1, 21):
    print(num)

print()

print('Até 1000')
nums = [nums for nums in range(1, 1001)]
print(nums)
print(f'Soma: {sum(nums)}')
print(f'Máximo: {max(nums)}')
print(f'Mínimo: {min(nums)} \n')

impar = list(range(1, 21, 2))
print(f'Ímpares: {impar}')

multiplo_3 = []
for valor in range(3, 31):
    if valor % 3 == 0:
        multiplo_3.append(valor)
print(f'Múltiplos de 3: {multiplo_3}')

# cubos = []

# for cubo in range(1 ,11):

#    cubos.append(cubo**3)

#print(f'Cubos: {cubos}')

cubos = [cubo**3 for cubo in range(1, 11)]
print(f'Cubos: {cubos}')
print(f'\tOs três primeiros itens da lista são: {cubos[:3]}')
print(f'\tOs três itens do meio são: {cubos[4:7]}')
print(f'\tOs três últimos itens são: {cubos[7:10]}')

print()

friend_pizzas = pizzas.copy()
pizzas.append('Lombo')
friend_pizzas.append('Vegana')

#4.12
#for my_pizzas in pizzas:
    #for my_friend in friend_pizzas:
    #print(f'Minhas pizzas favoritas são: {my_pizzas}')
    #print(f'\nAs pizzas favoritas do meu amigo são: {my_friend}')


print('Minhas pizzas favoritas são:')
for my_pizza in pizzas:
    print(my_pizza)

print('\nAs pizzas favoritas do meu amigo são:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)

print()

print('Menu:')
buffet = (
'Panquecas de carne',
'Lasanha',
'Macarrão ao molho pesto',
'Gelato',
'Tiramisu')

for menu in buffet:
    print(menu)

print()

print('New Menu:')
buffet = (
'Panquecas de carne',
'Lasanha',
'Macarrão ao molho pesto',
'Panna Cotta',
'Cannoli')

for new_menu in buffet:
    print(new_menu)