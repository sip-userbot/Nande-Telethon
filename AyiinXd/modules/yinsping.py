# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================Γ========================
#            Jangan Hapus Credit Ngentod
# ========================Γ========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**πππππ§ ππ€π£π ππ€π** π",
    "**πππππ§ πππ π πππ£π©ππ£π** π",
    "**ππͺπ πππππ§ πΎπ€π£π©π€π‘** π",
    "**ππͺπ πππππ§ πππ£π©ππ£π** π₯΅",
    "**πππππ§ ππππ** π",
    "**ππͺπ πππππ§ πΌπππ£π** π₯Ί",
    "**ππ πΎππ ππ₯ πππππ§ π½ππ£π** π",
    "**Hadir kak maap telat** π₯Ί",
    "**Hadir Tuan** ππ»",
    "**Hadir Majikan** ππ»",
    "**Hadir Sayang** π³",
    "**Hadir Bro Nande** π",
    "**maaf ka habis nemenin ka Nandee** π₯Ί",
    "**maaf ka habis disuruh Tuan Nandee** π₯Ίππ»",
    "**Hadir Sayang** π"
    "**Hadir Nande Akuuuuhhh** βΊοΈ",
    "**Hadir Nande brother Aku** π₯°",
]

pacar = [
    "**Kamu mau jadi pacar aku ga?** π",
    "**Memek mending sama aku** π",
    "**Hai ganteng** π·",
    "**Mau ga bang jadi pacar aku?** π",
    "**Mending pc aku bang** π₯Ί",
    "**Ngewe Sama Aku yuk**π₯΅π₯΅π¦",
    "**Kly Mau Aku Crotin??**π₯΅",
    "**kly Mau Aku Sepongin??**",
    "**kly Aku Sayang Kamu ,Mwahhhπ**",
]

salam = [
    "**Wa'alaikumsalam ganteng** π₯°π₯°",
    "**Wa'alaikumsalam WR WB** ππ»",
    "**Iyah Waalaikusalam** π₯΅",
    "**Wa'alaikumsalam bang**",
    "**Wa'alaikumsalam** π₯°",
    "**Wa'alaikumsalan Warohmatullohi Wabarokatu**",
    "**Wa'alaikumsalam Ustad**",
]

ayiincakep = [
    "**ππ?π πππ£π©ππ£π π½ππ£πππ©** π",
    "**πππ£π©ππ£ππ£π?π πππ  πΌππ πππ¬ππ£** π",
    "**π ππ’πͺ πππ£π©ππ£ππ£π?π πΌπ πͺ πππ£** π",
    "**ππ?ππ ππππ πππ π¨πππ£π** π",
    "**π ππ’πͺ πππ’ππ© πππ₯π π½π€π€π£π** π",
]


@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**γ± π½ππππ - πππππππ γ±**\n\nβ§ **α΄ΙͺΙ΄Ι’α΄Κ :** `{} ms`\nβ§ **α΄α΄α΄Ιͺα΄α΄ :** `{}`\nβ§ **α΄α΄‘Ι΄α΄Κ :** `{}`\nβ§ **Ιͺα΄ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK π‘
# JANGAN DI HAPUS GOBLOK π‘ LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA π₯΄ GUA TANDAIN LU AKUN TELENYA π‘

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^Absen$")
async def ayiinabsen(ganteng):
    await ganteng.reply(choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^Aku ganteng kan$")
async def ayiin(ganteng):
    await ganteng.reply(choice(ayiincakep))

@register(incoming=True, from_users=DEVS, pattern=r"^kly$")
async def ayiin(kly):
    await kly.reply(choice(pacar))

@register(incoming=True, from_users=DEVS, pattern=r"^dancok$")
async def ayiin(yeuh):
    await yeuh.reply(choice(salam))

# ========================Γ========================
#            Jangan Hapus Credit Ngentod
# ========================Γ========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `yinsping`\
        \n\n  Β»  **Perintah : **`Perintah Ini Hanya Untuk Devs π½ππππ - πππππππ Tod.`\
        \n  Β»  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
