import telebot
from telebot import types
import time
bot = telebot.TeleBot('6893596394:AAFxiXHDJ_QypG6GkXCE9tjUZ7wMn2gcz2U')
user_answers = {}
def delete_message(chat_id, message_id):
  try:
      bot.delete_message(chat_id, message_id)
  except Exception as e:
      print("Помилка при видаленні повідомлення:", e)
def create_rating_keyboard(callback_prefix):
    markup = types.InlineKeyboardMarkup(row_width=5)
    buttons = [types.InlineKeyboardButton(text=str(i), callback_data=f"{callback_prefix}_{i}") for i in range(11)]
    markup.add(*buttons)
    return markup
def send_start_message():
  chat_ids = [1580990462, 5210739777]  

def create_skin_state_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton(text="🌱1 тип", callback_data="skin_type_dry"),
        types.InlineKeyboardButton(text="🌱2 тип", callback_data="skin_type_normal"),
        types.InlineKeyboardButton(text="🌱3 тип", callback_data="skin_type_1"),
        types.InlineKeyboardButton(text="🌱4 тип", callback_data="skin_type_2"),
        types.InlineKeyboardButton(text="🌱5 тип", callback_data="skin_type_3")
    ]
    keyboard.add(*buttons)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    users[chat_id] = message.chat.username
    user = message.from_user
    if user.username:
        username = user.username
    else:
        username = "користувача"

    bot.send_message(1580990462, f"Користувач {username} розпочав опитування.")
    bot.send_message(5210739777, f"Користувач {username} розпочав опитування.")
    markup = types.InlineKeyboardMarkup()
    btn_start = types.InlineKeyboardButton(text='Розпочати', callback_data='start')
    markup.add(btn_start)

    bot.send_message(message.chat.id, "<b>Вітаю</b> 😍\n\n"

"Я допоможу Вам швидко з'ясувати <b>Ваш</b> тип та стан шкіри.\n\n"

"Але перед цим, хочу сказати, <b>що я безмежно вдячна за довіру</b> ☺️\n\n"

"Ця інформація допоможе Вам більш точно розуміти потреби шкіри та вдало підбирати догляд.\n\n"

"<b>Тому пропоную не втрачати час і протестувати Вашу шкіру просто зараз</b> 👇",
                 parse_mode='HTML', reply_markup=markup )

@bot.callback_query_handler(func=lambda call: call.data == 'start')
def callback_query_start(call):
    if call.data == 'start':
        bot.send_message(call.message.chat.id, "<b>Нижче Вам будуть подані описи різних типів шкіри👇</b>\n\n"
                                      "Уважно <b>прочитайте</b> їх <b>та оберіть</b> пункт, який буде найбільш точно описувати Ваші відчуття та вигляд Вашої шкіри.\n\n"
                                      "📎<b>Тип шкіри не дорівнює стан шкіри</b>\n"
                                      "📎<b>Тип шкіри не змінюється протягом життя</b>", parse_mode='HTML')
        delete_message(call.message.chat.id, call.message.message_id)
        time.sleep(9)
        bot.send_message(call.message.chat.id, "<b>🌱1 тип</b>\n"
                                          "⦁ шкіра матова, якщо одразу не нанести зволоження, мало власних ліпідів;\n"
                                          "⦁ після очищення хочеться одразу нанести крем;\n"
                                          "⦁ немає проблем з комедонами (поодинокі можливі);\n"
                                          "⦁ пори маловиражені (з віком вираженість пор зростає у всіх типів шкіри).",
                         parse_mode='HTML')
        time.sleep(9)
        bot.send_message(call.message.chat.id, "<b>🌱2 тип</b>\n"
                                          "⦁ природний помірний блиск (ні суха, ні жирна);\n"
                                          "⦁ немає дискомфорту, відчуття сухості і нагальної потреби у зволоженні після очищення;\n"
                                          "⦁ немає проблеми з комедонами (одиничні можуть бути, як і висипи), всі процеси відбуваються коректно.",
                         parse_mode='HTML')
        time.sleep(9)
        bot.send_message(call.message.chat.id, "<b>🌱3 тип</b>\n"
                                          "⦁ шкіра має надмірний жирний блиск;\n"
                                          "⦁ легко обходиться без зволоження після очищення;\n"
                                          "⦁ себум вільно виходить з проток сальних залоз, рідко є комедони або одиничні.",
                         parse_mode='HTML')
        time.sleep(9)
        bot.send_message(call.message.chat.id, "<b>🌱4 тип</b>\n"
                                          "⦁ себум густий і складно виходить з проток сальних залоз (через це є зневоднені, сухі ділянки);\n"
                                          "⦁ проблема закритих комедонів;\n"
                                          "⦁ часте відчуття стягнутості, лущення, порушений захисний бар'єр.",
                         parse_mode='HTML')
        time.sleep(9)
        bot.send_message(call.message.chat.id, "<b>🌱5 тип</b>\n"
                                          "⦁ є ділянки із комедонами, із запаленнями;\n"
                                          "⦁ є жирні та зневоднені ділянки.",parse_mode='HTML')
        time.sleep(6)
        bot.send_message(call.message.chat.id, "Прочитавши опис кожного типу, <b>оберіть пункт</b>, який буде найбільш точно характеризувати Ваш тип шкіри 👇", reply_markup=create_skin_state_keyboard(), parse_mode='HTML')
