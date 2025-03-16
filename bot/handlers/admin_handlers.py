from os.path import split

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram import F
from pydantic.v1.validators import anystr_strip_whitespace

from handlers import conference
from handlers import router, kb, users
from bot import config
import re
import datetime

from handlers.start_handlers import start_handler
from handlers.states import Admin
from bot import bot
import asyncio


async def is_valid_date(msg):
    pattern = r"\d{2}.\d{2}.\d{4}"
    response = bool(re.match(pattern, msg))
    print(response)
    return response

async def is_valid_time(msg):
    pattern = r"\d{2}:\d{2}"
    response = bool(re.match(pattern, msg))
    return response

@router.message(Command('admin'))
async def get_admin_panel(msg: Message):
    if msg.from_user.id in config.ADMINS:
        await msg.answer(text="Выберите действие", reply_markup=kb.admin_menu)
    else:
        await msg.answer(text="Извините вы не являетесь администратором")

@router.message(lambda msg: msg.from_user.id in config.ADMINS, F.text.lower() == "создать конференцию")
async def create_conf(msg: Message, state: FSMContext):
    if conference.date is not None or conference.time is not None or conference.description is not None:
        await msg.answer(text="Вы уже создали конференцию")
        return 0
    await msg.answer(text="Введите дату конференции в формате дд.мм.гггг", reply_markup=kb.cancel_btn)
    await state.set_state(Admin.date)

@router.message(lambda msg: msg.from_user.id in config.ADMINS, Admin.date)
async def date(msg: Message, state: FSMContext):
    if await is_valid_date(msg.text):
        print(12345)
        await state.update_data(date=msg.text)
        await msg.answer(text="Введите время конференции в формате чч:мм", reply_markup=kb.cancel_btn)
        await state.set_state(Admin.time)
    else:
        await msg.answer(text="Вы неверно ввели дату. Введите дату конференции в формате дд.мм.гггг")

@router.message(lambda msg: msg.from_user.id in config.ADMINS, Admin.time)
async def time(msg: Message, state: FSMContext):
    if await is_valid_time(msg.text):
        await state.update_data(time=msg.text)
        await state.set_state(Admin.description)
        await msg.answer(text="Введите описание конференции", reply_markup=kb.cancel_btn)
    else:
        await msg.answer(text="Вы неверно ввели время. Введите время конференции в формате чч:мм")

async def reminder_users():
    while True:
        if conference.date == datetime.date.today():
            cur_time = datetime.datetime.now()
            if conference.time - cur_time <= datetime.timedelta(hours=1):
                for user in users:
                    if conference.key is not None and conference.url is not None:
                        await bot.send_message(user.id, f"Напоминаю, что вы записаны на конференцию, которая пройдёт сегодня в {str(conference.time).split()[1][:-3]}\nКлюч конференции: {conference.key}\nСсылка на конференцию: {conference.url}")
                users.clear()
                await conference.clear()
                break
            else:
                await asyncio.sleep(60*10)
        else:
            await asyncio.sleep(60*10)

async def reminder_admin():
    while True:
        if conference.date == datetime.date.today():
            cur_time = datetime.datetime.now()
            if conference.time - cur_time <= datetime.timedelta(hours=2):
                if conference.key is not None and conference.url is not None:
                    if conference.date is None or conference.time is None or conference.description is None:
                        break
                    break
                for i in range(len(config.ADMINS)):
                    await bot.send_message(config.ADMINS[i], "Напоминаю, что вы должны отправить ссылку и код на коференцию. Для отправки нажмите на соответсвующую кнопку")
                await asyncio.sleep(60*10)
            else:
                await asyncio.sleep(60*10)
        else:
            await asyncio.sleep(60*10)


@router.message(lambda msg: msg.from_user.id in config.ADMINS, Admin.description)
async def description(msg: Message, state: FSMContext):
    await state.update_data(description=msg.text)
    await state.set_state(None)
    data = await state.get_data()
    await conference.create(time=data.get('time'), date=data.get('date'), description=data.get('description'))
    await msg.answer(text=f"Вы успешно создали конференцию, запланированную на {data.get('date')} в {data.get('time')}.\nОписание: {data.get('description')}")
    asyncio.create_task(reminder_users())
    asyncio.create_task(reminder_admin())


@router.message(F.text.lower() == 'добавить ключ и ссылку на конференцию')
async def get_key_url(msg: Message, state: FSMContext):
    print(conference.key, conference.url)
    if conference.date is None or conference.description is None:
        await msg.answer(text="Не найдено созданных конференций")
        return 0
    if conference.key is not None and conference.url is not None:
        await msg.answer(text="Вы уже добавили ключ и ссылку на конференцию")
        return 0
    await msg.answer(text="Введите ссылку на коференцию", reply_markup=kb.cancel_btn)
    await state.set_state(Admin.url)


@router.message(Admin.url)
async def url(msg: Message, state: FSMContext):
    await state.update_data(url=msg.text)
    await msg.answer(text="Введите ключ конференции", reply_markup=kb.cancel_btn)
    await state.set_state(Admin.key)


@router.message(Admin.key)
async def key(msg: Message, state: FSMContext):
    data = await state.get_data()
    conference.url = data.get('url')
    conference.key = msg.text
    await msg.answer(text="Вы успешно добавили ключ и ссылку на конференцию")
    await state.set_state(None)

@router.message(F.text.lower() == "узнать кто записался на конференцию")
async def get_users(msg: Message):
    if conference.date is None or conference.description is None:
        await msg.answer(text="Не найдено созданных конференций")
        return 0
    if len(users) != 0:
        for user in users:
            await msg.answer(text=f"{user.name}\nНомер телефона: {user.phone}\nЭлектронная почта: {user.mail}")
    else:
        await msg.answer(text="Пока что никто не записался на конференцию")

@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await callback.message.answer(text="Отменено")

@router.message()
async def NotFound(msg:Message):
    await msg.answer(text="Извините, я вас не понимаю, попробуйте ещё раз")

