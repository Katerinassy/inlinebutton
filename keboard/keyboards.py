from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Предсказние')
    button_2 = KeyboardButton('Чистая правда')
    button_3 = KeyboardButton('Отправь фото BMW M5')
    button_4 = KeyboardButton('Перейти на следующую клавиатуру')
    keyboard.add(button_1, button_2, button_3, button_4)
    return keyboard

def get_keyboard_2():
    keyboard_2= ReplyKeyboardMarkup(resize_keyboard=True)
    button_5 = KeyboardButton('Отправь фото RAM')
    button_6 = KeyboardButton('Вернуться на 1 клавиатуру')
    keyboard_2.add(button_5, button_6, )
    return keyboard_2