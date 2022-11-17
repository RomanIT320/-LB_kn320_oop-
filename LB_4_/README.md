# Звіт до роботи first class

## Тема: Знайомство з ООП

### Мета: Навчитись працювати з класама та об'єктами

---

### Виконання роботи:

- Я запустив програму з класом:

<details><summary> >>>>>> Python Code <<<<<< </summary>
### Перша програма на ООП

```python


class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        # Class attributes / Instance variables
        self.name = name if name is not None else self.anonymous_user().name
        MyName.total_names += 1  # modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"

    def name_length(self):
        return len(self.name)


print("Let's Start!")

names = ("Bohdan", "Marta", None, "Roman")
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""\n{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("ahahahahaha HATO")} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
Lenght name = {me.name_length()}
We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?
{"<*>"*20}
""")

print(
    f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")



```

</details>

ось що вона вивела мені у консольку:

```
Let's Start!

>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001DB7E1EA4F0>
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: ahahahahaha HATO
This is class variable <class 'int'>: from class 5 / from object 5
Lenght name = 6
We are done. We create 5 names! ??? Why 5?
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>


>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001DB7E1EA490>
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: ahahahahaha HATO
This is class variable <class 'int'>: from class 5 / from object 5
Lenght name = 5
We are done. We create 5 names! ??? Why 5?
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>


>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001DB7E1EA430>
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: ahahahahaha HATO
This is class variable <class 'int'>: from class 5 / from object 5
Lenght name = 9
We are done. We create 5 names! ??? Why 5?
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>


>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001DB7E1EA370>
This is object attribute: Roman / 5
This is <class 'property'>: My name is Roman / Roman@itcollege.lviv.ua
This is <class 'method'> call: Roman@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: ahahahahaha HATO
This is class variable <class 'int'>: from class 5 / from object 5
Lenght name = 5
We are done. We create 5 names! ??? Why 5?
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>

We are done. We create 5 names! ??? Why 5?
```

- Відповіді на запитання:

1. Чому коли передаємо значення None створюється обєкт з іменем Anonymous?

   - бо в класі є метод який повертає Anonymous якщо ім'я = none

   ```py
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
   ```

2. Як змінити текст привітання при виклику методу say_hello()? Допишіть цю частину коду.

   - me.say_hello("ahahahahaha HATO") <- можна написати текст у виклик функції. Якщо робити виклик без параметрів то метод поверне "Hello to everyone!"

3. Допишіть функцію в класі яка порахує кількість букв в імені (підказка: використайте функцію len());

   ```py
   def name_lenght(self):
        return len(self.name)
   ```

4. Порахуйте кількість імен у списку names та порівняйте із виведеним результатом. Дайте відповідь чому маємо різну кількість імен?

   - Через тиждень пошуків я все ж таки знайшов те 5-е ім'я.<br>
     Як важає юра і якщо я його правильно зрозумів все відбувається так:<br>
     1. Створюється екземпляр класу з ім'ям `None`
     1. Тоді спрацьовує `MyName.total_names += 1`
     1. Після чого викликається метод `anonymous_user()` який повертає таку підозрілу штуку `cls("Anonymous")`
     1. І тоді вже створюється екземпляр з ім'ям `Anonymous` і його :id: на одиницю білше бо він перейшов шеодне коло

### Висновок:

- :question: Що зроблено в роботі; :wavy_dash: Навчився працювати з класами та обєктами
- :question: Чи досягнуто мети роботи; :wavy_dash: так
- :question: Які нові знання отримано; :wavy_dash: Отримано знання про ООП, класи, методи, `магічні` функцфї, декоратори.
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; :wavy_dash: Вдалось, навіть на 4 запитання
- :question: Чи вдалося виконати всі завдання; :wavy_dash: Ну якби не Юра
- :question: Чи виникли складності у виконанні завдання; :wavy_dash: Так, проблеми були, але тільки в 4 запитанні )
- :question: Чи подобається такий формат здачі роботи (Feedback); :wavy_dash: :sunglasses:: 10\10:
- :question: Побажання для покращення (Suggestions); :wavy_dash:

---
