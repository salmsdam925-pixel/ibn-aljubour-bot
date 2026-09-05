from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 المراحل الدراسية", callback_data="stages")],
        [InlineKeyboardButton("👨‍🏫 المدرسون", callback_data="teachers")],
        [InlineKeyboardButton("📖 الملازم والملفات", callback_data="files")],
        [InlineKeyboardButton("🎥 المحاضرات", callback_data="lectures")],
        [InlineKeyboardButton("📝 الاختبارات", callback_data="tests")],
        [InlineKeyboardButton("📢 الإعلانات", callback_data="news")],
        [InlineKeyboardButton("☎️ الدعم الفني", callback_data="support")],
    ]

    await update.message.reply_text(
        "🎓 منصة ابن الجبور التعليمية\n\n"
        "أهلاً وسهلاً بك 🌹\n"
        "اختر من القائمة أدناه:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

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

    if query.data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("📚 المراحل الدراسية", callback_data="stages")],
            [InlineKeyboardButton("👨‍🏫 المدرسون", callback_data="teachers")],
            [InlineKeyboardButton("📖 الملازم والملفات", callback_data="files")],
            [InlineKeyboardButton("🎥 المحاضرات", callback_data="lectures")],
            [InlineKeyboardButton("📝 الاختبارات", callback_data="tests")],
            [InlineKeyboardButton("📢 الإعلانات", callback_data="news")],
            [InlineKeyboardButton("☎️ الدعم الفني", callback_data="support")],
        ]

        await query.edit_message_text(
            "🎓 منصة ابن الجبور التعليمية\n\n"
            "أهلاً وسهلاً بك 🌹\n"
            "اختر من القائمة أدناه:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    messages = {
        "teachers": "👨‍🏫 المدرسون\n\nسيتم إضافة المدرسين قريبًا.",
        "files": "📖 الملازم والملفات\n\nسيتم إضافة الملفات قريبًا.",
        "lectures": "🎥 المحاضرات\n\nسيتم إضافة المحاضرات قريبًا.",
        "tests": "📝 الاختبارات\n\nسيتم إضافة الاختبارات قريبًا.",
        "news": "📢 الإعلانات\n\nلا توجد إعلانات حاليًا.",
        "support": "☎️ الدعم الفني\n\nسيتم إضافة معلومات الدعم قريبًا.",

        "sixth_primary": (
            "📘 السادس الابتدائي\n\n"
            "سيتم إضافة المواد الدراسية قريبًا."
        ),

        "third_intermediate": (
            "📗 الثالث المتوسط\n\n"
            "سيتم إضافة المواد الدراسية قريبًا."
        ),

        "sixth_preparatory": (
            "📕 السادس الإعدادي\n\n"
            "سيتم إضافة المواد الدراسية قريبًا."
        ),
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
