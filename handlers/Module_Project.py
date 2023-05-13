from aiogram import Dispatcher
from keyboards.project_kb import *
from handlers.Machine import FSMAdmin
from keyboards.Machine_kb import AllMenu

# @dp.callback_query_handler(lambda x : x.data in [ i for i in P1_dict()]FSMAdmin.project)
async def cb_project1(callback: types.CallbackQuery):
    P1 = types.InlineKeyboardMarkup(row_width=3)
    P1.add(PModule1R if callback.data == 'PModule1' else PModule1B,
           PModule2R if callback.data == 'P1_2' else PModule2B,
           PModule3R if callback.data == 'P1_3' else PModule3B,
           AllMenu)
    await FSMAdmin.project1.set()
    await callback.message.edit_text(f'[{P1_dict()[callback.data][0]}]({P1_dict()[callback.data][1]})',
                                     reply_markup=P1)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in P2_dict()]FSMAdmin.project)
async def cb_project2(callback: types.CallbackQuery):
    P2 = types.InlineKeyboardMarkup(row_width=3)
    P2.add(PModule1RR if callback.data == 'PModule2' else PModule1BB,
           PModule2RR if callback.data == 'P2_2' else PModule2BB,
           PModule3RR if callback.data == 'P2_3' else PModule3BB,
           AllMenu)
    await FSMAdmin.project2.set()
    await callback.message.edit_text(f'[{P2_dict()[callback.data][0]}]({P2_dict()[callback.data][1]})',
                                     reply_markup=P2)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in P3_dict()]FSMAdmin.project)
async def cb_project3(callback: types.CallbackQuery):
    P3 = types.InlineKeyboardMarkup(row_width=3)
    P3.add(PModule1RR if callback.data == 'PModule3' else PModule1BB,
           AllMenu)
    await FSMAdmin.project3.set()
    await callback.message.edit_text(f'[{P3_dict()[callback.data][0]}]({P3_dict()[callback.data][1]})',
                                     reply_markup=P3)


def register_handlers_project(dp: Dispatcher):
    dp.register_callback_query_handler(cb_project1, lambda x: x.data in [i for i in P1_dict()], state=(FSMAdmin.project, FSMAdmin.project1))
    dp.register_callback_query_handler(cb_project2, lambda x: x.data in [i for i in P2_dict()], state=(FSMAdmin.project, FSMAdmin.project2))
    dp.register_callback_query_handler(cb_project3, lambda x: x.data in [i for i in P3_dict()], state=(FSMAdmin.project, FSMAdmin.project3))
