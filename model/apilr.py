from requests import get
TV = input('телевизионная реклама: ')
radio = input('реклама на радио: ')
newspaper = input('реклама в газетах: ')
print(get(f'http://127.0.0.1:5000/apilr', json={'TV': TV, 'radio': radio, 'newspaper': newspaper}).json())
