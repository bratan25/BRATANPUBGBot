import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

CONTROLS = "1-7660-0339-2236-4869-065"
SENSITIVITY = "1-7682-9896-6133-1914-916"
ADVANCED = "1-7682-9896-6133-1914-917"
UID = "5138869395"

TIKTOK = "https://www.tiktok.com/@gg.bratann"
INSTAGRAM = "https://www.instagram.com/bratanchill/"

TEXT = {
    "en": {
        "welcome": "🎮 <b>WELCOME TO BRATAN BOT</b>\n\nChoose what you need:",
        "sensitivity": "🎯 <b>BRATAN SENSITIVITY</b>\n\n<code>" + SENSITIVITY + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4-Finger Claw\n\nUse it as a base and adjust it to your own playstyle.",
        "controls": "🎮 <b>BRATAN CONTROLS</b>\n\n<code>" + CONTROLS + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4-Finger Claw",
        "advanced": "⚡ <b>BRATAN ADVANCED SENSITIVITY</b>\n\n<code>" + ADVANCED + "</code>",
        "device": "📱 <b>DEVICE</b>\n\niPhone 15 Pro Max\n✋ 4-Finger Claw\n🎯 Gyroscope Player",
        "uid": "🆔 <b>PUBG MOBILE UID</b>\n\n<code>" + UID + "</code>",
        "socials": "📲 <b>MY SOCIALS</b>\n\n🎵 <a href='" + TIKTOK + "'>TikTok</a> — @gg.bratann\n📸 <a href='" + INSTAGRAM + "'>Instagram</a> — @bratanchill",
        "back": "⬅️ Back",
    },
    "bg": {
        "welcome": "🎮 <b>ДОБРЕ ДОШЛИ В BRATAN BOT</b>\n\nИзбери какво ти трябва:",
        "sensitivity": "🎯 <b>BRATAN SENSITIVITY</b>\n\n<code>" + SENSITIVITY + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4 пръста\n\nИзползвай го като база и го настрой според твоя стил на игра.",
        "controls": "🎮 <b>BRATAN CONTROLS</b>\n\n<code>" + CONTROLS + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4 пръста",
        "advanced": "⚡ <b>BRATAN ADVANCED SENSITIVITY</b>\n\n<code>" + ADVANCED + "</code>",
        "device": "📱 <b>УСТРОЙСТВО</b>\n\niPhone 15 Pro Max\n✋ 4 пръста\n🎯 Gyroscope Player",
        "uid": "🆔 <b>PUBG MOBILE UID</b>\n\n<code>" + UID + "</code>",
        "socials": "📲 <b>МОИТЕ СОЦИАЛНИ МРЕЖИ</b>\n\n🎵 <a href='" + TIKTOK + "'>TikTok</a> — @gg.bratann\n📸 <a href='" + INSTAGRAM + "'>Instagram</a> — @bratanchill",
        "back": "⬅️ Назад",
    },
    "ru": {
        "welcome": "🎮 <b>ДОБРО ПОЖАЛОВАТЬ В BRATAN BOT</b>\n\nВыберите нужный раздел:",
        "sensitivity": "🎯 <b>BRATAN SENSITIVITY</b>\n\n<code>" + SENSITIVITY + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4 пальца\n\nИспользуйте как основу и настройте под свой стиль игры.",
        "controls": "🎮 <b>BRATAN CONTROLS</b>\n\n<code>" + CONTROLS + "</code>\n\n📱 iPhone 15 Pro Max\n✋ 4 пальца",
        "advanced": "⚡ <b>BRATAN ADVANCED SENSITIVITY</b>\n\n<code>" + ADVANCED + "</code>",
        "device": "📱 <b>УСТРОЙСТВО</b>\n\niPhone 15 Pro Max\n✋ 4 пальца\n🎯 Gyroscope Player",
        "uid": "🆔 <b>PUBG MOBILE UID</b>\n\n<code>" + UID + "</code>",
        "socials": "📲 <b>МОИ СОЦСЕТИ</b>\n\n🎵 <a href='" + TIKTOK + "'>TikTok</a> — @gg.bratann\n📸 <a href='" + INSTAGRAM + "'>Instagram</a> — @bratanchill",
        "back": "⬅️ Назад",
    },
}

def menu(lang):
    t = TEXT[lang]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎯 Sensitivity", callback_data="sensitivity"),
         InlineKeyboardButton("🎮 Controls", callback_data="controls")],
        [InlineKeyboardButton("⚡ Advanced", callback_data="advanced"),
         InlineKeyboardButton("📱 Device", callback_data="device")],
        [InlineKeyboardButton("🆔 PUBG UID", callback_data="uid"),
         InlineKeyboardButton("📲 Socials", callback_data="socials")],
    ])

def language_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton("🇧🇬 Български", callback_data="lang_bg")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["lang"] = "en"
    await update.message.reply_text(
        "🌍 <b>Choose your language / Избери език / Выберите язык</b>",
        parse_mode="HTML",
        reply_markup=language_menu(),
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("lang_"):
        lang = data[5:]
        context.user_data["lang"] = lang
        await query.edit_message_text(
            TEXT[lang]["welcome"],
            parse_mode="HTML",
            reply_markup=menu(lang),
        )
        return

    lang = context.user_data.get("lang", "en")
    t = TEXT[lang]

    if data in t:
        await query.edit_message_text(
            t[data],
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(t["back"], callback_data="back")]
            ]),
        )
    elif data == "back":
        await query.edit_message_text(
            t["welcome"],
            parse_mode="HTML",
            reply_markup=menu(lang),
        )

async def set_commands(app):
    await app.bot.set_my_commands([
        ("start", "Open the BRATAN menu"),
        ("sensitivity", "Get my sensitivity"),
        ("controls", "Get my controls"),
        ("advanced", "Get my advanced sensitivity"),
        ("uid", "Get my PUBG UID"),
    ])

async def command_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "en")
    cmd = update.message.text.lstrip("/").split("@")[0]
    mapping = {
        "sensitivity": "sensitivity",
        "controls": "controls",
        "advanced": "advanced",
        "uid": "uid",
    }
    key = mapping.get(cmd)
    if key:
        await update.message.reply_text(TEXT[lang][key], parse_mode="HTML", disable_web_page_preview=True)

def main():
    token = os.environ.get("BOT_TOKEN")
    webhook_url = os.environ.get("WEBHOOK_URL")
    port = int(os.environ.get("PORT", "10000"))

    if not token:
        raise RuntimeError("BOT_TOKEN environment variable is missing")
    if not webhook_url:
        raise RuntimeError("WEBHOOK_URL environment variable is missing")

    app = Application.builder().token(token).post_init(set_commands).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["sensitivity", "controls", "advanced", "uid"], command_reply))
    app.add_handler(CallbackQueryHandler(button))

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=webhook_url,
        allowed_updates=Update.ALL_TYPES,
    )

if __name__ == "__main__":
    main()
