import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram.filters import Command, CommandStart


API_TOKEN = "7498193874:AAEWYp-jyQCRFMa0_DITrPgRjPUGQ1jZ-Js"

bot = Bot(token=API_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🙍🏻‍♂️ Men haqimda")],
        [KeyboardButton(text="✉️ Email")],
        [KeyboardButton(text="📄 Mening resumem")],
        [KeyboardButton(text="📞 Men bilan bog‘lanish")]
    ],
    resize_keyboard=True
)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Porfoli botga xush kelibsiz.",
        reply_markup=menu_buttons
    )
from aiogram.types import FSInputFile


@router.message(F.text)
async def handle_buttons(message: Message):
    text = message.text

    if text == "🙍🏻‍♂️ Men haqimda":
        await message.answer("Men Hamidov Doniyorbek. Python dasturlash tilida boshlang'ich dasturchiman. Telegram botlar, web ilovalar va boshqa loyihalar yarataman.")

    elif text == "✉️ Email":
        await message.answer("Mening email manzilim: <b>donyor6hamidov25@gmail.com</b>")

    elif text == "📄 Mening resumem":
        try:
            file = FSInputFile("resume.pdf")
            await message.answer_document(file, caption="📄 Mening resume faylim:")
        except FileNotFoundError:
            await message.answer("❌ Resume fayli topilmadi. Iltimos, keyinroq urinib ko'ring.")

    elif text == "📞 Men bilan bog‘lanish":
        await message.answer("Bog‘lanish uchun telefon raqamim: <b>+998 90 776 39 86</b>")
        await message.answer("Yoki Telegramm orqali: @bookmakerr")

    else:
        await message.answer("Iltimos, mavjud tugmalardan birini tanlang.")

@dp.message(Command("about"))
async def show_user_files(message: Message):
    await message.answer("Salom, ushbu botga sizga men haqimdagi ma'lumotlarni yuboradi.")

@dp.message(Command("help"))
async def show_user_files(message: Message):
    await message.answer("Savollar bo'yicha (@bookmakerr)ga murojat qilishingiz mumkin.")


dp.include_router(router)

async def main():
    print("Bot ishlamoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
