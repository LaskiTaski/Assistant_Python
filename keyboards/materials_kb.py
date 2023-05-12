from aiogram import types


IntR = types.InlineKeyboardButton('Числа🔶', callback_data='Txt_book')
StrR = types.InlineKeyboardButton('Строки🔶', callback_data='str')
ListR = types.InlineKeyboardButton('Списки🔶', callback_data='list')
DictR = types.InlineKeyboardButton('Словари🔶', callback_data='dict')
OpenR = types.InlineKeyboardButton('Чтение файлов🔶', callback_data='open')
TurtleR = types.InlineKeyboardButton('Turtle🔶', callback_data='turtle')
OOPR = types.InlineKeyboardButton('ООП🔶', callback_data='OOP')
IntB = types.InlineKeyboardButton('Числа🔷', callback_data='Txt_book')
StrB = types.InlineKeyboardButton('Строки🔷', callback_data='str')
ListB = types.InlineKeyboardButton('Списки🔷', callback_data='list')
DictB = types.InlineKeyboardButton('Словари🔷', callback_data='dict')
OpenB = types.InlineKeyboardButton('Чтение файлов🔷', callback_data='open')
TurtleB = types.InlineKeyboardButton('Turtle🔷', callback_data='turtle')
OOPB = types.InlineKeyboardButton('ООП🔷', callback_data='OOP')
AllMenu = types.InlineKeyboardButton('Вернуться в меню🔙', callback_data='Menu')


def txt_dict():
    text = {
        'Txt_book' : ['Числа', 'https://telegra.ph/CHislovye-metodyfunkciioperacii-02-05'],
        'str' : ['Строки', 'https://telegra.ph/Strokovye-metodyfunkciiprimery-02-05'],
        'list' : ['Списки', 'https://telegra.ph/Metodyfunkciiprimery-spiskov-02-05'],
        'dict' : ['Словари', 'https://telegra.ph/Primery-i-metody-slovarej-02-05'],
        'open' : ['Чтение файлов', 'https://telegra.ph/CHtenie-fajlov-02-05'],
        'turtle': ['Turtle', 'https://telegra.ph/Modul-Turtle-02-05'],
        'OOP' : ['ООП', 'https://telegra.ph/OOP-02-05'],
    }
    return text