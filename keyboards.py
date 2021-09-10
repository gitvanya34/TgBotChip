from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_сategories = KeyboardButton('Категории🧢👚👖🥾')
button_search = KeyboardButton('Поиск🔍')
button_back = KeyboardButton('Назад')
button_exit = KeyboardButton('В главное меню')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_сategories, button_search, button_back, button_exit)


button_hats = KeyboardButton('Головные уборы🧢')
button_tshirts = KeyboardButton('Футболки👚')
button_hoodies = KeyboardButton('Худи👚')
button_pants = KeyboardButton('Брюки👖')
button_shoes = KeyboardButton('Обувь🥾')
button_back = KeyboardButton('Назад')
button_exit = KeyboardButton('В главное меню')
сategories_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hats, button_tshirts,button_hoodies,button_pants, button_shoes,button_back,button_exit)


button_model = KeyboardButton('Выбрать модель')
button_size = KeyboardButton('Размер')
button_pay = KeyboardButton('Оплатить')
button_back = KeyboardButton('Назад')
button_exit = KeyboardButton('В главное меню')
product_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_model,button_size,button_pay, button_back, button_exit )


# greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_hi)
