import asyncio

from aiogram import Bot, Dispatcher
from handlers import u_router, o_router
from config_data.config import load_config


async def main():
    config = load_config()
    bot = Bot(token=config.bot.token,
              parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(u_router)
    dp.include_router(o_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
