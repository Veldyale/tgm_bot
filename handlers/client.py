from aiogram import types, Dispatcher
from create_bot import bot, dp

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Че хотел?')
        await message.delete()
    except:
        await message.reply('Подключи нашего робота: https://t.me/AvertnBot')
        await message.delete()


async def show_operating_hours(message : types.Message):
        await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 20:00\nСб-Вс с 9:00 до 18:00')
        await message.delete()


async def show_address(message : types.Message):
        await bot.send_message(message.from_user.id, 'Проспект Нариманова д.44 офис 6')
        await message.delete()


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(show_operating_hours, commands=['operating_hours'])
    dp.register_message_handler(show_address, commands=['address'])