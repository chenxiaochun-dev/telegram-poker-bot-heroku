import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from game import start_new_game, handle_player_action
from data import games

TOKEN = os.environ.get("TOKEN")

# /start 命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "欢迎来到德州扑克 Bot！\n发送 /join 加入游戏，或 /deal 开始发牌"
    )

# /join 命令
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.effective_user

    game = games.setdefault(chat_id, start_new_game(chat_id))
    msg = game.add_player(user.id, user.first_name)
    await update.message.reply_text(msg)

# /deal 命令
async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    game = games.get(chat_id)

    if not game:
        await update.message.reply_text("请先 /join 玩家")
        return

    msg = game.deal_cards()
    await update.message.reply_text(msg)

# 按钮操作处理
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    action = query.data

    game = games.get(chat_id)
    if game:
        msg = handle_player_action(game, user_id, action)
        await query.edit_message_text(text=msg)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("deal", deal))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
