from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_1_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/breed-library')
    keyboard_inline.add(but_inline, but_inline2)

    return keyboard_inline

def get_keyboard_2_inline():
    keyboard_inline2 = InlineKeyboardMarkup(row_width= 2)
    but_inline3 = InlineKeyboardButton('Посмотреть', url='https://animals.moe-online.ru/articles/gryzuny/749')
    but_inline4 = InlineKeyboardButton('Посмотреть', url='https://animals.moe-online.ru/articles/gryzuny/749')
    keyboard_inline2.add(but_inline3, but_inline4)

    return keyboard_inline2
