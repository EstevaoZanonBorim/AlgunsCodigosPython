while True:
    # Variáveis e cálculo do IMC
    altura = input('Sua altura (em metros): ')
    peso = input('Seu peso (em quilos): ')
    
    # Convertendo altura e peso para float
    altura_float = float(altura)
    peso_float = float(peso)
    
    # Cálculo do IMC
    imc = peso_float / (altura_float ** 2)

    # Resultado e categoria
    resultado = f'Seu IMC é de {imc:.2f}'

    if imc < 18.5:
        categoria = "Peso baixo"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    elif 30 <= imc < 34.9:
        categoria = "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        categoria = "Obesidade grau 2"
    else:
        categoria = "Obesidade grau 3"

   
    print(f'''{resultado}.\nSua situação é: {categoria}
{30*'-'}''')