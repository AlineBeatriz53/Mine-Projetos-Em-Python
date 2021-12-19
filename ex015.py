dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km você percorreu? '))
pago = (dias * 120) + (km * 0.20)
print(f'O total a pagar será de R${pago:.2f}')
