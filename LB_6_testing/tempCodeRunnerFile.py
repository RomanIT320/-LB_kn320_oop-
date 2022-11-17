year = input('Введіть свій рік народження -> ')
assert year.isdigit(), f'Ви впевнені що це "{year}" число ?)'
age = 2022 - int(year)

pib = input(
    'Введіть своє імя 20')

list = pib.split()
for item in list:
    assert item.istitle(), f'Схоже ви поитлтся з "{item}" такого не може бути '

print(f'Вітаю {pib}, вам20 {age} рочків )))')