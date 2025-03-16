from aiogram import Router
from bot.handlers.kb import KB
from bot.handlers.conference import Conference
router = Router()
kb = KB()
conference = Conference()
users = []
from bot.handlers import start_handlers, conf_handlers, admin_handlers