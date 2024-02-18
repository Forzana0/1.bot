from filter.chat_types import ChatTypeFilter

from aiogram import Router, types
user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_group_router.message()
async def group_message(message: types.Message):
    await message.reply(f"Hello user {message.from_user.full_name}, {message.text}")