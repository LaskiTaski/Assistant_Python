from aiogram import Dispatcher
from keyboards.homework_kb import *
from handlers.Machine import FSMAdmin
from keyboards.Machine_kb import AllMenu


# @dp.callback_query_handler(lambda x : x.data in [ i for i in H1_dict()], state=FSMAdmin.home_work)
async def cb_home_work1(callback: types.CallbackQuery):
    H1 = types.InlineKeyboardMarkup(row_width=3)
    H1.add(HY1R  if callback.data == 'HModule1' else HY1B ,
           HY2R  if callback.data == 'H1_2' else HY2B ,
           HY3R  if callback.data == 'H1_3' else HY3B ,
           HY4R  if callback.data == 'H1_4' else HY4B ,
           HY5R  if callback.data == 'H1_5' else HY5B ,
           HY6R  if callback.data == 'H1_6' else HY6B ,
           HY7R  if callback.data == 'H1_7' else HY7B ,
           HY8R  if callback.data == 'H1_8' else HY8B ,
           HY9R  if callback.data == 'H1_9' else HY9B ,
           HY10R  if callback.data == 'H1_10' else HY10B ,
           HY11R  if callback.data == 'H1_11' else HY11B ,
           HY12R  if callback.data == 'H1_12' else HY12B ,
           AllMenu)
    await FSMAdmin.home_work1.set()
    await callback.message.edit_text(f'[{H1_dict()[callback.data][0]}]({H1_dict()[callback.data][1]})',
                                     reply_markup=H1)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in H2_dict()], state=FSMAdmin.home_work)
async def cb_home_work2(callback: types.CallbackQuery):
    H2 = types.InlineKeyboardMarkup(row_width=3)
    H2.add(HY1RR  if callback.data == 'HModule2' else HY1BB ,
           HY2RR  if callback.data == 'H2_2' else HY2BB ,
           HY3RR  if callback.data == 'H2_3' else HY3BB ,
           HY4RR  if callback.data == 'H2_4' else HY4BB ,
           HY5RR  if callback.data == 'H2_5' else HY5BB ,
           HY6RR  if callback.data == 'H2_6' else HY6BB ,
           HY7RR  if callback.data == 'H2_7' else HY7BB ,
           HY8RR  if callback.data == 'H2_8' else HY8BB ,
           HY9RR  if callback.data == 'H2_9' else HY9BB ,
           HY10RR  if callback.data == 'H2_10' else HY10BB ,
           HY11RR  if callback.data == 'H2_11' else HY11BB ,
           HY12RR  if callback.data == 'H2_12' else HY12BB ,
           AllMenu)
    await FSMAdmin.home_work2.set()
    await callback.message.edit_text(f'[{H2_dict()[callback.data][0]}]({H2_dict()[callback.data][1]})',
                                     reply_markup=H2)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in H3_dict()], state=FSMAdmin.home_work)
async def cb_home_work3(callback: types.CallbackQuery):
    H3 = types.InlineKeyboardMarkup(row_width=3)
    H3.add(HY1RRR  if callback.data == 'HModule3' else HY1BBB ,
           HY2RRR  if callback.data == 'H3_2' else HY2BBB ,
           HY3RRR  if callback.data == 'H3_3' else HY3BBB ,
           HY4RRR  if callback.data == 'H3_4' else HY4BBB ,
           HY5RRR  if callback.data == 'H3_5' else HY5BBB ,
           HY6RRR  if callback.data == 'H3_6' else HY6BBB ,
           HY7RRR  if callback.data == 'H3_7' else HY7BBB ,
           HY8RRR  if callback.data == 'H3_8' else HY8BBB ,
           HY9RRR  if callback.data == 'H3_9' else HY9BBB ,
           HY10RRR  if callback.data == 'H3_10' else HY10BBB ,
           HY11RRR  if callback.data == 'H3_11' else HY11BBB ,
           HY12RRR  if callback.data == 'H3_12' else HY12BBB ,
           AllMenu)
    await FSMAdmin.home_work3.set()
    await callback.message.edit_text(f'[{H3_dict()[callback.data][0]}]({H3_dict()[callback.data][1]})',
                                     reply_markup=H3)

def register_handlers_homework(dp : Dispatcher):
    dp.register_callback_query_handler(cb_home_work1, lambda x : x.data in [ i for i in H1_dict()], state=(FSMAdmin.home_work, FSMAdmin.home_work1))
    dp.register_callback_query_handler(cb_home_work2, lambda x : x.data in [ i for i in H2_dict()], state=(FSMAdmin.home_work, FSMAdmin.home_work2))
    dp.register_callback_query_handler(cb_home_work3, lambda x : x.data in [ i for i in H3_dict()], state=(FSMAdmin.home_work, FSMAdmin.home_work3))