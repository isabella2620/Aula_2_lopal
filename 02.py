pessoa = input("Estudante ou normal: ")
dia_semana = input("Qual o dia da semana: ")
sala = input("A sala é vip ou comum: ")

pessoa = "estudante"
dia_semana = "terca"
sala = "comum"
valor1 = 70
valor2 = 35

if pessoa == "estudante" and dia_semana == "terça" and sala == "comum":
   situacao = "Ingresso com desconto: 35,00"
elif pessoa == "normal" and dia_semana == "segunda"or"quarta"or"quinta"or"sexta"or"sabado"or"domingo" and sala == "vip":
    situacao = "Valor integral: 70,00"



print (f"Pessoa: {pessoa}")
print (f"Dia da semana: {dia_semana}")
print (f"Sala: {sala}")
print (f"Situação: {situacao}")


