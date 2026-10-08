renda_mensal = float(input("Digite sua renda mensal: "))
score = int(input("Digite o seu score de crédito: "))
bens_garantia = input("Você possui algum ben como garantia: ")
historico = input("Você possui historico de inadimplência: ")

if renda_mensal >= 3000 and score >= 600 and historico == "não":
    print("Empréstimo Aprovado!")

elif historico == "sim" and bens_garantia == "sim":
    print("Empréstimo aprovado!") 

else:
    print("Empréstimo negado!")   
