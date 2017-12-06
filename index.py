import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import MessageHandler,Filters
from telegram.ext import CommandHandler
import logging
from config import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
class Handlers:
    def start(bot,update):
        chat_id=update.message.chat_id
        markup=telegram.ReplyKeyboardMarkup(config.start_markup)
        bot.send_message(chat_id=update.message.chat_id,text="Здравствуйте, "+
        update.message.from_user.first_name+"!",reply_markup=markup)
    
    def handleCategories(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        bot.send_message(chat_id=update.message.chat_id,text="Выберите категорию",reply_markup=markup)
    def routeMessage(bot,update):
        if update.message.text=="Категории":
            Handlers.handleCategories(bot,update)
            return
        if update.message.text=="Добавить новый канал":
            Handlers.handleNewChannel(bot,update)
            return
        if update.message.text=="Музыка":
            Handlers.handleMusic(bot,update)
            return
        if update.message.text=="Вернутся в главное меню":
            Handlers.handleReturnToMain(bot,update)
            return
        if update.message.text=="Наука/Новости":
            Handlers.handleScience(bot,update)
            return
        if update.message.text=="Искусство":
            Handlers.handleArt(bot,update)
            return
        if update.message.text=="Полезное":
            Handlers.handleUseful(bot,update)
            return
        if update.message.text=="История":
            Handlers.handleHistory(bot,update)
            return
        else:
            bot.send_message(chat_id=update.message.chat_id,text="Не понимаю тебя")
            return
    ################################################################################
    def handleNewChannel(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        text=config.newChannel_text
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    def handleArt(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        text=config.art_text
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    def handleHistory(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        text=config.history_text
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    def handleUseful(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        text=config.useful_text
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    def handleScience(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        text=config.science_text
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    def handleReturnToMain(bot,update):
        markup=telegram.ReplyKeyboardMarkup(config.start_markup)
        bot.send_message(chat_id=update.message.chat_id,text="Выберите категорию",reply_markup=markup)
    def handleMusic(bot,update):
        text=config.music_text
        markup=telegram.ReplyKeyboardMarkup(config.categories_markup)
        bot.send_message(chat_id=update.message.chat_id,text=text,reply_markup=markup)
    #################################################################################

updater=Updater(config.bot_token)
dispatcher=updater.dispatcher

dispatcher.add_handler(CommandHandler("start",Handlers.start))
dispatcher.add_handler(MessageHandler(Filters.text,Handlers.routeMessage))
updater.start_polling()