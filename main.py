from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_1_inline, get_keyboard_2_inline

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Кнопка 1')
async def button_1_click(message: types.Message):
    await message.answer('Ты нажал кнопку 1')


@dp.message_handler(lambda message: message.text == 'Кнопка 2')
async def button_2_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://icdn.lenta.ru/images/2023/11/28/16/20231128163903784/square_1280_283df4079b9b28cab0e06492462f760a.jpeg', caption='Вот тебе кошка', reply_markup=get_keyboard_1_inline())


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото хомяка', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Кнопка 4')
async def button_4_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото хомяка')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://zoolike.by/image/cache/data/from_url/v-nashem-dome-poselilsya-zamechatelnyj-homyak-170104102151-906698009503420-49444-500x500.jpg', caption='Вот тебе хомяк', reply_markup=get_keyboard_2_inline())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото  кошки', reply_markup=get_keyboard_1())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)