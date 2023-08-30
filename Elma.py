# MIT License

# Copyright (c) 2023 ttwiz_z

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.




from asyncio import sleep
from disnake.ext import commands
from disnake import Intents
from disnake import Activity
from disnake import ActivityType
from disnake.utils import get
from disnake import User

bot = commands.InteractionBot(intents = Intents.all())

@bot.event
async def on_command_error(_, exception):
    try:
        if isinstance(exception, commands.errors.CommandNotFound):
            return None
    except:
        pass

@bot.event
async def on_ready():
    try:
        await bot.change_presence(activity = Activity(type = ActivityType.watching, name = "/help"))
        print(f"{bot.user} онлайн!")
    except:
        pass

@bot.slash_command(description = "Предоставляет документацию.")
async def help(inter):
    try:
        await inter.response.send_message("""
**Эльма** – простой в использовании бот, служащий для верификации пользователей.

Добавить на сервер:
__https://clck.ru/34Z8Ar__

Команды:
`/setup` – активирует бота, для использования этой команды требуются права администратора.
`/verify <user>` – верифицирует пользователя. Пример использования: (`ttwiz_z` : `/verify @ttwiz_z`), (`_.elma._` : `/verify @_.elma._`).

Бот разработан `ttwiz_z`.
        """)
        await sleep(1)
        await inter.edit_original_response(suppress_embeds = True)
    except:
        await inter.response.send_message("Что-то пошло не так…")

@bot.slash_command(description = "Активирует бота.", dm_permission = False, default_member_permissions = 8)
async def setup(inter):
    try:
        if get(inter.guild.roles, name = "Верифицированный"):
            await inter.response.send_message("Бот уже активирован!")
        else:
            await inter.guild.create_role(name = "Верифицированный", reason = "Бот успешно активирован!")
            await inter.response.send_message("Бот успешно активирован!")
    except:
        await inter.response.send_message("Что-то пошло не так…")

@bot.slash_command(description = "Верифицирует пользователя.", dm_permission = False)
async def verify(inter, user : User):
    try:
        if user and user == inter.author:
            if get(inter.guild.roles, name = "Верифицированный"):
                if get(inter.guild.roles, name = "Верифицированный") in inter.author.roles:
                    await inter.response.send_message("Вы уже верифицированы!")
                else:
                    await inter.author.add_roles(get(inter.guild.roles, name = "Верифицированный"), reason = "Пользователь успешно верифицирован!")
                    await inter.response.send_message("Вы успешно верифицированы!")
            else:
                await inter.response.send_message("Бот не активирован! Для его активации нужно прописать команду `/setup` (требуются права администратора).")
        else:
            await inter.response.send_message("Для прохождения верификации Вы должны упомянуть себя!")
    except:
        await inter.response.send_message("Что-то пошло не так…")

bot.run("TOKEN")