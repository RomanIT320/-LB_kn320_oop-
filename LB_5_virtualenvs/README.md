# Звіт до роботи virtualenvs

## Тема: Віртуальні середовища

### Мета: Оволодіти основам роботи з сторонніми бібліотеками

---

### Виконання роботи:

### Основи роботи з сторонніми бібліотеками

- Я ввів команду `pip list`, щоб вивести список встановлених бібліотек:

<details><summary> === Осьо шо получилося === </summary>
```<br>
aiogram           2.13
aiohttp           3.7.4.post0
async-timeout     3.0.1
attrs             21.2.0
Babel             2.9.1
certifi           2021.5.30
chardet           4.0.0
configparser      5.0.2
idna              2.10
keyboard          0.13.5
MouseInfo         0.1.3
mss               6.1.0
multidict         5.1.0
numpy             1.20.3
pip               21.2.3
pyaes             1.6.1
pyasn1            0.4.8
PyAutoGUI         0.9.52
PyGetWindow       0.0.9
PyMsgBox          1.0.9
pyperclip         1.8.2
PyRect            0.1.4
PyScreeze         0.1.27
pyTelegramBotAPI  3.7.9
PyTweening        1.0.3
pytz              2021.1
requests          2.25.1
rsa               4.7.2
setuptools        57.4.0
Telethon          1.23.0
termcolor         1.1.0
typing-extensions 3.10.0.0
urllib3           1.26.5
wget              3.2
yarl              1.6.3
```
</details>

---

- Я вставив код з прикладу у файл `.ipynb`

```py
import requests

res = requests.get('https://google.com')
print(res.status_code)
```

у відповідь я получив код 200, який означає, що все гуд )

```txt
200
```

- Поекспериментував з різнимим методами рекюестс:

```py
import requests as r

res = r.get('https://api.github.com/events')

print(f'''
url \t {res.url}
just res \t {res}
status code \t {res.status_code}
encoding \t {res.encoding}
raw \t {res.raw}
a lot of text \t {res.text}
''')
```

<details><summary> === Щось занадто багато тексту на цій сторінці, для прикладу я залишив 1% від всього тексту === </summary>
```<br>
url  -   https://api.github.com/events<br>
just res    -    Response [200]<br>
status   -   code 200<br>
encoding   -     utf-8<br>
raw     -    urllib3.response.HTTPResponse object at 0x000001B1E2B52890<br>
a lot of text    -   [{"id":"24554816296","type":"PushEvent","actor":{"id":28802726,"login":"lapnguyen12b","display_login":"lapnguyen12b","gravatar_id":"","url":"https://api.github.com/users/lapnguyen12b","avatar_url":"https://avatars.githubusercontent.com/u/28802726?"},"repo":{"id":550319158,"name":"lapnguyen12b/Solidity-tutorial","url":"https://api.github.com/repos/lapnguyen12b/Solidity-tutorial"},"payload":{"push_id":11306606032,"size":2,"distinct_size":1,"ref":"refs/heads/master","head":"d6adc79cd41c0800c77a7c5c615a2804a6f5edd1","before":"7d0dfeaac16bfb43091c120953568284ab62edfb","commits":[{"sha":"b8b15243e4febea83269cb958dc059d58354e491","author":{"email":"lapnguyen12b@gmail.com","name":"lapnv"},"message":"first constract","distinct":false,"url":"https://api.github.com/repos/lapnguyen12b/Solidity-tutorial/commits/b8b15243e4febea83269cb958dc059d58354e491"},{"sha":"d6adc79cd41c0800c77a7c5c615a2804a6f5edd1","author":{"email":"lapnguyen12b@gmail.com","name":"lnv1995"},"message":"Merge pull request #1 from lapnguyen12b/lapnv/first-constract\n\nFirst constract","distinct":true,"url":"https://api.github.com/repos/lapnguyen12b/Solidity-tutorial/commits/d6adc79cd41c0800c77a7c5c615a2804a6f5edd1"}]
```
</details>

---

- Я ввів наступні команди:

```
pip show requests
pip install requests==2.1
pip show requests
pip uninstall requests
```

І ось що вони вивели у консольку:

## pip show requests

```
Name: requests
Version: 2.27.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: d:\software\programs\python3\lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by: cfscrape, openai, shodan, webdriver-manager
```

## pip install requests==2.1

```
Collecting requests==2.1
  Downloading requests-2.1.0-py2.py3-none-any.whl (445 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 445.3/445.3 kB 3.1 MB/s eta 0:00:00
Installing collected packages: requests
  Attempting uninstall: requests
    Found existing installation: requests 2.27.1
    Uninstalling requests-2.27.1:
      Successfully uninstalled requests-2.27.1
Successfully installed requests-2.1.0
```

## pip show requests

видно що інсталювалась старіша версія бібліотеки

```
Name: requests
Version: 2.1.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Copyright 2013 Kenneth Reitz
Location: d:\software\programs\python3\lib\site-packages
Requires:
Required-by: cfscrape, openai, shodan, webdriver-manager
```

