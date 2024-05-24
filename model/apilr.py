from requests import get
TV = input('Телевизионная реклама: ')
radio = input('Реклама на радио: ')
newspaper = input('Реклама в газетах: ')
print(get(f'http://127.0.0.1:5000/apilr', json={'TV': TV, 'radio': radio, 'newspaper': newspaper}).json())
