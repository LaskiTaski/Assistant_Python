from aiogram import types


PModule1 = types.InlineKeyboardButton('Module1🤨', callback_data='PModule1')
PModule2 = types.InlineKeyboardButton('Module2🫠 ', callback_data='PModule2')
PModule3 = types.InlineKeyboardButton('Module3🤯', callback_data='PModule3')
PModule4 = types.InlineKeyboardButton('Module4🫣', callback_data='PModule4')
PBackMenu = types.InlineKeyboardButton(text='Вернуться в меню🔙', callback_data='Projects')
AllMenu = types.InlineKeyboardButton('Вернуться в меню🔙', callback_data='Menu')


PModule1R = types.InlineKeyboardButton('1 проект🔶', callback_data='PModule1')
PModule2R = types.InlineKeyboardButton('2 проект🔶', callback_data='P1_2')
PModule3R = types.InlineKeyboardButton('3 проект🔶', callback_data='P1_3')
PModule1B = types.InlineKeyboardButton('1 проект🔷', callback_data='PModule1')
PModule2B = types.InlineKeyboardButton('2 проект🔷', callback_data='P1_2')
PModule3B = types.InlineKeyboardButton('3 проект🔷', callback_data='P1_3')

def P1_dict():
    P1 = {
        'PModule1': ['10 Урок', 'https://telegra.ph/Pervyj-proekt-1-modulya-02-03'],
        'P1_2': ['11 Урок', 'https://telegra.ph/Vtoroj-proekt-1-modulya-02-03'],
        'P1_3': ['12 Урок', 'https://telegra.ph/Tretij-proekt-1-modulya-02-03'],
    }
    return P1


PModule1RR = types.InlineKeyboardButton('1 проект🔶', callback_data='PModule2')
PModule2RR = types.InlineKeyboardButton('2 проект🔶', callback_data='P2_2')
PModule3RR = types.InlineKeyboardButton('3 проект🔶', callback_data='P2_3')
PModule1BB = types.InlineKeyboardButton('1 проект🔷', callback_data='PModule2')
PModule2BB = types.InlineKeyboardButton('2 проект🔷', callback_data='P2_2')
PModule3BB = types.InlineKeyboardButton('3 проект🔷', callback_data='P2_3')

def P2_dict():
    P2 = {
        'PModule2': ['8 Урок', 'https://telegra.ph/Pervyj-proekt-2-modulya-02-03'],
        'P2_2': ['11 Урок', 'https://telegra.ph/Vtoroj-proekt-2-modulya-02-03'],
        'P2_3': ['12 Урок', 'https://telegra.ph/Tretij-proekt-2-modulya-02-03'],
    }
    return P2

PModule1RRR = types.InlineKeyboardButton('1 проект🔶', callback_data='PModule3')
PModule1BBB = types.InlineKeyboardButton('1 проект🔷', callback_data='PModule3')

def P3_dict():
    P3 = {
        'PModule3': ['12 Урок', 'https://telegra.ph/Mini-bot-03-17'],
    }
    return P3