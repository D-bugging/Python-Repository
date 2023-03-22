import sys
import os.path
import glob

fn = input('File name: ').strip()

if not os.path.exists(fn):
  print('Try again...')
  sys.exit()

# Numerando as linhas
for l, s in enumerate(open(fn)):
  print(l + 1, s)

# Imprime uma lista contendo linhas do arquivo
print(open('temp.txt').readlines())

# Método seek() permite ir para qualquer posição do arquivo
# Módulo IO implementa de forma separada as operações de arquivo e as rotinas de manipulação de texto

# os.path.basename()	-	retorna o componente final de um caminho
# os.path.dirname()		-	retorna um caminho sem o componente final
# os.path.exists()		-	retorna True se o caminho existe ou False se não existe
# os.path.getsize()		-	retorna o tamanho do arquivo em bytes

# Mostra uma lista de nomes de arquivos e seus respectivos tamanhos
for file in sorted(glob.glob('*.py')):
	print(file, os.path.getsize(file))

# A função glob.glob() retorna uma lista com os nomes de arquivos que atendem biblioteca padrão

# Cria um arquivo temporário
text = 'Test'
temp = os.tmpfile()

# Escreve no arquivo temporário
temp.write('Test')

# Volta para o início do arquivo
temp.seek(0)

# Mostra o conteúdo do arquivo
print(temp.read())

# Fecha o arquivo
temp.close()
