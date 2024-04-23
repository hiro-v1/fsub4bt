from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="• ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ •", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink3),
                InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• ᴛᴜᴛᴜᴘ •", callback_data="close"),
            ],
        ]
        return buttons

def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and FORCE_SUB_CHANNEL4:
        buttons = [
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink3),
                InlineKeyboardButton(text="𝗝𝗼𝗶𝗻 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons