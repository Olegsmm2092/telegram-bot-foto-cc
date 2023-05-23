from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_resize_keyboard():
    # keyboard = [
    #     [
    #         InlineKeyboardButton("100x100", callback_data="100 100"),
    #         InlineKeyboardButton("100x100", callback_data="200 200"),
    #         InlineKeyboardButton("100x100", callback_data="300 300"),
    #     ]
    # ]
    keyboard = [

        [
            InlineKeyboardButton('Scroll Left', callback_data='scroll_left'),
            InlineKeyboardButton('Scroll Right', callback_data='scroll_right')
        ],
        [
            InlineKeyboardButton(dfs('100', n)) for n in range(1, 3 + 1)
        ],
        [
            InlineKeyboardButton('Back', callback_data='back')
        ]
    ]


def dfs(geometry, n):
    size = int(geometry) * n
    return f"{size}x{size}", f"{size} {size}"
