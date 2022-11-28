# -*- coding: UTF-8 -*-
#Bot B_Votson Team, Project "Yumi Tyan v2"
#Open Code license

import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

users = [' @B_Votson', ' @V0tson', " @hallgheen", ' @Kob2n4ik', '@ahahahhaggajahahH']
roles = ["Kerry -", "Mid -", "Offlayner -", "Support -", "Full-Support -"]
hero = ['Abaddon', 'Alchemist', 'Ancient Apparition', 'AntiMage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight', 'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dawnbreaker', 'Dazzle', 'Death Prophet', 'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit', 'Enchantress', 'Enigma', 'Faceless Void', 'Grimstroke', 'Gyrocopter', 'Hoodwink', 'Huskar', 'Invoker', 'Io', 'Jakiro', 'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion', 'Lone Driud', 'Luna', 'Lycan', 'Magnus', 'Mars', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', "Nature's Prophet", 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight', 'Oracle', 'Outworld Destroyer', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Puck', 'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Snapfire', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit', 'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector', 'Troll Warlord', 'Tusk', 'Underlord', 'Undying', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Visage', 'Void Spirit', 'Warlock', 'Weaver', 'Windranger', 'Winter Wywern', 'Witch Doctor', 'Wraith King', 'Zeus']

def shuffleall():
    random.shuffle(users)
    random.shuffle(roles)
    random.shuffle(hero)
    


#TOKEN
TOKEN = "5611167409:AAG4hz_IJGWNyh0fO3S8B2sxrM59Y1xSVwM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
genders = ['Полудибил', 'Националист', 'Ядерный Автобус', 'Полуфабрикат', 'Автомат ак-47', 'Гей', 'Автономная станция', 'анальный шарик жириновского', 'памперс', 'кто то', 'миша', 'вещь', 'Ботяра обоссаный', 'финалист порно-кастинга', 'Питонист', 'мастер по минету', 'анальный мудрец', 'оффник', 'бущенка ванючая', "ватная палочка", "крыса подвальная"]
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Ну че?')


@dp.message_handler(commands=['randomhero'])

async def randomdraft(msg: types.Message):
    await msg.answer("Случайный герой: " + hero[random.randint(0,  121)])



@dp.message_handler(commands=['randomdraft'])

async def randomdraft(msg: types.Message):
    shuffleall()
    await msg.answer("Случайный драфт предложеный ботом(все герои выбраны случайно)")
    await msg.answer("Керри: " + hero[random.randint(0,  121)] + '\n Мидер: ' + hero[random.randint(0, 121)] + '\n Оффлейнер: ' + hero[random.randint(0,  121)] + '\n Сапорт: ' + hero[random.randint(0,  121)] + '\n Сапорт 5-ка: ' + hero[random.randint(0,  121)])
    
@dp.message_handler(commands=['whatgender'])
async def send_gender(msg: types.Message):
    await msg.reply('Сегодня вы: ' + genders[random.randint(0, 21)] + " по гендеру!")
@dp.message_handler(commands=['whatrole'])


async def send_roles(msg: types.Message):
    shuffleall()
    await msg.answer("Роли были полностью рандомно выбраны ботом. \n1) " + roles[0] + " - " + users[0] + " \n2) " + roles[1] + " - " + users[1] + "\n3) " + roles[2] + " - " + users[2] + "\n 4) " + roles[3] + " - " + users[3] + '\n 5) ' + roles[4] + ' - ' + users[4])

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    


    


    #if msg.text.lower() == 'пруфай':
    #    await msg.reply("Пруфать будешь у своей мамаши покойной, а тут доказывают")
    
    #if msg.text.lower() == 'пошел нахуй':
    #    await msg.reply("Соси хуй даун")

    
    if msg.text.lower() == '/whatdota':
        await msg.answer("Функция заменена на /randomhero и /randomdraft")
    
    
    
    if msg.text.lower() == '/test':
        await msg.reply("test", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test", web_app=WebAppInfo(url="https://google.com"))))

    if msg.text.lower() == '/offabot':
        if msg.chat.id == 936106535:
            await msg.answer('Бот выключен. Для включения перезагрузите скрипт bot.py')
            exit()
        if msg.chat.id != 936106535:
            await msg.answer("Только разроботчик может полностю выключить скрипт!")
    if msg.text.lower() == '/outcode':
        
        await msg.answer('Исходный код бота вы всегда можете найти на сайте: http://bvotson.byethost7.com')

    if msg.text.lower() == '/isgay':
        #if random.randint(0, 1) == 1: 
        #    await msg.reply('Да, он определенно гей!')
        #else:
        #    await msg.reply("Нет, он не гей, он явно долбоеб!")
        await msg.reply("Функция была временно отключена. За подробностями обратитесь к разработчику")
    if msg.text.lower() == '/howitdo':
        await msg.reply("Бот был написан B_Votson Team, весь код есть в открытом доступе на сайте. Написан на python, хостинг: heruko") 
    
    if msg.text.lower() == '/report':
        await msg.reply("Функция была отключена.")
        
    if msg.text.lower() == '/helpbvh':
        await msg.reply('Что бы настроить отправку в телеграм вам нужно:')
        await msg.reply('1) Отправить "/newbot" боту @BotFather')
        await msg.reply('2) Кинуть токен в соотвествуещее окно')
        await msg.reply('3) Написать мне /chatid что бы узнать свой чат ид')
        await msg.reply('4) Написать этот ид в другую строку в скрипте')
        await msg.reply('5) Нажать "СОХРАНИТЬ НАСТРОЙКИ')
    
    if msg.text.lower() == "/chatid":
      cid = msg.chat.id
      await msg.answer(cid)
    
if __name__ == '__main__':
   executor.start_polling(dp)
   
