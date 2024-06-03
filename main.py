from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_1_inline, get_keyboard_2_inline
from datetime import datetime


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Предсказние')
async def button_1_click(message: types.Message):
    await message.answer('Через 3 дня случиться что-то очень хорошее')


@dp.message_handler(lambda message: message.text == 'Чистая правда')
async def button_2_click(message: types.Message):
    await message.answer('Ты выглядишь шикарно')

@dp.message_handler(lambda message: message.text == 'Отправь фото BMW M5')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://avatars.mds.yandex.net/get-verba/787013/2a00000160984840410e310d545cdba95902/auto_main', caption='Вот тебе BMW M5', reply_markup=get_keyboard_1_inline())


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь узнать информацию, а также купить машину RAM', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Кнопка 4')
async def button_4_click(message: types.Message):
    await message.answer('Ты нажал кнопку 2')

@dp.message_handler(lambda message: message.text == 'Отправь фото RAM')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsaqrq3Se0q7HqObm3G9fQCgglosiWhHEB2g&s', caption='Вот тебе RAM', reply_markup=get_keyboard_2_inline())

@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def random_number(callback_query: types.CallbackQuery):
    curent_time = datetime.now()
    await callback_query.message.answer(f'Текущее время: { curent_time }',  callback_data='send_datetime', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить бота отправить фото BMW M5', reply_markup=get_keyboard_1())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)