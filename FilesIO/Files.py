import sys

# Cria um objeto do tipo file
temp = open('temp.txt', 'w')

# Escrevendo no arquivo
for i in range(100):
  temp.write('%03d\n' %i)

# Fechando
temp.close()

temp = open('temp.txt')

# Escrevendo no terminal
for i in temp:
  # Escrever em sys.stdout envia o texto para a saída padrão
  sys.stdout.write(i)

temp.close()
