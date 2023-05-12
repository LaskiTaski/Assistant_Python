from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.Machine_kb import *
from keyboards.video_kb import *
from keyboards.homework_kb import *
from keyboards.project_kb import *
from keyboards.learning_kb import *
from keyboards.materials_kb import *
from bot_telegram import bot
from aiogram import types, Dispatcher


class FSMAdmin(StatesGroup):
    start = State()

    video = State()
    video1 = State()
    video2 = State()
    video3 = State()
    video4 = State()

    home_work = State()
    home_work1 = State()
    home_work2 = State()
    home_work3 = State()

    project = State()
    project1 = State()
    project2 = State()
    project3 = State()

    learning = State()
    material = State()

# @dp.message_handler(!!!commands=['start']!!!, state=None)
async def cmd_start(message: types.Message):
    ikbmenu = types.InlineKeyboardMarkup(row_width=1)
    ikbmenu.add(Video, Home_Work, Project, Learning,  Book)
    await FSMAdmin.start.set()
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите раздел',
                           reply_markup=ikbmenu)

# @dp.callback_query_handler(text='Menu')
async def cb_menu1(callback: types.CallbackQuery):
    ikbmenu = types.InlineKeyboardMarkup(row_width=1)
    ikbmenu.add(Video, Home_Work, Project, Learning, Book)
    await FSMAdmin.start.set()
    await callback.message.edit_text('Выберите раздел', reply_markup=ikbmenu)


# @dp.callback_query_handler(text='AllMenu', state='*')
# async def allmenu_handler(callback : types.CallbackQuery, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()


# @dp.callback_query_handler(text='Video', state=FSMAdmin.start)
async def cb_video(callback: types.CallbackQuery):
    Video = types.InlineKeyboardMarkup(row_width=1)
    Video.add(VModule1, VModule2, VModule3, VModule4, AllMenu)
    await FSMAdmin.video.set()
    await callback.message.edit_text('Видеоматериалы по:', reply_markup=Video)


# @dp.callback_query_handler(text='Home_Work', state=FSMAdmin.start)
async def cb_home_work(callback: types.CallbackQuery):
    Video = types.InlineKeyboardMarkup(row_width=1)
    Video.add(HModule1, HModule2, HModule3, AllMenu)
    await FSMAdmin.home_work.set()
    await callback.message.edit_text('Разбор домашки по:', reply_markup=Video)


# @dp.callback_query_handler(text='Projects', state=FSMAdmin.start)
async def cb_projects(callback: types.CallbackQuery):
    PModules = types.InlineKeyboardMarkup(row_width=1)
    PModules.add(PModule1, PModule2, PModule3, PModule4, AllMenu)
    await FSMAdmin.project.set()
    await callback.message.edit_text('Проекты по:', reply_markup=PModules)



# @dp.callback_query_handler(lambda x : x.data in [ i for i in learning_dict()], state=FSMAdmin.start)
async def cb_learning(callback: types.CallbackQuery, state=FSMAdmin.start):
    Learning = types.InlineKeyboardMarkup(row_width=3)
    Learning.add(Timur_1_R if callback.data == 'Learning' else Timur_1_B,
                 Timur_2_R if callback.data == 'lvl2' else Timur_2_B,
                 Egorov_1_R if callback.data == 'lvl3' else Egorov_1_B,
                 Fedotov_R if callback.data == 'lvl4' else Fedotov_B,
                 Egorov_2_R if callback.data == 'lvl5' else Egorov_2_B,
                 LeetCode_R if callback.data == 'lvl6' else LeetCode_B,
                 CodeWars_R if callback.data == 'lvl7' else CodeWars_B,
                 AllMenu)
    await callback.message.edit_text(f'[{learning_dict()[callback.data][0]}]({learning_dict()[callback.data][1]})',
                                     reply_markup=Learning)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in txt_dict()], state=FSMAdmin.start)
async def cb_materials(callback: types.CallbackQuery):
    TXT = types.InlineKeyboardMarkup(row_width=3)
    TXT.add(IntR if callback.data == 'Txt_book' else IntB,
            StrR if callback.data == 'str' else StrB,
            ListR if callback.data == 'list' else ListB,
            DictR if callback.data == 'dict' else DictB,
            OpenR if callback.data == 'open' else OpenB,
            TurtleR  if callback.data == 'turtle' else TurtleB,
            OOPR if callback.data == 'OOP' else OOPB,
            AllMenu)
    await callback.message.edit_text(f'[{txt_dict()[callback.data][0]}]({txt_dict()[callback.data][1]})',
                                     reply_markup=TXT)


def register_handlers_machine(dp : Dispatcher):
    dp.register_message_handler(cmd_start, state=None)
    dp.register_callback_query_handler(cb_menu1, text='Menu' , state='*')
    dp.register_callback_query_handler(cb_video, text='Video', state=FSMAdmin.start)
    dp.register_callback_query_handler(cb_home_work, text='Home_Work', state=FSMAdmin.start)
    dp.register_callback_query_handler(cb_projects, text='Projects', state=FSMAdmin.start)
    dp.register_callback_query_handler(cb_learning, lambda x: x.data in [i for i in learning_dict()], state=FSMAdmin.start)
    dp.register_callback_query_handler(cb_materials, lambda x: x.data in [i for i in txt_dict()], state=FSMAdmin.start)