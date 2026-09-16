print(3*'---', 'Answer 6.1', 3*'---')

pessoa = {
    'first_name': 'Maria',
    'last_name': 'Alves',
    'age': 18,
    'city': 'São Bernardo'
}

print(f"Primeiro nome: {pessoa['first_name']}")
print(f"Sobrenome: {pessoa['last_name']}")
print(f"Idade: {pessoa['age']}")
print(f"Cidade: {pessoa['city']}")

print()


print(3*'---', 'Answer 6.2', 3*'---')

numeros_favoritos = {
    'Maria': 7,
    'Ana': 3,
    'João': 10,
    'Carlos': 5,
    'Beatriz': 8
}

for nome, numero in numeros_favoritos.items():
    print(f'{nome}: {numero}')

print()


print(3*'---', 'Answer 6.3', 3*'---')

glossario = {
    'variável': 'Um espaço usado para armazenar um valor.',
    'lista': 'Uma coleção de valores que pode armazenar vários itens.',
    'dicionário': 'Uma coleção de pares chave-valor.',
    'laço': 'Uma estrutura usada para repetir um bloco de código.',
    'função': 'Um bloco de código criado para realizar uma tarefa específica.'
}

for palavra, significado in glossario.items():
    print(f'{palavra.title()}:\n\t{significado}\n')


print(3*'---', 'Answer 6.4', 3*'---')

glossario = {
    'variável': 'Um espaço usado para armazenar um valor.',
    'lista': 'Uma coleção de valores que pode armazenar vários itens.',
    'dicionário': 'Uma coleção de pares chave-valor.',
    'laço': 'Uma estrutura usada para repetir um bloco de código.',
    'função': 'Um bloco de código criado para realizar uma tarefa específica.',
    'string': 'Um tipo de dado usado para representar textos.',
    'inteiro': 'Um número que não possui casas decimais.',
    'booleano': 'Um tipo de dado que pode ter os valores True ou False.',
    'tupla': 'Uma coleção de valores que não pode ser alterada.',
    'comentário': 'Um texto no código usado para explicar o que ele faz.'
}

for palavra, significado in glossario.items():
    print(f'{palavra.title()}:\n\t{significado}\n')


print(3*'---', 'Answer 6.5', 3*'---')

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'ganges': 'índia'
}

print('Rios e países:')
for rio, pais in rios.items():
    print(f'O {rio.title()} corre pelo {pais.title()}.')

print()

print('Rios:')
for rio in rios.keys():
    print(rio.title())

print()

print('Países:')
for pais in rios.values():
    print(pais.title())

print()


print(3*'---', 'Answer 6.6', 3*'---')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

pessoas_enquete = ['jen', 'sarah', 'maria', 'ana', 'phil', 'carlos']

for pessoa in pessoas_enquete:
    if pessoa in favorite_languages:
        print(f'Obrigado, {pessoa.title()}, por responder à enquete!')
    else:
        print(f'{pessoa.title()}, participe da nossa enquete sobre linguagem favorita!')

print(3*'---', 'Answer 6.7', 3*'---')

pessoa1 = {
    'first_name': 'Maria',
    'last_name': 'Alves',
    'age': 18,
    'city': 'São Bernardo'
}

pessoa2 = {
    'first_name': 'Ana',
    'last_name': 'Silva',
    'age': 20,
    'city': 'Parnaíba'
}

pessoa3 = {
    'first_name': 'João',
    'last_name': 'Santos',
    'age': 22,
    'city': 'Teresina'
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print(f"Primeiro nome: {pessoa['first_name']}")
    print(f"Sobrenome: {pessoa['last_name']}")
    print(f"Idade: {pessoa['age']}")
    print(f"Cidade: {pessoa['city']}")
    print()


print(3*'---', 'Answer 6.8', 3*'---')

gato = {
    'tipo': 'gato',
    'dono': 'Maria'
}

cachorro = {
    'tipo': 'cachorro',
    'dono': 'João'
}

coelho = {
    'tipo': 'coelho',
    'dono': 'Ana'
}

pets = [gato, cachorro, coelho]

for pet in pets:
    print(f"Tipo do animal: {pet['tipo']}")
    print(f"Dono: {pet['dono']}")
    print()


print(3*'---', 'Answer 6.9', 3*'---')

favorite_places = {
    'Maria': ['Paris', 'Tóquio', 'Londres'],
    'Ana': ['Nova York', 'Roma'],
    'João': ['Rio de Janeiro', 'São Paulo', 'Salvador']
}

for pessoa, lugares in favorite_places.items():
    print(f'{pessoa}:')
    for lugar in lugares:
        print(f'\t{lugar}')
    print()


print(3*'---', 'Answer 6.10', 3*'---')

numeros_favoritos = {
    'Maria': [7, 18, 21],
    'Ana': [3, 10],
    'João': [5, 15, 20],
    'Carlos': [8],
    'Beatriz': [4, 12]
}

for nome, numeros in numeros_favoritos.items():
    print(f'{nome}:')
    for numero in numeros:
        print(f'\t{numero}')
    print()


print(3*'---', 'Answer 6.11', 3*'---')

cities = {
    'Paris': {
        'country': 'França',
        'population': '2,1 milhões',
        'fact': 'É conhecida pela Torre Eiffel.'
    },

    'Tóquio': {
        'country': 'Japão',
        'population': '14 milhões',
        'fact': 'É a capital do Japão.'
    },

    'Nova York': {
        'country': 'Estados Unidos',
        'population': '8,3 milhões',
        'fact': 'É conhecida pela Estátua da Liberdade.'
    }
}

for cidade, informacoes in cities.items():
    print(f'Cidade: {cidade}')
    print(f"País: {informacoes['country']}")
    print(f"População: {informacoes['population']}")
    print(f"Fato: {informacoes['fact']}")
    print()


print(3*'---', 'Answer 6.12', 3*'---')

pessoa = {
    'first_name': 'Maria',
    'last_name': 'Alves',
    'age': 18,
    'city': 'São Bernardo',
    'course': 'Análise e Desenvolvimento de Sistemas',
    'favorite_language': 'Python'
}

print(f"Nome completo: {pessoa['first_name']} {pessoa['last_name']}")
print(f"Idade: {pessoa['age']}")
print(f"Cidade: {pessoa['city']}")
print(f"Curso: {pessoa['course']}")
print(f"Linguagem favorita: {pessoa['favorite_language']}")