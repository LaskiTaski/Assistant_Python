from aiogram.utils import executor
from bot_telegram import dp
from handlers import Machine, Module_Video, \
                     Module_HomeWork, Module_Project
"""
ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ДЛЯ ХОСТЫ...

"""
import os
from background import keep_alive  #импорт функции для поддержки работоспособности
import pip
pip.main(['install', 'aiogram'])

Machine.register_handlers_machine(dp)
Module_Video.register_handlers_video(dp)
Module_HomeWork.register_handlers_homework(dp)
Module_Project.register_handlers_project(dp)



keep_alive()
async def on_start_up(_):
    print('Работаем!')

executor.start_polling(dp, skip_updates=True,on_startup=on_start_up)