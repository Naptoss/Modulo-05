import random


# Gera um numero inteiro entre A e B
# inteiro = random.randint(1, 100)

# Gera um numero aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)

# Gera um numero tipo float entre A e B
# flutuante = random.uniform(10, 20)

# Gera um numero de ponto flutuante entre  0 e 1
flutuante = random.random()

# Sorteia um nome aleatorio de forma nao repetida
lista = ['Antonio', 'Allyson', 'Sammy', 'Hugo', 'Luca', 'Felps']
for i in range(1000):
    sorteio = random.sample(lista, 2)
    print(sorteio)

print(inteiro)
print(flutuante)
