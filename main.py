import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN, ADMINS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def admin_button():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[[types.KeyboardButton(text="🛠 ADMIN PANEL")]]
    )

def admin_menu():
    return types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [types.KeyboardButton("👤 Foydalanuvchilar"), types.KeyboardButton("📊 Statistika")],
            [types.KeyboardButton("⭐ PRO qo‘shish"), types.KeyboardButton("🧑‍💼 Ishchi qo‘shish")],
            [types.KeyboardButton("❌ Ban"), types.KeyboardButton("📨 Xabar yuborish")],
            [types.KeyboardButton("🔙 Orqaga")]
        ]
    )

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer("Assalomu alaykum, admin!", reply_markup=admin_button())
    else:
        await message.answer("Assalomu alaykum! Men tayyorman.")

@dp.message(lambda m: m.text == "🛠 ADMIN PANEL")
async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMINS:
        return await message.answer("⛔ Siz adminsiz emassiz!")
    await message.answer("🛠 Admin paneli:", reply_markup=admin_menu())

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
