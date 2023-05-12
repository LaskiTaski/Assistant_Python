from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from dotenv import load_dotenv
import os

load_dotenv()


storage = MemoryStorage()


TOKEN = os.getenv('TOKEN_API')

bot = Bot(token=TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot, storage= storage)