from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")


# =========================================================
# قنوات الاشتراك الإجباري
# =========================================================

CHANNELS = [
    ("@English_English1997", "https://t.me/English_English1997"),
    ("@quraan2quraan", "https://t.me/quraan2quraan"),
]


# =========================================================
# القائمة الرئيسية
# =========================================================

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


# =========================================================
# قائمة الاشتراك
# =========================================================

def subscription_menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "📢 اشترك بالقناة التعليمية",
                url="https://t.me/English_English1997"
            )
        ],
        [
            InlineKeyboardButton(
                "📖 اشترك بقناة القرآن الكريم",
                url="https://t.me/quraan2quraan"
            )
        ],
        [
            InlineKeyboardButton(
                "✅ تحقق من الاشتراك",
                callback_data="check_subscription"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================================================
# التحقق من الاشتراك في القنوات
# =========================================================

async def is_subscribed(user_id, context):

    try:

        for channel, _ in CHANNELS:

            member = await context.bot.get_chat_member(
                chat_id=channel,
                user_id=user_id
            )

            if member.status not in [
                "member",
                "administrator",
                "creator"
            ]:
                return False

        return True

    except Exception:

        return False


# =========================================================
# أمر START
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    subscribed = await is_subscribed(
        user_id,
        context
    )

    if not subscribed:

        await update.message.reply_text(

            "🎓 منصة ابن الجبور التعليمية\n\n"
            "🌹 أهلاً وسهلاً بك\n\n"
            "📢 للاستفادة من خدمات المنصة مجانًا، "
            "يرجى الاشتراك في القناتين أولاً.\n\n"

            "1️⃣ اشترك بالقناة التعليمية\n"
            "2️⃣ اشترك بقناة القرآن الكريم\n\n"

            "بعد الاشتراك اضغط على زر التحقق:",

            reply_markup=subscription_menu()
        )

        return

    await update.message.reply_text(

        "🎓 منصة ابن الجبور التعليمية\n\n"
        "أهلاً وسهلاً بك 🌹\n\n"
        "اختر من القائمة أدناه:",

        reply_markup=main_menu()
    )


# =========================================================
# التعامل مع الأزرار
# =========================================================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    # =====================================================
    # التحقق من الاشتراك
    # =====================================================

    if query.data == "check_subscription":

        user_id = query.from_user.id

        subscribed = await is_subscribed(
            user_id,
            context
        )

        if subscribed:

            await query.edit_message_text(

                "✅ تم التحقق من اشتراكك بنجاح!\n\n"
                "🎓 أهلاً بك في منصة ابن الجبور التعليمية 🌹\n\n"
                "اختر من القائمة أدناه:",

                reply_markup=main_menu()
            )

        else:

            await query.answer(

                "❌ يجب الاشتراك في القناتين أولاً.",
                show_alert=True
            )

        return


    # =====================================================
    # المراحل الدراسية
    # =====================================================

    if query.data == "stages":

        keyboard = [

            [
                InlineKeyboardButton(
                    "📘 السادس الابتدائي",
                    callback_data="sixth_primary"
                )
            ],

            [
                InlineKeyboardButton(
                    "📗 الثالث المتوسط",
                    callback_data="third_intermediate"
                )
            ],

            [
                InlineKeyboardButton(
                    "📕 السادس الإعدادي",
                    callback_data="sixth_preparatory"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 القائمة الرئيسية",
                    callback_data="main_menu"
                )
            ],

        ]

        await query.edit_message_text(

            "📚 المراحل الدراسية\n\n"
            "اختر المرحلة الدراسية:",

            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return


    # =====================================================
    # السادس الإعدادي
    # =====================================================

    if query.data == "sixth_preparatory":

        keyboard = [

            [
                InlineKeyboardButton(
                    "🔵 الفرع العلمي",
                    callback_data="scientific"
                )
            ],

            [
                InlineKeyboardButton(
                    "🟢 الفرع الأدبي",
                    callback_data="literary"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 المراحل الدراسية",
                    callback_data="stages"
                )
            ],

        ]

        await query.edit_message_text(

            "📕 السادس الإعدادي\n\n"
            "اختر الفرع:",

            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return


    # =====================================================
    # السادس العلمي
    # =====================================================

    if query.data == "scientific":

        keyboard = [

            [
                InlineKeyboardButton(
                    "📖 الإسلامية",
                    url="https://t.me/aljbouryEdu/13"
                )
            ],

            [
                InlineKeyboardButton(
                    "📕 العربي – الجزء الأول",
                    url="https://t.me/aljbouryEdu/14"
                )
            ],

            [
                InlineKeyboardButton(
                    "📕 العربي – الجزء الثاني",
                    url="https://t.me/aljbouryEdu/15"
                )
            ],

            [
                InlineKeyboardButton(
                    "📘 الإنكليزي – كتاب الطالب",
                    url="https://t.me/aljbouryEdu/16"
                )
            ],

            [
                InlineKeyboardButton(
                    "📗 الإنكليزي – كتاب النشاط",
                    url="https://t.me/aljbouryEdu/17"
                )
            ],

            [
                InlineKeyboardButton(
                    "📐 الرياضيات",
                    url="https://t.me/aljbouryEdu/18"
                )
            ],

            [
                InlineKeyboardButton(
                    "⚗️ الكيمياء",
                    url="https://t.me/aljbouryEdu/19"
                )
            ],

            [
                InlineKeyboardButton(
                    "🧬 الأحياء",
                    url="https://t.me/aljbouryEdu/20"
                )
            ],

            [
                InlineKeyboardButton(
                    "⚡ الفيزياء",
                    url="https://t.me/aljbouryEdu/21"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 الفروع",
                    callback_data="sixth_preparatory"
                )
            ],

        ]

        await query.edit_message_text(

            "🔵 السادس الإعدادي – الفرع العلمي\n\n"
            "📚 الكتب الدراسية\n\n"
            "اختر الكتاب الذي تريد الانتقال إليه:",

            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return


    # =====================================================
    # السادس الأدبي
    # =====================================================

    if query.data == "literary":

        keyboard = [

            [
                InlineKeyboardButton(
                    "📖 الإسلامية",
                    url="https://t.me/aljbouryEdu/13"
                )
            ],

            [
                InlineKeyboardButton(
                    "📕 العربي – الجزء الأول",
                    url="https://t.me/aljbouryEdu/26"
                )
            ],

            [
                InlineKeyboardButton(
                    "📕 العربي – الجزء الثاني",
                    url="https://t.me/aljbouryEdu/27"
                )
            ],

            [
                InlineKeyboardButton(
                    "📚 كتاب النقد",
                    url="https://t.me/aljbouryEdu/28"
                )
            ],

            [
                InlineKeyboardButton(
                    "📘 الإنكليزي – كتاب الطالب",
                    url="https://t.me/aljbouryEdu/16"
                )
            ],

            [
                InlineKeyboardButton(
                    "📗 الإنكليزي – كتاب النشاط",
                    url="https://t.me/aljbouryEdu/17"
                )
            ],

            [
                InlineKeyboardButton(
                    "📐 الرياضيات",
                    url="https://t.me/aljbouryEdu/22"
                )
            ],

            [
                InlineKeyboardButton(
                    "🌍 الجغرافية",
                    url="https://t.me/aljbouryEdu/23"
                )
            ],

            [
                InlineKeyboardButton(
                    "📜 التاريخ",
                    url="https://t.me/aljbouryEdu/24"
                )
            ],

            [
                InlineKeyboardButton(
                    "💰 الاقتصاد",
                    url="https://t.me/aljbouryEdu/25"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 الفروع",
                    callback_data="sixth_preparatory"
                )
            ],

        ]

        await query.edit_message_text(

            "🟢 السادس الإعدادي – الفرع الأدبي\n\n"
            "📚 الكتب الدراسية\n\n"
            "اختر الكتاب الذي تريد الانتقال إليه:",

            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return


    # =====================================================
    # السادس الابتدائي
    # =====================================================

    if query.data == "sixth_primary":

        await query.edit_message_text(

            "📘 السادس الابتدائي\n\n"
            "سيتم إضافة المواد والملازم قريبًا.",

            reply_markup=InlineKeyboardMarkup([

                [
                    InlineKeyboardButton(
                        "🔙 المراحل الدراسية",
                        callback_data="stages"
                    )
                ]

            ])
        )

        return


    # =====================================================
    # الثالث المتوسط
    # =====================================================

    if query.data == "third_intermediate":

        await query.edit_message_text(

            "📗 الثالث المتوسط\n\n"
            "سيتم إضافة المواد والملازم قريبًا.",

            reply_markup=InlineKeyboardMarkup([

                [
                    InlineKeyboardButton(
                        "🔙 المراحل الدراسية",
                        callback_data="stages"
                    )
                ]

            ])
        )

        return


    # =====================================================
    # العودة للقائمة الرئيسية
    # =====================================================

    if query.data == "main_menu":

        await query.edit_message_text(

            "🎓 منصة ابن الجبور التعليمية\n\n"
            "أهلاً وسهلاً بك 🌹\n"
            "اختر من القائمة أدناه:",

            reply_markup=main_menu()
        )

        return


    # =====================================================
    # الأقسام الأخرى
    # =====================================================

    messages = {

        "teachers":
            "👨‍🏫 المدرسون\n\n"
            "سيتم إضافة المدرسين قريبًا.",

        "files":
            "📖 الملازم والملفات\n\n"
            "سيتم إضافة الملفات قريبًا.",

        "lectures":
            "🎥 المحاضرات\n\n"
            "سيتم إضافة المحاضرات قريبًا.",

        "tests":
            "📝 الاختبارات\n\n"
            "سيتم إضافة الاختبارات قريبًا.",

        "news":
            "📢 الإعلانات\n\n"
            "لا توجد إعلانات حاليًا.",

        "support":
            "☎️ الدعم الفني\n\n"
            "سيتم إضافة معلومات الدعم قريبًا.",

    }


    await query.edit_message_text(

        messages.get(
            query.data,
            "اختر من القائمة الرئيسية."
        )

    )


# =========================================================
# تشغيل البوت
# =========================================================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("منصة ابن الجبور تعمل الآن...")

    app.run_polling()


if __name__ == "__main__":

    main()
