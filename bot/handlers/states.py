from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    agreement = State()
    name = State()
    mail = State()
    phone = State()
    recorded = State()


class Admin(StatesGroup):
    date = State()
    description = State()
    time = State()
    key = State()
    url = State()





