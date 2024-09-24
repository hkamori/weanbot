import telebot
from openai import OpenAI
import time

client = OpenAI(api_key='key')
bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет *{message.from_user.first_name}*! 👋🤖\n'
    mess2 = f'*Что я умею?* ✨\n\n⋅ Отвечать на вопросы с использованием эмодзи.\n⋅ Переводить тексты на разные языки.\n⋅ Помогать в написании кода.\n⋅ Создавать тексты по запросу.\n⋅ Помогать с уроками и обучением.\n⋅ Выполнять поиск информации по заданным вопросам.\n⋅ Чтобы узнать список команд, просто введите *"/help"* 🤖🌐'
    bot.send_message(message.chat.id, mess, parse_mode= "Markdown")
    bot.send_message(message.chat.id, mess2, parse_mode= "Markdown")

@bot.message_handler(commands=['help'])
def help(message):
    mess_help = f'*Команды* 🎆\n\n⋅ */ai* | Классический ИИ 🤖\n⋅ */emoji* | ИИ отвечает в эмодзи ✨\n⋅ */translate* | Переводчик 🎀'
    bot.send_message(message.chat.id, mess_help, parse_mode= "Markdown")

@bot.message_handler(commands=['emoji'])
def emoji(message):
    result = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a message, and your task is to respond using emojis only, dont use text, only emojis."
        },
        {
        "role": "user",
        "content": result
        }
    ],
    temperature=0.8,
    max_tokens=64,
    top_p=1
    )
    print(f'{result} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode= "html")


@bot.message_handler(commands=['ai'])
def ai(message):
    result2 = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a message, and your task is to respond."
        },
        {
        "role": "user",
        "content": result2
        }
    ],
    temperature=0
    )
    print(f'{result2} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode="html")

@bot.message_handler(commands=['translate'])
def translate(message):
    result = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a, and your task is to translate it into language that user request, but send only a translated sentence without languages user request."
        },
        {
        "role": "user",
        "content": result
        }
    ],
    temperature=0.7
    )
    print(f'{result} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode= "html")

@bot.message_handler(commands=['joke'])
def joke(message):
    result = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a topic, and your task is to make a joke with this topic in ukrainian."
        },
        {
        "role": "user",
        "content": result
        }
    ],
    temperature=0.7
    )
    print(f'{result} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode= "html")


bot.polling(none_stop=True)
