# Função in

# o 'in' tem menor precedência que '=='

def meu_in(elemento, sequencia):
    # busca linear
    for e in sequencia:
        if e == elemento:
            return True
        
    return False

# palavra = input()

#for i in range(len(palavra) - 1):
#    if meu_in(palavra[i + 1], "aeiou"):
#        print(palavra[i])
        
nums = [10, 4, 9, -2, 8, 0, 41]
while True:
    n = int(input())
    if meu_in(n, nums): # If n in nums: -> a mesma coisa
        print(f'{n} está na lista {nums}')
    else:
        print(f'{n} NÃO está na lista {nums}')
