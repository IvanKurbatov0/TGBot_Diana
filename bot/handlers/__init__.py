from aiogram import Router
from handlers.kb import KB
from handlers.conference import Conference
router = Router()
kb = KB()
conference = Conference()
users = []
from handlers import start_handlers, conf_handlers, admin_handlers