# print(2 + 2)

# print("Olá mundo!")

# numeros = list(range(1,101))

# for numero in numeros:
#     if numero % 2 == 0 and numero % 4 ==0:
#         print(numero)


# for i in range(1,10):
#     if i % 2 == 1 and i % 5 == 0:
#         print (i)


# using list comprehension

# numeros = list(range(1,101))

# num_pares = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]
# #esse primeiro numero é o retorno da coisa toda, é o que vai "receber" o resultado do que vier depois
# print(num_pares)

numeros = list(range(1,101))

numeros_impares = [ numero for numero in numeros if numero % 2== 1 and numero % 4 == 1]

print(numeros_impares)
print(type(numeros_impares),type(numeros))





















