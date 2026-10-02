renda_mensal = int(input("Digite sua renda mensal: "))
score_credito = int(input("Digite o seu score de crédito: "))
bens_garantia = str(input("Você possui algum ben como garantia: "))
historico_inadimplencia = str(input("Você possui historico de inadimplência: "))

if renda_mensal >= 3000 and score_credito >= 600 and historico_inadimplencia == "não":
    print("Empréstimo Aprovado!")

elif historico_inadimplencia == "sim" and bens_garantia == "sim":
    print("Empréstimo aprovado") 

else:
    print("Empréstimo negado!")   