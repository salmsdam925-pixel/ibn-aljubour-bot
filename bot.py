from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_USERNAME = "@English_English1997"
CHANNEL_LINK = "https://t.me/English_English1997"


def main_menu():
    keyboard = [
        [InlineKeyboardButton("📚 المراحل الدراسية", callback_data="stages")],
        [InlineKeyboardButton("👨‍🏫 المدرسون", callback_data="teachers")],
        [InlineKeyboardButton("📖 الملازم والملفات", callback_data="files")],
        [InlineKeyboardButton("🎥 المحاضرات", callback_data="lectures")],
        [InlineKeyboardButton("📝 الاختبارات", callback_data="tests")],
        [InlineKeyboardButton("📢 الإعلانات", callback_data="news")],
        [InlineKeyboardButton("☎️ الدعم الفني", callback_data="support")],
    ]
    return InlineKeyboardMarkup(keyboard)


def subscription_menu():
    keyboard = [
        [InlineKeyboardButton("📢 اشترك في القناة", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ تحقق من الاشتراك", callback_data="check_subscription")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def is_subscribed(user_id, context):
    try:
        member = await context.bot.get_chat_member(
            chat_id=CHANNEL_USERNAME,
            user_id=user_id
        )

        return member.status in ["member", "administrator", "creator"]

    except Exception:
        return False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    subscribed = await is_subscribed(user_id, context)

    if not subscribed:
        await update.message.reply_text(
            "🎓 منصة ابن الجبور التعليمية\n\n"
            "🌹 أهلاً وسهلاً بك\n\n"
            "📢 للاستخدام المجاني للمنصة، يرجى الاشتراك في قناة المنصة أولاً.\n\n"
            "بعد الاشتراك اضغط على زر التحقق:",
            reply_markup=subscription_menu()
        )
        return

    await update.message.reply_text(
        "🎓 منصة ابن الجبور التعليمية\n\n"
        "أهلاً وسهلاً بك 🌹\n"
        "اختر من القائمة أدناه:",
        reply_markup=main_menu()
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # التحقق من الاشتراك
    if query.data == "check_subscription":
        user_id = query.from_user.id

        subscribed = await is_subscribed(user_id, context)

        if subscribed:
            await query.edit_message_text(
                "✅ تم التحقق من اشتراكك بنجاح!\n\n"
                "🎓 أهلاً بك في منصة ابن الجبور التعليمية 🌹",
                reply_markup=main_menu()
            )
        else:
            await query.answer(
                "❌ لم يتم العثور على اشتراكك في القناة.",
                show_alert=True
            )
        return

    # المراحل الدراسية
    if query.data == "stages":
        keyboard = [
            [InlineKeyboardButton("📘 السادس الابتدائي", callback_data="sixth_primary")],
            [InlineKeyboardButton("📗 الثالث المتوسط", callback_data="third_intermediate")],
            [InlineKeyboardButton("📕 السادس الإعدادي", callback_data="sixth_preparatory")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")],
        ]

        await query.edit_message_text(
            "📚 المراحل الدراسية\n\n"
            "اختر المرحلة الدراسية:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # السادس الإعدادي
    if query.data == "sixth_preparatory":
        keyboard = [
            [InlineKeyboardButton("🔵 الفرع العلمي", callback_data="scientific")],
            [InlineKeyboardButton("🟢 الفرع الأدبي", callback_data="literary")],
            [InlineKeyboardButton("🔙 المراحل الدراسية", callback_data="stages")],
        ]

        await query.edit_message_text(
            "📕 السادس الإعدادي\n\n"
            "اختر الفرع:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # الفرع العلمي
    if query.data == "scientific":
        await query.edit_message_text(
            "🔵 السادس الإعدادي – الفرع العلمي\n\n"
            "سيتم إضافة جميع المواد والملازم قريبًا.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 الفروع", callback_data="sixth_preparatory")]
            ])
        )
        return

    # الفرع الأدبي
    if query.data == "literary":
        await query.edit_message_text(
            "🟢 السادس الإعدادي – الفرع الأدبي\n\n"
            "سيتم إضافة جميع المواد والملازم قريبًا.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 الفروع", callback_data="sixth_preparatory")]
            ])
        )
        return

    # القائمة الرئيسية
    if query.data == "main_menu":
        await query.edit_message_text(
            "🎓 منصة ابن الجبور التعليمية\n\n"
            "أهلاً وسهلاً بك 🌹\n"
            "اختر من القائمة أدناه:",
            reply_markup=main_menu()
        )
        return

    messages = {
        "sixth_primary": "📘 السادس الابتدائي\n\nسيتم إضافة المواد والملازم قريبًا.",
        "third_intermediate": "📗 الثالث المتوسط\n\nسيتم إضافة المواد والملازم قريبًا.",
        "teachers": "👨‍🏫 المدرسون\n\nسيتم إضافة المدرسين قريبًا.",
        "files": "📖 الملازم والملفات\n\nسيتم إضافة الملفات قريبًا.",
        "lectures": "🎥 المحاضرات\n\nسيتم إضافة المحاضرات قريبًا.",
        "tests": "📝 الاختبارات\n\nسيتم إضافة الاختبارات قريبًا.",
        "news": "📢 الإعلانات\n\nلا توجد إعلانات حاليًا.",
        "support": "☎️ الدعم الفني\n\nسيتم إضافة معلومات الدعم قريبًا.",
    }

    await query.edit_message_text(
        messages.get(query.data, "اختر من القائمة الرئيسية.")
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("منصة ابن الجبور تعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()
