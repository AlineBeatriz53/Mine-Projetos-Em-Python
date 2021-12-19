print ('====DÉFI 10====')
real = float(input('Quanto dinheiro você tem na carteira? R$'))
print('='*12)
dolar = real / 5.69
euro = real / 6.40
dolarC = real / 4.42
iene = real / 0.050
won = real / 0.0048
print(f'Com R${real:.2f} você pode comprar: \n${dolar:.2f} \nEUR{euro:.2f} \nUS${dolarC:.2f} \n¥{iene:.2f} \n₩{won:.2f}')
print('='*12)