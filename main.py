from pyrogram import Client, filters, emoji
from pyrogram.types import Message
bot = Client('Bot')

@bot.on_message(filters.command('start', prefixes=["/"]))
def start(bot, msg):
    msg.reply_text(f"مرحبا اني اسمي ملاك عمري 21 سنه من بغداد أرفعني مشرف بكروبك وراقب التفاعل {emoji.FACE_BLOWING_A_KISS}")

@bot.on_message()
async def all_message(_:Client, m:Message):
    text = m.text
    chat_id = m.chat.id
    user_id = m.from_user.id
    if text in ("مرحبا", "هلو","هلوو","هلووو","هلووو","هلوووو","هلووووو", "هلاو", "هلاوو","هلاووو","هلاوووو","هيلاو","هيلاوو","هيلاووو",""," "
                        ,"هلا","ضيف جديد", "ممكن ترحيب",
                        ):
        await m.reply(f"يا الف هلا {emoji.KISSING_FACE_WITH_CLOSED_EYES}",reply_to_message_id=m.message_id)


    elif text in ("شلونك", " شخبارك", "شكو ماكو", "شنو الاخبار", "شونك", "شلونج", "شخبارج", "شنو اخبارج", "شنونج", "شلونه وضعج", "شونج","اخبارج","امورج","اوضاعج"):
        await m.reply("الحمد لله تمام",reply_to_message_id=m.message_id)


    elif text in ("مشتقاين", "مشتاقين","مشتاقلج", "اشتاقيتلج","كلش مشتاقلج","هواي مشتاقلج", "اني مشتاقلج", "مشتاق", "اني اشتاقلج", "تره اشتاقلج","مشتاقلج ملكه"):
        await m.reply(f" تشتاقلك العافية عيوني{emoji.FACE_WITH_HAND_OVER_MOUTH}",reply_to_message_id=m.message_id)


    elif text in ("احبج", "حبيبي", "حبيتبي", "حبيبتي", "حبي","حبج", "انتي حبي", "انتي كلبي", "انتي الغاليه","كلبي","عمري","روحي","غلاي","عيوني"):
        await m.reply(f" يعمري{emoji.SMILING_FACE_WITH_HEART_EYES}",reply_to_message_id=m.message_id)


    elif text in ("حياتي", "حياتو", "انتي حياتي", "حياتي ملكه"):
        await m.reply(f" سالمه حياتك يعمري{emoji.SMILING_FACE_WITH_HEARTS}",reply_to_message_id=m.message_id)


    elif text in ("ممكن نتعرف", "نتعرف", "شنو اسمج", " شكد عمرج", "عمرج", "عمرج شكد", "يامواليد", "عندك كم سنه", "جبيره لو صغيره","اسمج", "اسمج شنو", "عرفينه","من وين", "بيتكم وين", "وين بينتكم",
                          "عنوانج","نتعرف عليج"):
        await m.reply("اسمي ملاك \n"
                      "عمري 21\n"
                      " من بغداد\n",reply_to_message_id=m.message_id)

    elif text in ("ضوجه","اني ضايج","مقهور","حزين","زعلان","مغثوث","كلش ضايج","ضجت","نقهرت","ضايجه","اني ضايجه","اني مقهورة","اني مقهوره",
                  "اني زعلانه","زعلانه","حزينه","موجوعة","انا تالم","انا اتألم","ضايج"):
        await m.reply(f" سلامتك عيوني{emoji.SAD_BUT_RELIEVED_FACE}",reply_to_message_id=m.message_id)


    elif text in ("اهو","اهوو","اهووو","اهوووو","اهووووو","اهوووووو","اهووووووو"):
        await m.reply(f" ليش اهو شكلت اني مثلا ؟{emoji.UNAMUSED_FACE}",reply_to_message_id=m.message_id)


    elif text in ("شو مختفيه", "شو ماكو","وينج","شو مختفية","شو ماشوفج","شنو وينج","شو مشفتج","وينج ملكه","موجودة","موجوده",
                  "موجودة ؟","وين ماوين"):
        await m.reply(f" موجوده عيوني{emoji.FACE_WITH_ROLLING_EYES}",reply_to_message_id=m.message_id)



    elif text in ("ممكن طلب","اختي ممكن طلب","ممكن طلب اختي","اريد منج شي","اريد اطلب طلب","اريد منج طلب","اريد منج شغله","رايد منج فد شغله"
                  ,"رايدج بموضوع","رايده منج طلب صغير","ممكن سؤال","سؤال","ممكن","اكلج","طلب"):
        await m.reply(f" تفضل حبي{emoji.SMILING_FACE}",reply_to_message_id=m.message_id)


    elif text in ("جيد","عفيه","ممتاز","جيد جدا","جيد جداً","عفيه عليج","سباعيه","سبعه","خوش بنيه","انتي محترمه","انتي محبوبه"):
        await m.reply(f"{emoji.SMILING_FACE_WITH_HEART_EYES}{emoji.RED_HEART}")


    elif text in ("شبيج","شكو شبيج","شبيج شكو","هاي شبيج","شبيج يمعوده","سالمين شبيج","شبيج عيوني","شبيج حبي","شنو شبيج"):
        await m.reply(f" كلشي مابيه{emoji.SLIGHTLY_SMILING_FACE}",reply_to_message_id=m.message_id)


bot.run()