#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki


from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlexaMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["S_B_1"], callback_data=f"settings_back_helper")]
    second = [
        InlineKeyboardButton(
            text=_["S_B_8"],
            callback_data="settingsback_helper",
        ),
        InlineKeyboardButton(text=_["S_B_1"], callback_data=f"settings_back_helper"),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ اوامر القنوات ›",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر المجموعات ›",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر بالانگليزي ›",
                    callback_data="help_callback hb3",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_8"],
                    callback_data=f"settingsback_helper",
                ),
                InlineKeyboardButton(text=_["S_B_1"], callback_data=f"settings_back_helper"),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
