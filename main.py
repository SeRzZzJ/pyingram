import re

from pyongram import TelegramBotLongPolling
from pyongram import Context
from pyongram import MessageRouter, MessageFormRouter

telegram_bot = TelegramBotLongPolling("5681001250:AAEWW99s6uWs1tJwH18xzqZK4EcLrahcmE8")
message_router = MessageRouter()
message_form = MessageFormRouter("form")


@message_router.text(trigger=lambda msg: msg["text"] == "старт", is_next_handler=False)
async def msg(ctx: Context):
    ctx.enter("form")
    ctx.session.set("info", "start")
    await ctx.reply("Марафон формы начался, продолжим?")


@message_form.text(trigger=lambda msg: msg["text"] == "да")
async def to_handle_msg(ctx: Context):
    await ctx.reply("Красавчик!")
    ctx.session.update("info", "yes")
    ctx.exit()
    await ctx.reply("Марафон формы закончился")


@message_form.text(trigger=lambda msg: msg["text"] == "нет")
async def to_handle_msg(ctx: Context):
    await ctx.reply("Зря!")
    ctx.session.update("info", "no")
    ctx.exit()
    await ctx.reply("Марафон формы закончился")


@message_router.text(trigger=lambda msg: True, is_next_handler=False)
async def to_handle_msg(ctx: Context):
    if ctx.session.get("info") == "yes":
        return await ctx.reply_with_html("<b>ответ был да!</b>")
    if ctx.session.get("info") == "no":
        return await ctx.reply_with_html("<b>ответ был НЕТ!</b>")
    await ctx.reply_with_html(f"<b>{ctx.update["message"]["text"]}</b>")


@message_router.text(trigger=lambda msg: True)
async def to_handle_msg(ctx: Context):
    await ctx.reply_with_html(f"<b>ЕЩЕ ОДНО ЭХО</b>")


@message_router.start()
async def to_handle_msg(ctx: Context):
    await ctx.reply_with_html(f"<b>ЕЩЕ ОДНО ЭХО</b>")


telegram_bot.use_router(message_router)
telegram_bot.use_router(message_form)

if __name__ == "__main__":
    telegram_bot.run_infinity_loop()
