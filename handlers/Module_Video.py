from aiogram import Dispatcher
from keyboards.video_kb import *
from handlers.Machine import FSMAdmin
from keyboards.Machine_kb import AllMenu


# @dp.callback_query_handler(lambda x : x.data in [ i for i in V1_dict()], state=FSMAdmin.video)
async def cb_video1(callback: types.CallbackQuery):
    print('Работает V1')
    V1 = types.InlineKeyboardMarkup(row_width=3)
    V1.add(VY1R if callback.data == 'VModule1' else VY1B,
           VY2R if callback.data == 'V1_2' else VY2B,
           VY3R if callback.data == 'V1_3' else VY3B,
           VY4R if callback.data == 'V1_4' else VY4B,
           VY5R if callback.data == 'V1_5' else VY5B,
           VY6R if callback.data == 'V1_6' else VY6B,
           VY7R if callback.data == 'V1_7' else VY7B,
           VY8R if callback.data == 'V1_8' else VY8B,
           VY9R if callback.data == 'V1_9' else VY9B,
           VY10R if callback.data == 'V1_10' else VY10B,
           VY11R if callback.data == 'V1_11' else VY11B,
           VY12R if callback.data == 'V1_12' else VY12B,
           AllMenu)
    await FSMAdmin.video1.set()
    await callback.message.edit_text(f'[{V1_dict()[callback.data][0]}]({V1_dict()[callback.data][1]})',
                                     reply_markup=V1)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in V2_dict()], state=FSMAdmin.video)
async def cb_video2(callback: types.CallbackQuery):
    V2 = types.InlineKeyboardMarkup(row_width=3)
    V2.add(VY1RR if callback.data == 'VModule2' else VY1BB,
           VY2RR if callback.data == 'V2_2' else VY2BB,
           VY3RR if callback.data == 'V2_3' else VY3BB,
           VY4RR if callback.data == 'V2_4' else VY4BB,
           VY5RR if callback.data == 'V2_5' else VY5BB,
           VY6RR if callback.data == 'V2_6' else VY6BB,
           VY7RR if callback.data == 'V2_7' else VY7BB,
           VY8RR if callback.data == 'V2_8' else VY8BB,
           VY9RR if callback.data == 'V2_9' else VY9BB,
           VY10RR if callback.data == 'V2_10' else VY10BB,
           VY11RR if callback.data == 'V2_11' else VY11BB,
           VY12RR if callback.data == 'V2_12' else VY12BB,
           AllMenu)
    await FSMAdmin.video2.set()
    await callback.message.edit_text(f'[{V2_dict()[callback.data][0]}]({V2_dict()[callback.data][1]})',
                                     reply_markup=V2)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in V3_dict()], state=FSMAdmin.video)
async def cb_video3(callback: types.CallbackQuery):
    V2 = types.InlineKeyboardMarkup(row_width=3)
    V2.add(V1Y1R  if callback.data == 'VModule3' else V1Y1B ,
           V1Y2R  if callback.data == 'V3_2' else V1Y2B ,
           V1Y3R  if callback.data == 'V3_3' else V1Y3B ,
           V1Y4R  if callback.data == 'V3_4' else V1Y4B ,
           V1Y5R  if callback.data == 'V3_5' else V1Y5B ,
           V1Y6R  if callback.data == 'V3_6' else V1Y6B ,
           V1Y7R  if callback.data == 'V3_7' else V1Y7B ,
           V1Y8R  if callback.data == 'V3_8' else V1Y8B ,
           V1Y9R  if callback.data == 'V3_9' else V1Y9B ,
           V1Y10R  if callback.data == 'V3_10' else V1Y10B ,
           V1Y11R  if callback.data == 'V3_11' else V1Y11B ,
           V1Y12R  if callback.data == 'V3_12' else V1Y12B ,
           AllMenu)
    await FSMAdmin.video3.set()
    await callback.message.edit_text(f'[{V3_dict()[callback.data][0]}]({V3_dict()[callback.data][1]})',
                                     reply_markup=V2)


# @dp.callback_query_handler(lambda x : x.data in [ i for i in V4_dict()], state=FSMAdmin.video)
async def cb_video4(callback: types.CallbackQuery):
    V4 = types.InlineKeyboardMarkup(row_width=3)
    V4.add(V1Y1RR  if callback.data == 'VModule4' else V1Y1BB ,
           V1Y2RR  if callback.data == 'V4_2' else V1Y2BB ,
           V1Y3RR  if callback.data == 'V4_3' else V1Y3BB ,
           V1Y4RR  if callback.data == 'V4_4' else V1Y4BB ,
           V1Y5RR  if callback.data == 'V4_5' else V1Y5BB ,
           V1Y6RR  if callback.data == 'V4_6' else V1Y6BB ,
           V1Y7RR  if callback.data == 'V4_7' else V1Y7BB ,
           V1Y8RR  if callback.data == 'V4_8' else V1Y8BB ,
           V1Y9RR  if callback.data == 'V4_9' else V1Y9BB ,
           V1Y10RR  if callback.data == 'V4_10' else V1Y10BB ,
           V1Y11RR  if callback.data == 'V4_11' else V1Y11BB ,
           V1Y12RR  if callback.data == 'V4_12' else V1Y12BB ,
           AllMenu)
    await FSMAdmin.video4.set()
    await callback.message.edit_text(f'[{V4_dict()[callback.data][0]}]({V4_dict()[callback.data][1]})',
                                     reply_markup=V4)


def register_handlers_video(dp : Dispatcher):
    dp.register_callback_query_handler(cb_video1, lambda x : x.data in [ i for i in V1_dict()], state=(FSMAdmin.video, FSMAdmin.video1))
    dp.register_callback_query_handler(cb_video2, lambda x : x.data in [ i for i in V2_dict()], state=(FSMAdmin.video, FSMAdmin.video2))
    dp.register_callback_query_handler(cb_video3, lambda x : x.data in [ i for i in V3_dict()], state=(FSMAdmin.video, FSMAdmin.video3))
    dp.register_callback_query_handler(cb_video4, lambda x : x.data in [ i for i in V4_dict()], state=(FSMAdmin.video, FSMAdmin.video4))