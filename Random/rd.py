import random
import string

# Gera um numero inteiro entre A e B
# inteiro = random.randint(1, 100)

# Gera um numero aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)

# Gera um numero tipo float entre A e B
# flutuante = random.uniform(10, 20)

# Gera um numero de ponto flutuante entre  0 e 1
flutuante = random.random()

# Sorteia 2 nomes aleatorio de forma nao repetida
lista = ['Antonio', 'Allyson', 'Sammy', 'Hugo', 'Luca', 'Felps']
for i in range(10):
    sorteio = random.sample(lista, 2)
    print(sorteio)


# Gera uma senha aleatoria
letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%&*"
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
