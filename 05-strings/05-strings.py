# Código utilizado no livro Aprenda Python Básico - Rápido e Fácil de entender, de Felipe Galvão
# Mais informações sobre o livro: http://felipegalvao.com.br/livros

# Capítulo 5: Strings

# Definindo as primeiras strings
string1 = "Oi Python"
string2 = 'Tchau Python'
print(string1)
print(string2)

# Definindo strings com aspas triplas
string_grande = '''Olá. Esta é uma string grande no Python. 
Aqui você pode usar " ou '
Caracteres são escapados como se espera.
É a terceira forma de definir uma string, apesar de não ser tão usual.... 
\t testando o TAB para finalizar'''
print(string_grande)

# Usando aspas simples com aspas duplas e vice-versa
string3 = "A cantora \033[1;30;41mSinnead O'Connor\033[m"
string4 = 'Alfredo disse "Corram aqui para ver isso!"'
print(string3)
print(string4)

# Para escapar caracteres, use a \
string5 = "Alfredo disse \"Corram aqui para ver isso!\""
string6 = 'Sinnead O\'Connor disse "Nothing compares 2 u"'
print(string5)
print(string6)

# Escapando a contrabarra \
string7 = "Estou escapando uma \\"
print(string7)

# Definindo strings raw, com um r antecedendo a mesma
string8 = r"Utilizamos \n para inserir uma nova linha na string"
print(string8)

# Inserindo variáveis em strings com f-string (caractere de formatação)
nome = "Felipe"
idade = 30
print(f"Meu nome é {nome} ")
print(f"Tenho {idade} anos")

# Inserindo e formatando decimais em strings
a = 30.46257
print("Formatando decimais: %f" % a)

print("Formatando decimais: %.2f" % a)
print("Formatando decimais: %.3f" % a)

# Inserindo múltiplos valores em uma string - 's' string; 'd' decimal ou numérico
nome = 'Felipe'
idade = 30
print("Meu nome é %s e tenho %d anos" % (nome, idade))
print('-'*20)

# Strings como listas; acessando caracteres
string9 = "Olá, meu nome é Felipe"
print(len(string9))
print(string9[0])
print(string9[3])
print(string9[21])

# Funções capitalize, upper e lower
string10 = "olá, meu NOME é Felipe"
print(string10.capitalize())
print(string10.upper())
print(string10.lower())

# Exemplo da função center()
string11 = "olá, meu nome é Felipe"
print(string11.center(50, "*"))

# Exemplo da função find
string12 = "Olá, meu nome é Felipe"
substring1 = "meu"
print(string12.find(substring1))
print('--'*3)
substring2 = "José"
print(string12.find(substring2))
print('--'*3)
print(string12.find(substring1, 7))
print(string12.find(substring1, 2))
print('--'*3)
# Funções isalnum, isalpha e isnumeric
string13 = "Felipe"
print(string13.isalnum())
print(string13.isalpha())
print(string13.isnumeric())
print('--'*3)
string14 = "1234"
print(string14.isalnum())
print(string14.isalpha())
print(string14.isnumeric())
print('--'*3)
string15 = "Felipe1234"
print(string15.isalnum())
print(string15.isalpha())
print(string15.isnumeric())
print('--'*3)
# Função len: retorna a quantidade de caracteres de uma string
string16 = "Meu nome é Felipe"
print(len(string16))
print('--'*3)
# Função replace: substitui uma parte da string por outra indicada como parâmetro
string17 = "Olá, meu nome é Felipe"
print(string17.replace("Felipe","José"))
print('--'*3)
# Funções strip, rstrip e lstrip: removem espaços nas extremidades ou à esquerda ou à direita da string
string18 = "   Olá, meu nome é Felipe      "
print(string18)
print(string18.strip()) # remove espaços antes e depois da string
print(string18.rstrip()) # remove espaços à direita da string
print(string18.lstrip()) # remove espaços à esquerda da string