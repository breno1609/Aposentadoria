#HOMENS = 65 ANOS + 15 DE CONTRIBUIÇÃO
#MULHERES = 60 + 12 DE CONTRIBUIÇÃO
print("Aposentadoria: Apto ou Inapto!")
print("------------------------------")

sexo = input("Informe o seu Sexo: H para Homem e M para Mulher: ")

if sexo == "H":
    idade = int(input("Informe a sua idade: "))
    servico = float(input("Informe o seu tempo de Serviço de Carteira Assinada: "))
    if idade >= 65 and servico >= 15:
        print("Você já está Apto a receber a aposentadoria! Entre em contato com a Equipe Responsável.")
    elif idade >= 65 and servico < 15:
        tempo_servico = 15 - servico
        print(f"Inapto! Ainda faltam {tempo_servico} anos de contribução. Complete o tempo de serviço minimo de Carteira Assinada, para dar entrada na aposentadoria.")
    elif idade < 65 and servico > 15:
        idade_H = 65 - idade
        print(f"Inapto! Aguarde a idade correta, ainda faltam {idade_H} anos, para você se aposentar.")
    else:
        idade_H = 65 - idade
        tempo_servico = 15 - servico
        print(f"Inapto! Ainda faltam {idade_H} anos e {tempo_servico} anos de contribuição.")

elif sexo == "M":
    idade = int(input("Informe a sua idade: "))
    servico = float(input("Informe o seu tempo de Serviço de Carteira Assinada: "))
    if idade >= 60 and servico >= 12:
        print("Você já está Apto a receber a aposentadoria! Entre em contato com a Equipe Responsável.")
    elif idade >=65 and servico <12:
        tempo_servico = 12 - servico
        print(f"Inapto! Ainda faltam {tempo_servico} anos de contribução. Complete o tempo de serviço minimo de Carteira Assinada, para dar entrada na aposentadoria.")
    elif idade <60 and servico >12:
        idade_F = 60 - idade
        print(f"Inapto! Aguarde a idade correta, ainda faltam {idade_F} anos, para você se aposentar.")
    else:
        idade_F = 60 - idade
        tempo_servico = 12 - servico
        print(f"Inapto! Ainda faltam {idade_F} anos e {tempo_servico} anos de contribuição.")

else:
    breakpoint("Escolha H ou F, para poder continuar!")
