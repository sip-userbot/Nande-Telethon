""" Userbot module for other small commands. """
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await eor(event, get_string("hlpr_1").format(me.first_name)
    )


@ayiin_cmd(pattern="listvar$")
async def var(event):
    await eor(event, get_string("hlpr_2")
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  »  **Perintah :** `{cmd}ihelp`\
        \n  »  **Kegunaan : **Bantuan Untuk 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝.\
        \n\n  »  **Perintah :** `{cmd}listvar`\
        \n  »  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  »  **Perintah :** `{cmd}repo`\
        \n  »  **Kegunaan : **Melihat Repository 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝.\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **Link untuk mengambil String 𝙽𝚊𝚗𝚍𝚎 - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝.\
    "
    }
)
