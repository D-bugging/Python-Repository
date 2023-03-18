# A tipagem do Python é forte
# O código fonte é traduzido pelo Python para Bytecode, que é formato binário com instruções para o interpretador.
# O bytecode é multiplataforma e pode ser distribuído e executado sem fonte original

# Comentários funcionais
# #!/usr/bin/env python     - definir o interpretador que será utilizado para rodar o programa em sistema UNIX
# -*- coding: utf-8 -*-     - alterar a codificação do arquivo fonte do programa, para suportar caracteres que não fazem parte da linguagem inglesa (latin1 ou utf-8)

# Tipos do Python podem ser Mutáveis e Imutáveis
# Tipos de coleções: Lista, Tupla, Dicionário

# PyDOC é uma ferramenta de ducomentação, pode ser utilizada tanto para acessar a documentação dos módulos que acompanham o Python, quanto a documentação dos módulos de terceiros
# pydoc ./module.py
# pydoc -p 8000
# pydoc -g

# Condições
temp = 23
if temp < 0:
  print('Cold as Fuck')
elif 0 <= temp <= 20:
  print('Cold')
elif 21 <= temp <= 25:
  print('Normal')
else:
  print('HOT')

varTern = 'Hehe' if True == True else 'Haha'
print(varTern)

# Loops
s = 0
for x in range(1, 100):
  s = s + x
print(s)

for x in ['Orange', 'Juice']:
  print(x)
else:
  print('Little Juice')

s = 0
x = 1
while x < 100:
  s += x
  x += 1
else:
  print(s)

# Conversões
print("Real para inteiro ", int(3.14))
print("Inteiro para real ", float(5))
print("Calculo entre inteiro e real resulta em real ", 5.0 / 2 + 3)
print("Inteiro em outra base (base 8) ", int('20', 8))
print("Inteiro em outra base (base 16) ", int('20', 16))

# Operações com números complexos
c = 3 + 4j
print("c = ", c)
print("Parte real: ", c.real)
print("Parte imaginária: ", c.imag)
print("Conjugado: ", c.conjugate())

# Operações bit-a-bit:
# Deslocamento para esquerda (<<)
# Deslocamento para direitra (>>)
# E bit-a-bit (&)
# OU bita-a-bit (|)
# OU exclusivo bit-a-bit (^)
# Inversão (~)

# String
print('Padrão'); print(u'Unicode'); print("Padrão")
print('\n'); print(r'\n'); print('\\n')
print('Concate' + 'nação')
s = 'Camel'; print('Interpolação %s => %d' % (s, len(s)))
for ch in s: print(ch)
if s.startswith('C'): print(s.upper())
print(3 * s)

# Símbolos utilizados na interpolação:
  # %s - string
  # %d - inteiro
  # %o - octal
  # %x - hexadecimal
  # %f - real
  # %e - real exponencial
  # %% - sinal de porcentagem

print('Agora são %02d:%02d' % (16, 30))
print('Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))
print('Decimal: %d, Octal: %o, Hexadecimal %x' % (10, 10, 10))


musicians = [('Page', 'guitarrista', 'Led Zeppelin'), ('Fripp', 'guitarrista', 'King Crimson')]

# Parâmetros identificados pela ordem
msg = '{0} é {1} do {2}'
for name, function, band in musicians:
  print(msg.format(name, function, band))

# Parâmetros identificados pelo nome
msg = '{saudacao}, são {hour:02d}:{minute:02d}'
print(msg.format(saudacao='Good Morning', hour=7, minute=30))

print('Python'[::-1])

# Dicionário
dictionary = {'name': 'Shirley Manson', 'band': 'Garbage'}
print(dictionary['name'])
dictionary['album'] = 'Version 2.0'
del dictionary['album']
# items = dictionary.items()
# keys = dictionary.keys()
# values = dictionary.values()

# Progs e seus albuns
progs = {'Yes': ['Close to the Edge', 'Fragile'], 'Genesis': ['Foxtrot', 'The Nursery Crime'], 'ELP': ['Brain Salad Surgery']}
progs['King Crimson'] = ['Red', 'Discipline']

# Retorna uma lista de tuplas com a chave e valor
for prog, albuns in progs.items():
  print(prog, '=>', albuns)

#if progs.has_key('ELP'):
#  del progs['ELP']

# Argumentos
# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionário)
def func(*args, **kargs):
  print(args)
  print(kargs)

func('peso', 10, unidade='k')