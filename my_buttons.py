from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


admins_menu = ReplyKeyboardMarkup(resize_keyboard=True)

admins_menu.add(KeyboardButton('Zat qosiw'),
                KeyboardButton(text='Zakazlar'),
                KeyboardButton(text='Xabar jiberiw'),
                KeyboardButton('Menu')
                )

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='Menu'),
         KeyboardButton(text='Contacts'),
         KeyboardButton(text='Location'))

zat_qosiw_menu = ReplyKeyboardMarkup(resize_keyboard=True)
zat_qosiw_menu.add(KeyboardButton(text='Fast food'),
                   KeyboardButton(text='Hot food'),
                   KeyboardButton(text='Drinks'))
qoriw = ReplyKeyboardMarkup(resize_keyboard=True)
qoriw.add(KeyboardButton(text='Fast food qoriw'),
                   KeyboardButton(text='Hot food qoriw'),
                   KeyboardButton(text='Drinks qoriw'))
reg_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
reg_buttons.add(KeyboardButton('start form'))
reg = ReplyKeyboardMarkup(resize_keyboard=True)
reg.add(KeyboardButton('Registration'))