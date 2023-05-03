from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('Main')

# --- Main Menu ---
btnMenu = KeyboardButton('📋Menu')
btnCart = KeyboardButton('🛒Basket')
btnDoneCart = KeyboardButton('✅Done Cart')
btnContact = KeyboardButton('👨🏻‍💻Contact')
btnAboutUs = KeyboardButton('💬️About Us')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu, btnCart, btnDoneCart, btnContact, btnAboutUs)
