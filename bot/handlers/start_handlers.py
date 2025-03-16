from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from bot.handlers import router, kb


@router.message(Command("start"))
async def start_handler(msg: Message):
    print(msg.from_user.id)
    await msg.answer(f"Здравствуйте, {msg.from_user.full_name}! 👋\n\nВас приветствует бухгалтерский центр Дианы Царбаевой! Мы помогаем вашему бизнесу уже более 20 лет и за последний год сэкономили 30 миллионов рублей своим клиентам.\n\n📍Здесь Вы можете подробнее узнать о бухгалтерском центре Дианы Царбаевой и предоставляемых услугах, а также записаться на консультацию",
                     reply_markup=kb.start_menu)


@router.message(F.text.lower() == "о компании")
async def about_company(msg: Message):
    await msg.answer_video(video="BAACAgIAAxkBAAIB8Wc4hojb07b4MNWQEPSKoqagMLgqAALoWgACD0XJSWTue4_biQE4NgQ", caption="✅ <b>У нас более 140 клиентов на обслуживании</b>\n\n✅ <b>Мы сэкономили 30 миллионов рублей за последний год</b>\n\n✅ <b>Имеем 24 года непрерывного опыта</b>\n\n✅ <b>1000+ консультаций</b>\n\n✅ <b>5000+ решённых вопросов</b>\n\n✅ <b>Законно снижаем налоги и уменьшаем расходы вашего бизнеса</b>")


@router.message(F.text.lower() == "об услугах")
async def about_services(msg: Message):
    await msg.answer(text="Выберите необходимый тип услуги", reply_markup=kb.services_menu)


@router.message(F.text.lower() == "бухгалтерские услуги")
async def service_1(msg: Message):
    await msg.answer(text="✅ Полное бухгалтерское обслуживание ООО и ИП\n\n✅ Решаем проблемы с налоговой\n\n✅ Ответы на требования\n\n✅ Кадровый учет\n\n✅ Расчет зарплаты, налогов и взносов\n\n✅ Оформление первичных документов\n\n✅ Составление и сдача отчетности в налоговые органы, внебюджетные фонды, органы статистики, другие государственные органы")


@router.message(F.text.lower() == "регистрационные действия")
async def service_2(msg: Message):
    await msg.answer(text="✅ Регистрация ООО и ИП\n\n✅ Закрытие ИП\n\n✅ Ликвидация ООО\n\n✅ Подбор ОКВЭД\n\n✅ Открытие расчетных счетов")


@router.message(F.text.lower() == "аудит")
async def service_3(msg: Message):
    await msg.answer(text="✅ Восстановление учета\n\n✅ Аудит бухгалтерской базы 1С\n\n")


@router.message(F.text.lower() == "консультирование")
async def service_4(msg: Message):
    await msg.answer(text="✅ Подбор кассы, эквайринга и системы платежей\n\n✅ Консультации по бухгалтерскому и налоговому учету\n\n✅ Консультации по подбору правильной системы налогообложения\n\n✅ Консультации по оформлению сотрудников")


@router.message(F.text.lower() == "разовые услуги")
async def service_4(msg :Message):
    await msg.answer(text="✅ Сопровождение налоговых проверок\n\n✅ Контроль и подготовка платежных поручений на уплату налогов, взносов\n\n✅ Любой другой комплекс бухгалтерских услуг")


@router.message(F.text.lower() == "⬅️ вернуться назад")
async def exit(msg: Message):
    await msg.answer(text='Вы вернулись назад', reply_markup=kb.start_menu)


@router.message(F.text.lower() == "записаться на консультацию")
async def consultation(msg: Message):
    await msg.answer(text="Для записи нажмите кнопку ниже\n\nTelegram канал: https://t.me/diana_nalog\n\nVK: https://vk.com/club73536707\n\nYouTube: https://youtube.com/@DIANA_CZARBAEBA?si=rZOPSh0BtTZN-AC5",
                     reply_markup=kb.sign_up)


@router.message(F.text.lower() == "сотрудничество")
async def cooperation(msg: Message):
    await msg.answer(text="✨ СОТРУДНИЧЕСТВО ✨\n\nЯ предлагаю вам денежное вознаграждение за рекомендацию меня как специалиста:\n\nВы рекомендуете меня, а при заключении договора с новым клиентом от вас вы получаете  50% оплаты за первый месяц обслуживания лично от меня 🤝\n\nПравила:\n\n1️⃣ Кто-то из ваших знакомых находится в поиске хорошего бухгалтера\n\n2️⃣ Вы даете ему мои контакты\n\n3️⃣ Мы созваниваемся, договариваемся об обслуживании, согласовав стоимость\n\n4️⃣ Как только я получаю оплату за первый месяц обслуживания (например, 10 000 руб.), 50%, то есть 5 000 руб. перевожу вам\n\n‼️ У меня есть специальная форма договора, разработанная юристом, специально для нашего сотрудничества\n\n‼️ Обязательно сообщите, что клиент от вас")


@router.message(F.text.lower() == "как добраться")
async def offices(msg: Message):
    await msg.answer(text="Какой офис Вас интересует?", reply_markup=kb.offices_menu)


@router.message(F.text.lower() == "ул. будапешская, д. 97, корп 2")
async def send_video_office1(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIEVmc_JS4sHL17zSjPz8K5rJxKA95bAAJ7VgACOW_4SeeFNRwDHP80NgQ")

@router.message(F.text.lower() == "балканская площадь, 5ад")
async def send_video_office2(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIEV2c_JmCCOOhqtEGBSTrPlA0VQJ7GAAKJVgACOW_4ScHL5In4eXWSNgQ")


# @router.message(F.text.lower == "" or F.text.lower() == )
# def offices_video(msg: Message):
#     await msg.answer_video()

# @router.message()
# async def get_video(msg: Message):
#     print(msg.video.file_id)