@bot.callback_query_handler(func=lambda call: call.data.startswith('skin_type_'))
def callback_query_skin_type(call):
    time.sleep(0)
    user_answers[call.message.chat.id] = {"skin_type": call.data.split('_')[-1]}
    bot.send_message(call.message.chat.id, "<b>Дякую 🤍</b>\n"
                                           "Ваша відповідь врахована", parse_mode='HTML')
    time.sleep(3)
    bot.send_message(call.message.chat.id, "Ідемо далі ✅", parse_mode='HTML')
    time.sleep(2)

    bot.send_message(call.message.chat.id, "Ми вже з'ясували, що <b>тип шкіри сталий,</b> а от\n"
                                      "<b>Стан шкіри може періодично змінюватись,</b>\n"
                                      "оскільки на нього впливає догляд, навколишнє середовище, стреси.", parse_mode='HTML')
    time.sleep(9)
    bot.send_message(call.message.chat.id, "Ви можете відчувати, що Ваша шкіра перебуває у <b>зневодненому стані 💦</b> незалежно від Вашого типу шкіри.\n\n"
                                      "Це стан, коли <b>Ви відчуваєте</b>\n"
                                      "⦁ сухість\n"
                                      "⦁ можливе лущення\n"
                                      "⦁ нестача вологи роговому шару шкіри.\n\n"
                                      "Це тимчасовий стан і він досить легко коригується доглядом.", parse_mode='HTML')


    delete_message(call.message.chat.id, call.message.message_id)
    time.sleep(10)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text="Так", callback_data="dehydration_yes"),
        types.InlineKeyboardButton(text="Ні", callback_data="dehydration_no")]
    keyboard.add(*buttons)
    bot.send_message(call.message.chat.id, "Чи відчуваєте ви зневодненість?", reply_markup=keyboard)
    time.sleep(1)
