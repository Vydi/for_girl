import asyncio
from datetime import datetime

from config import TOKEN_BOT, admin
from aiogram import Bot, Dispatcher, executor, types
from my_parser import post_for_tg, add_subb, all_sub_f
import random

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)

posts_arr = post_for_tg()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Любимка моя, чтоб не скучала \u2764\uFE0F')
    if str(message.from_user.id) != admin:
        print('not mine')
        add_subb(message.from_user.id)
    else:
        print('admin!')


async def posts(wait_for=10):
    while True:
        subscribers = all_sub_f()
        print(subscribers)
        await asyncio.sleep(wait_for)
        for i in subscribers:
            await bot.send_message(i, text=random.choice(posts_arr))
            print('------------------------------------------', datetime.now(), i)


# запускаем лонг поллинг
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(posts())
    executor.start_polling(dp, skip_updates=True)