## pip uninstall requests

```
Found existing installation: requests 2.1.0
Uninstalling requests-2.1.0:
  Would remove:
    d:\software\programs\python3\lib\site-packages\requests-2.1.0.dist-info\*
    d:\software\programs\python3\lib\site-packages\requests\*
Proceed (Y/n)? y
  Successfully uninstalled requests-2.1.0
```

---

### Робота у віртуальному середовищі

- Я ввів по черзі запропоновані команди, але деякі з них видавали помилку

```py
python - m venv ./my_env
source my_env/Scripts/activate
pip install requests
deactivate
pip show requests
```

- Команда `pip show requests` вивела опис бібліотеки. Вона це вивела бо так пише в [доках )](https://pip.pypa.io/en/stable/cli/pip_show/)

```
Name: requests
Version: 2.28.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: d:\software\programs\python3\lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by: cfscrape, openai, shodan, webdriver-manager
```

---

### Робота з Pipenv

- Я інсталював піпенв бібліотеку, та написав `pipenv --help`. Ось що вивелось:

```
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.
  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]
  --python TEXT                   Specify which version of Python virtualenv
                                  should use.
  --three                         Use Python 3 when creating virtualenv.
                                  Deprecated
  --clear                         Clears caches (pipenv, pip).  [env var:
                                  PIPENV_CLEAR]
  -q, --quiet                     Quiet mode.
  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  verify        Verify the hash in Pipfile.lock is up-to-date.
```

- Я ввів код з прикладу і запустив з терміналу VS Code. У відповідь я отримав код сторінки
  Це не весь код, для прикладу я вставив тільки до закриваючого тегу `head`

```text
b'<!DOCTYPE html>'
b'<html lang="en">'
b''
b'<head>'
b'    <meta charset="UTF-8">'
b'    <title>httpbin.org</title>'
b'    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"'
b'        rel="stylesheet">'
b'    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">'
b'    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />'
b'    <style>'
b'        html {'
b'            box-sizing: border-box;'
b'            overflow: -moz-scrollbars-vertical;'
b'            overflow-y: scroll;'
b'        }'
b''
b'        *,'
b'        *:before,'
b'        *:after {'
b'            box-sizing: inherit;'
b'        }'
b''
b'        body {'
b'            margin: 0;'
b'            background: #fafafa;'
b'        }'
b'    </style>'
b'</head>'
b''
```

- Коли я запустив код код через консольку `CMD`, то результат був такий самий як і вище.

- Я написав команду `pipenv shell`. Після чого у папці заспавнився файл `Pipfile`, а вигляд консольки змінився на такий `(Lab4-LqyyIgqt) D:\Labs\Labs 3.1\ООП\github\OOP\Lab4>`.
  Здається теппер консолька буде запускати програмки у віртуальному серидовищі. 🤔

- Коли я запустив той самий код у віртуальному серидовищі, мені пітон сказав що мені не хватає модуля `ModuleNotFoundError: No module named 'requests'`.
  Проте мене це не зупинило. Я зробив `pip install requests`.
  Після того все запустилсь, результат такий самий.

- Я обрав бібліотеку `aiogram` вона створена для роботи з `Telegram API`, знайшов [документацію](https://docs.aiogram.dev/en/latest/).
  У мене навіть є бот, якого я колись писав. Сьогодні зранку я вчився закидувати його на хостинг 😎.
  [Ось він тут є, в сусідньому репозиторії.](https://github.com/Yuriy-Lapin/bot404)

- Спробував я змінти інтерпритатор, але він у мене тільки 1:

```
Python 3.10.6 64-bit
```

### Робота зі змінними середовища

- Я створив файл `.env` та запистик код з пикладу, мені вивело таку помилку:

```
KeyError: 'HELLO'
```

---

### Висновок:

- :question: Що зроблено в роботі; :wavy_dash: Трошки побавились з бібліотеками та віртуальними серидовищами
- :question: Чи досягнуто мети роботи; :wavy_dash: я гадаю що так )
- :question: Які нові знання отримано; :wavy_dash: ну я раніше не знав про існування віртуальних серидовищ
- :question: Чи вдалось відповісти на всі питання задані в ході роботи; :wavy_dash: так, можливо 🤔
- :question: Чи вдалося виконати всі завдання; :wavy_dash: вдалось, хоча при рботі з venv деякі команди видавали помилку, можливо я не до кінця зрозумів синтаксис команди 🤔
- :question: Чи виникли складності у виконанні завдання; :wavy_dash: ще й як виникли, минулий понеділок та вівторок без світла діже сильно вибив з привичного ритму життя. Аж тепер коли тривог не так багато, я зміг доробити це завдання.
- :question: Чи подобається такий формат здачі роботи (Feedback); :wavy_dash: :sunglasses::+1:
- :question: Побажання для покращення (Suggestions); :wavy_dash: впринцині всьо норм )
