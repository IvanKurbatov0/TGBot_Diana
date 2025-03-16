from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

class KB:
    def __init__(self):
        self.start_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="О компании"), KeyboardButton(text="Об услугах")],
                                                         [KeyboardButton(text="Записаться на консультацию"), KeyboardButton(text="Как добраться")],
                                                         [KeyboardButton(text="Записаться на конференцию")],],
                                              resize_keyboard=True)

        self.services_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Бухгалтерские услуги"),KeyboardButton(text="Регистрационные действия")],
                                                           [KeyboardButton(text="Аудит"), KeyboardButton(text="Консультирование")],
                                                           [KeyboardButton(text="Разовые услуги"), KeyboardButton(text="⬅️ Вернуться назад")]],
                                                 resize_keyboard=True)

        self.back_btn = InlineKeyboardButton(text="⬅️ Вернуться назад", callback_data="back")

        self.cancel_btn = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="❌ Отмена", callback_data='cancel')]])

        self.agreement = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="✅ Подтверждаю", callback_data="agreement")],
                                                               [InlineKeyboardButton(text="❌ Отмена", callback_data='cancel')]])

        self.sign_up = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Записаться", url="https://t.me/Diana_nalogi", callback_data="sign_up")]])

        self.admin_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Создать конференцию"), KeyboardButton(text="Узнать кто записался на конференцию")],
                                                        [KeyboardButton(text="Добавить ключ и ссылку на конференцию")]],
                                              resize_keyboard=True)

        self.offices_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="ул. Будапешская, д. 97, корп 2"), KeyboardButton(text="Балканская площадь, 5АД")],
                                                          [KeyboardButton(text="⬅️ Вернуться назад")]],
                                                resize_keyboard=True)

