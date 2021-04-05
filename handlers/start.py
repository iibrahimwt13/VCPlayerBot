from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba🥳 {message.from_user.first_name}!
Ben Wyline Music Bot, Telegram gruplarınızda müzik çalmanıza izin veren bir botum. 
@zeus0901 ❤ tarafından korunur
Hakkımda daha fazla şey öğrenmek için aşağıdaki düğmeleri kullanın.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Komutlar", url="https://t.me/WylineVoiceHelp/2",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grup", url="https://t.me/OlympusCh4t"
                    ),
                    InlineKeyboardButton(
                      "📢Support Kanal", url="https://t.me/WylineVoiceHelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥Support Grup", url="https://t.me/wylinesupport"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ YouTube videosu aramak istiyor musunuz??",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Hayır ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
