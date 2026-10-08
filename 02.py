pessoa = input("Estudante ou normal: ")
dia_semana = input("Qual o dia da semana: ")
sala = input("A sala é vip ou comum: ")

if pessoa == "estudante" and dia_semana == "terça" and sala == "comum":
   situacao = "Ingresso com desconto: 35,00"
else:
    situacao = "Valor integral: 70,00"



print (f"Pessoa: {pessoa}")
print (f"Dia da semana: {dia_semana}")
print (f"Sala: {sala}")
print (f"Situação: {situacao}")


