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
        \n\n  ยป  **Perintah :** `{cmd}ihelp`\
        \n  ยป  **Kegunaan : **Bantuan Untuk ๐ฝ๐๐๐๐ - ๐๐๐๐๐๐๐.\
        \n\n  ยป  **Perintah :** `{cmd}listvar`\
        \n  ยป  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  ยป  **Perintah :** `{cmd}repo`\
        \n  ยป  **Kegunaan : **Melihat Repository ๐ฝ๐๐๐๐ - ๐๐๐๐๐๐๐.\
        \n\n  ยป  **Perintah :** `{cmd}string`\
        \n  ยป  **Kegunaan : **Link untuk mengambil String ๐ฝ๐๐๐๐ - ๐๐๐๐๐๐๐.\
    "
    }
)
