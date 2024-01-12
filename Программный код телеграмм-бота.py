import telebot  # Импортируем библиотеку для создания бота.
from telebot import types  # Импортируем из библиотеки объект, который поможет в создании кнопок.
bot = telebot.TeleBot('5781778325:AAFCq906xvRRCc7PeVv5TkSB-VpmMlWjD_A')  # Указываем токен бота.


@bot.message_handler(commands=['start'])  # Отслеживает команду start
def start(message):
    if message.text == '/start':
        answers.clear()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Кнопки будут находиться ниже поля текста.
    # S1, S2, S3, S4, S6 являются наименованиями встроенных кнопок.
    S1 = types.InlineKeyboardButton('Макароны, крупы и каши')
    S2 = types.InlineKeyboardButton('Молочные продукты \U0001F95B')
    # \U000... это код эмоджи, так чат не будет перегружен сообщениями.
    S3 = types.InlineKeyboardButton('Мясо \U0001F357')
    S4 = types.InlineKeyboardButton('Овощи')
    S5 = types.InlineKeyboardButton('Фрукты')
    S6 = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
    markup.add(S1, S2, S3, S4, S5, S6)  # Комплектуем кнопки.
    send = bot.send_message(message.chat.id,
                            'Привет, {0.first_name}! Скорей выбирай продукты и начинай готовить.'.format(
                                message.from_user),
                            reply_markup=markup)  # Обращение к боту, чтобы он отправил заданное сообщение.
    bot.register_next_step_handler(send, purchase)
    # Метод (register_next_step_handler) принимает два обязательных аргумента.
    # Он ждет сообщение от пользователя, потом вызывает указанную функцию purchase.


@bot.message_handler(commands=['help'])  # Отслеживает команду help
def helplist(message):
    helptext = '''Ваш любимый телеграмм бот всегда готов помочь! \U0001F439 Вот его команды:
/start - стартовое сообщение;
/help  - помощь;
/clean - очищает список ингредиентов.'''
    bot.send_message(message.chat.id, helptext)


@bot.message_handler(commands=['clean'])
def delete(message):
    if message.text == '/clean':
        answers.clear()
    send = bot.send_message(message.chat.id, 'Список очищен')
    bot.register_next_step_handler(send, get_name)


global answers  # Ключевое слово, которое позволяет изменять переменную вне текущей области видимости.
answers = []
def get_name(message):  # Конструкция формирует наш список ингредиентов.
    if message.text == 'Посмотреть ингредиенты':
        answers1 = str(answers)
        chars = {
            '[': ' ',
            "'": '',
            ']': '',
            ',': '\n'
        }
        new_answers = answers1.translate(str.maketrans(chars))
        bot.send_message(message.chat.id, 'Список: ' + '\n' + str(new_answers))
    elif len(message.text) <= 15 and message.text != '/start' and message.text != '/clean' and message.text != '/help'\
            and message.text != 'Мясо \U0001F357' and message.text != 'Овощи' and message.text != 'Фрукты':
        answers.append(message.text)

import urllib.request  # Импортируем модуль, который поможет в открытии URL-адресов и получении информации из Интернета.
def parsing(message):  # В данной конструкции мы займемся парсингом из облака.
    if message.text == 'Да!':
        answers2 = str(answers)
        char = {
            '[': '',
            '"': '',
            '[': '',
            "'": '',
            ',': '',
            ']': '',
            '"': '',
            ']': ''
        }
        new = answers2.translate(str.maketrans(char))
        n = str(sorted(list(new.split())))
        c = {
            '[': '<',
            "'": '',
            ']': '>',
        }
        list_1 = n.translate(str.maketrans(c))# Этот список будет использоваться для парсинга.
        logo = urllib.request.urlopen(
            "https://drive.google.com/uc?export=download&id=1lEZIoTr2XI2r1ZafTwRqPR_E6B-mgI61").read()
        # Функция urlopen открывает url.
        with open("parsing.txt", "wb") as f:
            f.write(logo)  # Переписываем в файл содержимое из нашей ссылки для дальнейшего использования.
        f.close()
        with open("parsing.txt", "r", encoding="utf8") as file:  # Читаем наш файл.
            try:
                for line in file:
                    # Сравниваем список ингредиентов со строчкой в файле.
                    if list_1 in line:
                        # Если все сходится, то боту будет передана информация из файла,
                        # которая находится между символами $ и # (это вспомогательные символы).
                        s = file.read()
                        s_new = s[s.find("$") + 1:]
                        bot.send_message(message.chat.id, s_new.split("#")[0])
                        break
                else:
                    bot.send_message(message.chat.id, 'Рецепт не найден')
            finally:
                file.close()


