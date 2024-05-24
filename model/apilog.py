from requests import get
treatment = input('Вид операции (0 - Хирургическая, 1 - Нефролитотомия): ')
stone_size = input('Размер камня (0 - Большой, 1 - Маленький): ')
print(get(f'http://127.0.0.1:5000/apilog', json={'treatment': treatment, 'stone_size': stone_size}).json())
