from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("✅ Бот работает! Привет!")

@router.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")