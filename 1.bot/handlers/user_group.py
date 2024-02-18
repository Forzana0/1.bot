from filter.chat_types import ChatTypeFilter
from string import punctuation
from aiogram import Router, types
user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

banned_words={'ку','прив', 'пон', 'зроз'}

def clean_text(text:str):
    return text.translate(str.maketrans('','', punctuation)).lower()

@user_group_router.edited_message()
@user_group_router.message()
async def group_message(message: types.Message):
    if banned_words.intersection(message.text.lower().split()):
        await message.reply(clean_text(message.text))
        await message.answer(f"{message.from_user.full_name}, keep calm in the chat!")
    else:
        await message.answer(f"Hello to you{message.from_user.full_name}")
    # await message.reply(f"Hello user {message.from_user.full_name}, {message.text}")