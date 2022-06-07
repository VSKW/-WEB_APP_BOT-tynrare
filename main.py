from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '5452578219:AAEYyZ0zwjBzH87VIDDMwScSsso0Hvn2NLo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer('Даров, изай меню в левом нижнем углу')

@dp.message_handler(commands="games")
async def games(msg: types.Message):
    await msg.answer('ТакиеЕстьИгры:')
    
    photo = open("img/chiken.png", 'rb')
    await bot.send_photo(chat_id=msg.chat.id, photo=photo, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="запустить ЭТО", web_app=WebAppInfo(url="https://play.tynrare.net/"))))
    
    photo2 = open("img/page not found.png", 'rb')
    await bot.send_photo(chat_id=msg.chat.id, photo=photo2, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="запустить ЭТО", web_app=WebAppInfo(url="https://www.tynrare.net/apps/experiments/shaders/f/"))))
    
    photo3 = open("img/some shit.png", 'rb')
    await bot.send_photo(chat_id=msg.chat.id, photo=photo3, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="запустить ЭТО", web_app=WebAppInfo(url="https://www.tynrare.net/apps/experiments/shaders/a/"))))
    await msg.answer("A", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Я ХОЧУ СМОТРЕТЬ РЕКЛАМУ@", web_app=WebAppInfo(url="https://natribu.org/ru/"))))  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)