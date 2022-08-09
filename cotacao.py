import requests
import json

moeda = str(input('Informe a moeda que deseja verificar a cotação, Dolar(d), Euro(e) ou Bitcoin(b): ' ))

while (moeda != 'd' and moeda != 'e' and moeda != 'b'):
    moeda = str(input('informe um valor valido'))
    
if moeda == 'd':
    moeda = 'USDBRL'
if moeda == 'e':
    moeda = 'EURBRL'
if moeda == 'b':
    moeda = 'BTCBRL'

def cotacao(moeda):
    cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = cotacao.json()
    
    resultado = cotacao[moeda]['bid']
    return 'A cotação atual da moeda {} é de R${}' .format(moeda, resultado)

print(cotacao(moeda))




