#strings

palavra = 'termodinâmica' 
print palavra

primeiraLetra = palavra[0]
print primeiraLetra

primeiraLetraVezesCinco = 5 * palavra[0]
print primeiraLetraVezesCinco

intervalo = palavra[9:12]
print intervalo

intervalo2 = palavra[9:]
print intervalo2

intervalo3 = palavra[0:9]
print intervalo3

intervalo4 = palavra[:9]
print intervalo4

intervalo5 = palavra[:]
print intervalo5

intervalo6 = palavra[1:8]
print intervalo6

intervalo7 = palavra[1:8:2]
print intervalo7

intervalo8 = palavra[1:8:3]
print intervalo8

intervalo9 = palavra[7:0:-1]
print intervalo9

intervalo10 = palavra[7::-1]
print intervalo10

intervalo11 = palavra[:4:-2]
print intervalo11

intervalo12 = palavra[::-1]
print intervalo12

palindromo = 'assa';
print palindromo[::-1]

palavra = palavra + ' aplicada'
print palavra

print palavra[14:]

print len(palavra)

a = 'Boa tarde!'
print a

a = 'Nova'
print a

# NAO PERMITIDO ->    a[0] = 'T'   STRINGS SAO IMUTAVEIS

#listas

lista = [1, 2, 3]
print lista

print lista[0]

print lista[2]

print lista[0] + lista[2]

lista = lista + [4]

print lista

lista = lista + [0, 0, 0]
print lista

print lista[-1]

print lista[2:-2]

print len(lista)

lista[0] = 'zero'
print lista

lista[1] = lista[1] + lista[2]
print lista

lista[2] = lista[0]
print lista

linha1 = [1,2,3]
linha2 = [4,5,6]
linha3 = [7,8,9]

matriz = [linha1,linha2,linha3]
print matriz

print matriz[1]

print matriz[1][1]

#tuplas

tupla = (1,2,3)
print tupla

# NAO PERMITIDO ->        tupla[0] = 2        TUPLAS SAO IMUTAVEIS

a,b = (0),('Deu Certo?')
print a,b

a,b = b,a
print a,b

#dicionários

aurelio = {'denominação':'ilha solteira','população':23000,'renda':1500}
print aurelio

aurelio['votação'] = 'turismo'
print aurelio

print aurelio['renda']
print aurelio['denominação']

aurelio['renda'] = aurelio['renda'] + 200
print aurelio['renda']

print aurelio.keys()

print aurelio.has_key('idade')
aurelio['idade'] = 24 

print aurelio.has_key('idade')
print aurelio['idade']

print aurelio.items()