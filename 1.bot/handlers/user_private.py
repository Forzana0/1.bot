from aiogram.filters import CommandStart, Command
from aiogram import types, Router
import random

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Hello my dear friend {message.from_user.full_name}. I am your personal TG Bot")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Menu : \n1. /menu \n2. /help \n3. /echo \n4. /start")


@user_private_router.message()
async def echo(message: types.Message):
    hello = random.choice(["hello", "Hi", "привіт"])
    byebye = random.choice(["bye", "Goodbye", "пака"])
    text = message.text
    if text in ['hi', 'hello', 'привіт']:
        await message.answer(f"{hello} {message.from_user.full_name}")
    elif text in ['goodbay', 'bay',]:
        await message.answer(f"{byebye}{message.from_user.full_name}")
    else:
        await message.reply("I do not understand you")