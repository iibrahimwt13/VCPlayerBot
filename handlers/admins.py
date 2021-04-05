from pyrogram import Client, filters
from pyrogram.types import Message
import tgcalls
import sira
from config import SUDO_USERS
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("〰️Wyline〰️=⏸ Durduruldu.")


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("〰️Wyline〰️=▶️ Devam.")


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("〰️Wyline〰️=⏹ Akışı durdurdum.")


@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    sira.task_done(chat_id)
    await message.reply_text("Işleme Alındı")
    if sira.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("kuyrukta hiçbir şey yok")
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, sira.get(chat_id)["file_path"]
        )

        await message.reply_text("〰️Wyline〰️=⏩ Geçerli şarkı atlandı.")


@Client.on_message(
    filters.command("admincache")
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("〰️Wyline〰️=❇️ Yönetici önbelleği yenilendi!")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def helper(client , message:Message):
     await message.reply_text("Komutlar ve orada kullanım burada açıklanmıştır-: \n '/saavn' Jio saavan'da şarkı aramak ve ilk sonucu çalmak için \n '/deezer' Şarkıyı deezer'da aramak ve kaliteli akış elde etmek için \n '/ytt' Youtube'da şarkıyı aramak ve ilk maçı oynamak için sonuç \n '/play' Oynatmaya devam etmek için \n '/resume' akışını duraklatmak için \n '/pause' şarkısının akışını durdurmak için geçerli şarkıyı atlamak için \n '/skip' çalınacak bir bağlantıya veya herhangi bir telgraf ses dosyasına yanıt olarak bunu yanıtlayın. 
