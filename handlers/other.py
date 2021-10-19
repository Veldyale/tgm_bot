from aiogram import types, Dispatcher

import json, string


async def echo_end(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Я тебе сейчас БЛЯТЬ поматерюсь 🤬!')
        # await bot.send_message(message.from_user.id, 'Мат запрещен!')
        await message.delete()


def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_end)