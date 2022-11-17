# Звіт до роботи
## Тема: Основи python
### Мета роботи: Навчитися працювати з основними типами даних
---
### Виконання роботи
- Результати виконання завдання 1..3 :
    1. Опрацював всі типи даних;
    1. Використав вбудовані константи;
    1. Використав вбудовані функції;
    1. Використав цикли;
    1. Використав розгалуження;
    1. Створив код з помилкою;
    1. Використав контекст менеджер;
    1. Використав lambdas;
---
- Рисунки виконаних робіт:

    <!-- 1. ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/Test_program.png "test_program_1") -->1. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_1.png " ")
    2. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_2.png " ")
    3. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_3.png " ")
    4. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_4.png " ")
    5. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_5.png " ")
    6. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_6.png " ")
    7. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_7.png " ")
    8. 
    ![alt text](https://raw.githubusercontent.com/RomanIT320/LB_kn320_oop/main/pictures/LB_3_8.png " ")
    


- код який використовувся в ході роботи:
1. 
```python
a = "хай буде так"  # зміння з текстом
b = "це"
c = 1   #числова змінна
d = 2   
e = ["a", 155, 1.14, "НЕ москаль"]  # list
f = {"a": "слово", "b": 14 }    # dict
g = ("a", )     # tuple
l = {"cc", }    #set

print(a, c , b , d, '(', e ,')' ,(l, f))
```
2. 
```python
print("перша константа", False)
print("друга константа", True)
print("третя константа", None)
print("третя константа", Ellipsis)
```
3. 
```python
print(abs(-12.5), f"є рівним {abs(12.5)}")
print(chr(92))
print(bin(3))
```
4. 
```python
for i in range(4):
    print(i,)

print(" ")

letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

print(" ")

position_ = ["Чорнобаївка","Гостометель","Харків"]
katsap = ["540","452","143"]
for i in range(len(position_)):
    print(f"На позиції {position_[i]} було знищеноо {katsap[i]} кацапів")
```
5. 
```python
a = 19
b = 17
c = 18
print("О пане вам пакетик потрібно" if a > 18 else "Хлопчику яке пиво ти себе бачив")
print("О пане вам пакетик потрібно" if b > 18 else "Хлопчику яке пиво ти себе бачив")


```
6. 
```python
B = 0
try:
    print("Таке число підійде", 10/B, "?")
except Exception as e:
    print(e)
finally:
    print("Ну хай буде" if B > 0 else "Міняй")


```
7. 
```python
a = a + 1

with open("output.txt", "w") as f:
    f.write(f"Ви запустили код {a} разів")
    
with open("output.txt", "r") as f:
    for line in f:
        print(line)


    
```
8. 
```python
this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Роман', 'Нестор'))

print("")
print("А тепер те шо я набрив")
print("")

lambda_fun = lambda a, d: f'Якщо {a} помножити на {d} то получиться {a * d}'
print("Викликаю калькулятор -->", lambda_fun(13,245))
```


- результати виконання індивідуального завдання:

```text
    Результати задовільні 
```

### Висновок: 
- :question: Що зроблено в роботі;

    Було використано базові дані та функції які є вбудовані в Python.
    
- :question: Чи досягнуто мети роботи;

    Так, всі завдання виконано і протестовано успішно.
    
- :question: Які нові знання отримано;
    
    Вивчив базовий синтаксис Python та навчився використовувати нові функції.
    
- :question: Чи вдалось відповісти на всі питання задані в ході роботи;

    
     Так
    
- :question: Чи вдалося виконати всі завдання;

    
     Так
    
- :question: Чи виникли складності у виконанні завдання;

    
    Ні
    
- :question: Чи подобається такий формат здачі роботи (Feedback);

    
    Так 
    
- :question: Побажання для покращення (Suggestions);

    
    Можна додатково до офіційної документації додавати ще опис функцій з сайту [w3schools](https://www.w3schools.com/) так як там інколи краще розписані властивості та типи даних, з якими працює функція
    
---