@bot.message_handler(content_types=['text'])  # Отслеживаем сообщения от пользователя.
def purchase(message):
    if message.text == 'Макароны, крупы и каши':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        С1 = types.InlineKeyboardButton('Вермишель')
        С2 = types.InlineKeyboardButton('Спагетти')
        С3 = types.InlineKeyboardButton('Крупа гречневая')
        С4 = types.InlineKeyboardButton('Булгур')
        С5 = types.InlineKeyboardButton('Хлопья овсяные')
        С6 = types.InlineKeyboardButton('Рис')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        products = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup1.add(С1, С2, С3, С4, С5, С6, back, products)
        send = bot.send_message(message.chat.id, '\U0001F35C', reply_markup=markup1)
        bot.register_next_step_handler(send, get_name);
        # Метод принимает два обязательных аргумента.
        # Он ждет сообщение от пользователя, потом вызывает указанную функцию get_name.

    elif message.text == 'Молочные продукты \U0001F95B':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Mp1 = types.InlineKeyboardButton('Масло сливочное')
        Mp2 = types.InlineKeyboardButton('Молоко')
        Mp3 = types.InlineKeyboardButton('Сливки')
        Mp4 = types.InlineKeyboardButton('Сметана')
        Mp5 = types.InlineKeyboardButton('Сыр твердый')
        Mp6 = types.InlineKeyboardButton('Творог')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        products = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup2.add(Mp1, Mp2, Mp3, Mp4, Mp5, Mp6, back, products)
        send = bot.send_message(message.chat.id, 'Молочные продукты', reply_markup=markup2)
        bot.register_next_step_handler(send, get_name);

    elif message.text == 'Мясо \U0001F357':
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        M1 = types.InlineKeyboardButton('Говядина')
        M2 = types.InlineKeyboardButton('Курица')
        M3 = types.InlineKeyboardButton('Рыба')
        M4 = types.InlineKeyboardButton('Свинина')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        products = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup3.add(M1, M2, M3, M4, back, products)
        send = bot.send_message(message.chat.id, '\U0001F437', reply_markup=markup3)
        bot.register_next_step_handler(send, get_name);

    elif message.text == 'Овощи':
        markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        V1 = types.InlineKeyboardButton('Картофель')
        V2 = types.InlineKeyboardButton('Морковь')
        V3 = types.InlineKeyboardButton('Лук репчатый')
        V4 = types.InlineKeyboardButton('Огурец')
        V5 = types.InlineKeyboardButton('Помидор')
        V6 = types.InlineKeyboardButton('Свекла')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        products = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup4.add(V1, V2, V3, V4, V5, V6, back, products)
        send = bot.send_message(message.chat.id, '\U0001F957', reply_markup=markup4)
        bot.register_next_step_handler(send, get_name);

    elif message.text == 'Фрукты':
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        F1 = types.InlineKeyboardButton('Ананас')
        F2 = types.InlineKeyboardButton('Апельсин')
        F3 = types.InlineKeyboardButton('Банан')
        F4 = types.InlineKeyboardButton('Груша')
        F5 = types.InlineKeyboardButton('Лимон')
        F6 = types.InlineKeyboardButton('Яблоко')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        products = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup5.add(F1, F2, F3, F4, F5, F6, back, products)
        send = bot.send_message(message.chat.id, '\U0001F347', reply_markup=markup5)
        bot.register_next_step_handler(send, get_name);

    elif message.text == 'Вернуться в главное меню \U000023EA':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        S1 = types.InlineKeyboardButton('Макароны, крупы и каши')
        S2 = types.InlineKeyboardButton('Молочные продукты \U0001F95B')
        S3 = types.InlineKeyboardButton('Мясо \U0001F357')
        S4 = types.InlineKeyboardButton('Овощи')
        S5 = types.InlineKeyboardButton('Фрукты')
        S6 = types.InlineKeyboardButton('Список продуктов \U0001F4CB')
        markup.add(S1, S2, S3, S4, S5, S6)
        bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

    elif message.text == 'Начать поиск рецептов?':
        markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y = types.InlineKeyboardButton('Да!')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        markup7.add(y, back)
        send = bot.send_message(message.chat.id, '\U0001F50E', reply_markup=markup7)
        bot.register_next_step_handler(send, parsing)

    elif message.text == 'Список продуктов \U0001F4CB':
        markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        l_p1 = types.InlineKeyboardButton('Начать поиск рецептов?')
        l_p2 = types.InlineKeyboardButton('Посмотреть ингредиенты')
        l_p3 = types.InlineKeyboardButton('/clean')
        back = types.InlineKeyboardButton('Вернуться в главное меню \U000023EA')
        markup6.add(l_p1, l_p2, back, l_p3)
        send = bot.send_message(message.chat.id, '\U0001F4AC', reply_markup=markup6)
        bot.register_next_step_handler(send, get_name)


bot.polling(none_stop=True)  # Постоянная обработка бота.
