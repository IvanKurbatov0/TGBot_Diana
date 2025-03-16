from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F
from bot.handlers import router, kb
from bot.handlers.states import Form
from bot.handlers.user import User
from bot.handlers import conference
from bot.handlers import users

@router.message(F.text.lower() == "записаться на конференцию")
async def agreement(msg: Message, state: FSMContext):
    if conference.date is None or conference.description is None:
        await msg.answer(text="В ближайшее время не запланировано конференций")
        return 0
    else:
        for user in users:
            if user.id == msg.from_user.id:
                await msg.answer(text=f"Вы уже записаны на конференцию {conference.date} в {str(conference.time).split()[1][:-3]}")
                return 0
        await msg.answer(text=f"{conference.description}. Дата: {conference.date}, время: {str(conference.time).split()[1][:-3]}.\nДля записи на конференцию введите своё ФИО", reply_markup=kb.cancel_btn)
        await state.set_state(Form.name)


@router.message(Form.name)
async def name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Form.mail)
    await msg.answer(text="Введите электронную почту", reply_markup=kb.cancel_btn)


@router.message(Form.mail)
async def mail(msg: Message, state: FSMContext):
    await state.update_data(mail=msg.text)
    await state.set_state(Form.phone)
    await msg.answer(text="Введите свой номер телефона", reply_markup=kb.cancel_btn)


@router.message(Form.phone)
async def phone(msg: Message, state: FSMContext):
    await state.update_data(phone=msg.text)
    await msg.answer(text="Подтвердите согласие на дальнейшую обработку персональных данных", reply_markup=kb.agreement)
    await state.set_state(Form.agreement)


@router.callback_query(F.data == "agreement")
@router.message(Form.agreement and F.text.lower() == "✅ Подтверждаю")
async def conf(clbck: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    for user in users:
        if user.id == clbck.from_user.id:
            return 0
    users.append(User(id=clbck.from_user.id, name=data.get('name', None), mail=data.get('mail', None), phone=data.get('phone', None)))
    await clbck.message.answer(text="Вы успешно записаны на конференцию.\nЗа час до начала конференции Вам придёт напоминание с кодом и ссылкой")
    await state.set_state(None)

