from requests import get
treatment = input('Вид операции (0=хирургическая, 1=нефролитотомия): ')
stone_size = input('Размер камня (0=большой, 1=маленький): ')
print(get(f'http://127.0.0.1:5000/apiknn', json={'treatment': treatment, 'stone_size': stone_size}).json())