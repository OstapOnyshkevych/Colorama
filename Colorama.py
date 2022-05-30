from colorama import Fore, Back, Style       #Тут ми з бібліотеки colorama імпортуємо Fore(колір тексту),Back(колір заднього фону текста),Style(стиль текста)
from colorama import init
from termcolor import colored
init()
                        #На мою думку найважливіші команди з бібліотеки colorama є такі коди:
print(Fore.RED + 'Hello')          #Спочатку ми імпортуємо бібліотеку colorama.Вона нам дозволяє змінювати колір тексту і задній фон тексту.
                                   #Наприклад,у цьому коді слово Hello напишеться червоним кольором,бо ми із бібліотеки імпортували Fore.
                                   #Fore нам допомагає змінювати колір тексту.Можна зробити тест синім,якщо замість Fore.Red написати Fore.Blue і так дальше.

print(Back.BLUE + 'guys')          #А вже в цьому коді код Back означає у тексті задній фон.Тобто можна змінювати задній фон тексту на червоний,білий,чорний і так дальше.
                                   #Тобто слово guys напишеться червоним кольором,а задній фон тексту буде синім.Чому червоний текст?.Бо Fore.Red працює і на наступні тексти,навіть якщо вони і в іншому прінті.

print(Style.RESET_ALL)             #Щоб уникнути Fore.Red на наступних текстах,треба написати код Style.RESET_ALL.Цей код збиває і не дає червоному кольору і задньому фону розповсюджуватися на текстах після цього коду.Якщо текст перед цим кодом,текст буде червоним і матиме якийсь задній фон.
print('girls')                     #Тобто слово girls напишеться білим кольором і також без заднього фона.

print('\033[31m' + 'some red text')   #Щоб не писати print(Fore.Red + 'якийсь текст') можна написати цей код,тобто тут то саме тільки попростіше.Тут число 31 замалює текст червоним.
                                      #Від числа 30 до 39 це замальовка тексту,а від 40 до 47 це вже задній фон тексту.
                                    #Вот позначено яке число за що відповідає:
# КОЛІР ТЕКСТУ:
# ESC [ 30 m      # Чорний
# ESC [ 31 m      # Червоний
# ESC [ 32 m      # Зелений
# ESC [ 33 m      # Жовтий
# ESC [ 34 m      # Синій
# ESC [ 35 m      # Рожевий
# ESC [ 36 m      # Голубий
# ESC [ 37 m      # Білий
# ESC [ 39 m      # Забрати колір

# КОЛІР ЗАДНЬОГО ФОНУ:
# ESC [ 40 m      # Чорний
# ESC [ 41 m      # Червоний
# ESC [ 42 m      # Зелений
# ESC [ 43 m      # Жовтий
# ESC [ 44 m      # Синій
# ESC [ 45 m      # Рожевий
# ESC [ 46 m      # Голубий
# ESC [ 47 m      # Білий
# ESC [ 49 m      # Забрати колір

print(colored('Hello, World!', 'red', 'on_blue'))   #В цьому коді треба ще загрузити бібліотеку termcolor,щоб код запрацював.Тут тоже все скорочено.
                                                    #Наприклад щоб написати слова Hello World якийсь колір і щоб був задній фон.Це можна помістити в один рядок.
                                                    #Треба після прінта написати colored,щоб текст міг розфарбовуватися.Після того як Ви написали якийсь текст.
                                                    #Треба після того тексту поставити кому і в лапках написати колір в який Ви хочите пофарбувати текст.
                                                    #Потім,щоб зробити задній фон треба знову поставити кому і в лапках написати on_blue і тоді задній фон тексту буде голубий.

                                                    #Ці коди я вважаю найголовнішими з бібліотеки colorama