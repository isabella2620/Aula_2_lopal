pessoa = input("Digite o nome: ")
altura = float(input("Digite a altura: "))
idade = int(input("Digite a Idade: "))
autorização = input("Tem autorização (sim/nao): ")

altura >= 140
idade >= 12

if altura >= 140 and idade >= 12 or autorização == "sim":
    situação = "Acesso Liberado!"
else:
    situação = "Acesso Negado."



print (f"Nome: {pessoa}")
print (f"Idade: {idade}")
print (f"Altura: {altura}")
print (f"Situação: {situação}")
