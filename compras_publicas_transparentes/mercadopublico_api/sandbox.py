import requests

#response = requests.get('http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=2097-241-SE14&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622')
response = requests.get('http://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?estado=todos&ticket=34EA724F-17C8-462E-B23B-4A92B3A2F622')
print(response.json())