@bot.callback_query_handler(func=lambda call: call.data == 'dehydration_yes' or call.data == 'dehydration_no')
def callback_query_skin_condition_dehydration(call):
    chat_id = call.message.chat.id
    if chat_id not in user_answers:
        user_answers[chat_id] = {}

    if call.data == 'dehydration_yes':
        user_answers[chat_id]["dehydration"] = "yes"
    else:
        user_answers[chat_id]["dehydration"] = "no"

    bot.send_message(chat_id, "<b>Ваша відповідь врахована ✅</b>\n\n"
                             "І ми досліджуємо далі)", parse_mode='HTML')
    time.sleep(1)
    delete_message(call.message.chat.id, call.message.message_id)
    time.sleep(1)
    bot.send_message(call.message.chat.id, "<b>Ми переходимо до зʼясування рівня чутливості 👼 Вашої шкіри.</b>\n\n"
                                      "Це стан, який може бути набутим (наслідком впливу зовнішніх факторів).\n\n"
                                      "Або ж вродженим (генетична особливість)", parse_mode='HTML')
    bot.send_message(call.message.chat.id, "Для визначення рівня чутливості Вам потрібно оцінити кожен пункт <b>за десятибальною шкалою</b>"
                                      "(у разі, якщо відчуття нехарактерне, пункт оцінюється в 0 балів)👌", parse_mode='HTML')
    time.sleep(1)
    bot.send_message(call.message.chat.id, "Оцініть схильність Вашої шкіри до почервонінь", reply_markup=create_rating_keyboard("redness"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('redness_'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["redness"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Чи притаманне Вам відчуття тепла в шкірі? Яка інтенсивність?" ,reply_markup=create_rating_keyboard("heat_sensation"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('heat_sensation'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["heat_sensation"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "На скільки балів Ви б оцінили роздратування?", reply_markup=create_rating_keyboard("burning_sensation"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('burning_sensation'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["burning_sensation"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Чи відчуваєте Ви свербіж? Оцініть інтенсивність", reply_markup=create_rating_keyboard("itchiness"))
    delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('itchiness'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["itchiness"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Оцініть відчуття болю", reply_markup=create_rating_keyboard("pain"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('pain'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["pain"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Яку б оцінку ви поставили загальному відчуттю дискомфорту?", reply_markup=create_rating_keyboard("discomfort"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('discomfort'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["discomfort"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Чи притаманне Вам відчуття приливів крові? Оцініть", reply_markup=create_rating_keyboard("blood_rush"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('blood_rush'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["blood_rush"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "Оцініть відчуття печіння", reply_markup=create_rating_keyboard("burning"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('burning'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["burning"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "На скільки балів Ви оціните поколювання Вашої шкіри, якщо таке відчуття присутнє?", reply_markup=create_rating_keyboard("stinging"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('stinging'))
def callback_query_skin_redness(call):
    user_answers[call.message.chat.id]["stinging"] = int(call.data.split('_')[-1])
    bot.send_message(call.message.chat.id, "У скільки балів Ви б оцінили відчуття стягнутості?", reply_markup=create_rating_keyboard("damag"))
    delete_message(call.message.chat.id, call.message.message_id)
@bot.callback_query_handler(func=lambda call: call.data.startswith('damag'))
def callback_query_skin_damag(call):
    user_answers[call.message.chat.id]["damag"] = int(call.data.split('_')[-1])
    delete_message(call.message.chat.id, call.message.message_id)
    time.sleep(3)
    calculate_skin_condition(call.message)

def calculate_skin_condition(message):
    redness = user_answers[message.chat.id]["redness"]
    heat_sensation = user_answers[message.chat.id]["heat_sensation"]
    burning_sensation = user_answers[message.chat.id]["burning_sensation"]
    itchiness = user_answers[message.chat.id]["itchiness"]
    pain = user_answers[message.chat.id]["pain"]
    discomfort = user_answers[message.chat.id]["discomfort"]
    blood_rush = user_answers[message.chat.id]["blood_rush"]
    burning = user_answers[message.chat.id]["burning"]
    stinging = user_answers[message.chat.id]["stinging"]
    damag = user_answers[message.chat.id]["damag"]

    score = redness + heat_sensation + burning_sensation + itchiness + pain + discomfort + blood_rush + burning + stinging + damag

    skin_type = user_answers[message.chat.id]["skin_type"]
    dehydration = user_answers[message.chat.id]["dehydration"]

    if score <= 20:
        result = "нечутлива"
    elif 20 < score <= 60:
        result = "чутлива"
    else:
        result = "надто чутлива і потрібна обов’язково консультація лікаря"

    if skin_type == "dry":
      skin_type_text = "Сухий тип"
    elif skin_type == "normal":
      skin_type_text = "Нормальний тип"
    elif skin_type == "1":
      skin_type_text = "Жирний тип із жирною себореєю"
    elif skin_type == "2":
      skin_type_text = "Комбі/Жирний тип із сухою себореєю"
    elif skin_type == "3":
      skin_type_text = "Комбі/Жирний тип із змішаною себореєю"
    else:
      skin_type_text = skin_type

    if dehydration == "yes":
        dehydration_text = "Зневоднена"
    else:
        dehydration_text = "Не зневоднена"

    user_answers[message.chat.id]["score"] = score
    user_answers[message.chat.id]["result"] = result
    user_answers[message.chat.id]["skin_type_text"] = skin_type_text
    user_answers[message.chat.id]["dehydration_text"] = dehydration_text

    bot.send_message(message.chat.id, "Вітаю 🎉\n" "Тест пройдено, а Ваші відповіді опрацьовуються\n\n"
"Дякую за довіру 🤍", parse_mode='HTML')
    bot.send_message(message.chat.id, f"<b>У Вас</b> {skin_type_text} шкіри.\n"
                                      f"{dehydration_text}.\n"
                                      f"<b>За шкалою Мізері Ви отримали оцінку</b>: {score}.\n"
                                      f"І це свідчить про те, <b>що Ваша шкіра</b> {result}.", parse_mode='HTML')
    time.sleep(2)
    bot.send_message(message.chat.id, "Для переходу на сайт магазину скористайтесь посиланням нижче 👇", reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/limitless.shop_/")))
    bot.send_message(message.chat.id, "Перейти на сайт магазину:", reply_markup=types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Website", url="https://limitlessua.com/")))#команда для надсилання посилання на сайт магазину

def calculate_skin_condition(message):
    chat_id = message.chat.id
    if chat_id not in user_answers:
        return  

    redness = user_answers[chat_id].get("redness", 0)
    heat_sensation = user_answers[chat_id].get("heat_sensation", 0)
    burning_sensation = user_answers[chat_id].get("burning_sensation", 0)
    itchiness = user_answers[chat_id].get("itchiness", 0)
    pain = user_answers[chat_id].get("pain", 0)
    discomfort = user_answers[chat_id].get("discomfort", 0)
    blood_rush = user_answers[chat_id].get("blood_rush", 0)
    burning = user_answers[chat_id].get("burning", 0)
    stinging = user_answers[chat_id].get("stinging", 0)
    damag = user_answers[chat_id].get("damag", 0)

    score = redness + heat_sensation + burning_sensation + itchiness + pain + discomfort + blood_rush + burning + stinging + damag

    skin_type = user_answers[chat_id].get("skin_type", "")
    dehydration = user_answers[chat_id].get("dehydration", "")

    if score <= 20:
        result = "нечутлива"
    elif 20 < score <= 60:
        result = "чутлива"
    else:
        result = "надто чутлива і потрібна обов'язково консультація лікаря"

    if skin_type == "dry":
      skin_type_text = "Сухий тип"
    elif skin_type == "normal":
      skin_type_text = "Нормальний тип"
    elif skin_type == "1":
      skin_type_text = "Жирний тип із жирною себореєю"
    elif skin_type == "2":
      skin_type_text = "Комбі/Жирний тип із сухою себореєю"
    elif skin_type == "3":
      skin_type_text = "Комбі/Жирний тип із змішаною себореєю"
    else:
      skin_type_text = skin_type

    if dehydration == "yes":
        dehydration_text = "Зневоднена"
    elif dehydration == "no":
        dehydration_text = "Не зневоднена"
    else:
        dehydration_text = ""

    user_answers[chat_id]["score"] = score
    user_answers[chat_id]["result"] = result
    user_answers[chat_id]["skin_type_text"] = skin_type_text
    user_answers[chat_id]["dehydration_text"] = dehydration_text

    bot.send_message(message.chat.id, "Вітаю 🎉\n" "Тест пройдено, а Ваші відповіді опрацьовуються\n\n"
    "Дякую за довіру 🤍", parse_mode='HTML')
    time.sleep(2)
    bot.send_message(message.chat.id, f"<b>У Вас</b> {skin_type_text} шкіри.\n"
      f"{dehydration_text}.\n"
      f"<b>За шкалою Мізері Ви отримали оцінку</b>: {score}.\n"
      f"І це свідчить про те, <b>що Ваша шкіра</b> {result}.", parse_mode='HTML')
    time.sleep(4)
    bot.send_message(chat_id, "Якщо бажаєте продовжити консультацію або виникли додаткові питання - натискайте на зручний спосіб зв'язку з нашим консультантом:", reply_markup=types.InlineKeyboardMarkup().add(
     types.InlineKeyboardButton(text="Telegram", url="https://t.me/consultant_Limitless"),
     types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/limitless.shop_/")))

    bot.send_message(chat_id, "Перейти на сайт магазину", reply_markup=types.InlineKeyboardMarkup().add(
       types.InlineKeyboardButton(text="shop", url="https://limitlessua.com/")))
    time.sleep(4)
    bot.send_message(message.chat.id, "Не забувайте себе приймати, любити та турбуватись 🤍\n\n"
"<b>Ваша краса</b>, неповторність та особливість <b>не має меж</b>\n\n" 

"<b>А ми</b> з радістю <b>допоможемо</b> Вам більш <b>розуміти</b> Вашу шкіру та <b>підбирати догляд</b> по потребах 🥰\n\n"
"З любов’ю <b>Limitless</b> 🌱", parse_mode='HTML')
    send_results_to_admins(chat_id, message.chat.username, skin_type_text, dehydration_text, score, result)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Тиць', callback_data='button_pressed'))

    bot.send_message(message.chat.id, "Натисни якщо хочеш пройти знову", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == 'button_pressed':
    bot.send_message(call.message.chat.id, "/start")

def send_results_to_admins(chat_id, username, skin_type_text, dehydration_text, score, result):
    text = f"Результати тестування для користувача {username}:\n" \
           f"Тип шкіри: {skin_type_text}\n" \
           f"Стан зволоженості: {dehydration_text}\n" \
           f"Бали: {score}\n" \
           f"Результат: {result}"

    bot.send_message(1580990462, text)
    bot.send_message(5210739777, text)
def send_results_to_user(chat_id, username):
    score = user_answers[chat_id]["score"]
    result = user_answers[chat_id]["result"]
    skin_type_text = user_answers[chat_id]["skin_type_text"]
    dehydration_text = user_answers[chat_id]["dehydration_text"]

    text = f"Результати тестування для вас, {username}:\n" \
           f"Тип шкіри: {skin_type_text}\n" \
           f"Стан зволоженості: {dehydration_text}\n" \
           f"Бали: {score}\n" \
           f"Результат: {result}"

    bot.send_message(chat_id, text)
users = {}

@bot.message_handler(commands=['post'])
def post_handler(message):
    if message.chat.id == 1580990462:  
        text = message.text.replace('/post ', '', 1)  
        for user_id in users:
            try:
                bot.send_message(user_id, text)
            except Exception as e:
                print(f'Error sending message to {user_id}: {e}')

@bot.message_handler(commands=['post'])
def post_handler(message):
    if message.chat.id == 5210739777:  
        text = message.text.replace('/post ', '', 1)  
        for user_id in users:
            try:
                bot.send_message(user_id, text)
            except Exception as e:
                print(f'Error sending message to {user_id}: {e}')

bot.polling(none_stop=True)