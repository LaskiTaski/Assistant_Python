from aiogram import types


Timur_1_R = types.InlineKeyboardButton('Level 1🔶', callback_data='Learning')
Timur_2_R = types.InlineKeyboardButton('Level 2🔶', callback_data='lvl2')
Egorov_1_R = types.InlineKeyboardButton('Level 3🔶', callback_data='lvl3')
Fedotov_R = types.InlineKeyboardButton('Bioinformatics Institute🔶', callback_data='lvl4')
Egorov_2_R = types.InlineKeyboardButton('OOP🔶', callback_data='lvl5')
LeetCode_R = types.InlineKeyboardButton('LeetCode🔶', callback_data='lvl6')
CodeWars_R = types.InlineKeyboardButton('Codewars🔶', callback_data='lvl7')
Timur_1_B = types.InlineKeyboardButton('Level 1🔷', callback_data='Learning')
Timur_2_B = types.InlineKeyboardButton('Level 2🔷', callback_data='lvl2')
Egorov_1_B = types.InlineKeyboardButton('Level 3🔷', callback_data='lvl3')
Fedotov_B = types.InlineKeyboardButton('Bioinformatics Institute🔷', callback_data='lvl4')
Egorov_2_B = types.InlineKeyboardButton('OOP🔷', callback_data='lvl5')
LeetCode_B = types.InlineKeyboardButton('LeetCode🔷', callback_data='lvl6')
CodeWars_B = types.InlineKeyboardButton('Codewars🔷', callback_data='lvl7')
AllMenu = types.InlineKeyboardButton('Вернуться в меню🔙', callback_data='Menu')


def learning_dict():
    ledi = {
        'Learning' : ['Для начинающих', 'https://telegra.ph/Codewars-03-17'],
        'lvl2' : ['Для продвинутых', 'https://telegra.ph/Dlya-prodvinutyh-03-17'],
        'lvl3' : ['Инди-курс', 'https://telegra.ph/Indi-kurs-03-17-2'],
        'lvl4' : ['Bioinformatics Institute', 'https://telegra.ph/Bioinformatics-Institute-03-17'],
        'lvl5' : ['Всё про ООП', 'https://telegra.ph/OOP-03-17'],
        'lvl6' : ['LeetCode', 'https://telegra.ph/LeetCode-03-17'],
        'lvl7' : ['Codewars', 'https://telegra.ph/Codewars-03-17-2']
    }
    return ledi