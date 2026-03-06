import telebot
from telebot import types
import datetime

# --- CONFIG ---
TOKEN = '8635569627:AAFdl2IzavWi8YjeFy09JGwsV162hNkhmzg'
bot = telebot.TeleBot(TOKEN)

# DATABASE RUNTIME (Akan reset jika bot restart di GitHub)
OWNER_ID = 5120247112
premium_users = [5120247112, 1424892421]
current_email = "rul****@gmail.com"
total_banding = 158

# --- FUNCTIONS ---
def get_dashboard(username, user_id):
    now = datetime.datetime.now()
    status = "💎 PREMIUM" if user_id in premium_users else "❌ NO AKSES"
    return (
        f"Selamat datang, @{username}\n"
        f"Semoga Banding fix merah lancar boy\n\n"
        f"🟢 Status : ONLINE\n"
        f"📅 Tanggal : 06-03-2026\n"
        f"⏰ Waktu : {now.strftime('%H:%M:%S')} WIB\n\n"
        f"📊 Jumlah Email : 1\n"
        f"📈 Total Banding : {total_banding}\n"
        f"👥 Pengguna Bot : 852\n"
        f"💎/❌ AKSES : {status}\n\n"
        f"🛰️ Sender:\n"
        f"🟢 PRIBADI ({current_email})\n\n"
        f"Silakan pilih layanan yang ingin digunakan di bawah ini."
    )

# --- COMMANDS ---
@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🚫 FIX MERAH", callback_data="fix"),
        types.InlineKeyboardButton("📧 MENU EMAIL", callback_data="mail"),
        types.InlineKeyboardButton("💎 BUY AKSES", callback_data="buy"),
        types.InlineKeyboardButton("⚠️ TUTORIAL", callback_data="tutor"),
        types.InlineKeyboardButton("📢 CHENEL YAPING", url="https://t.me/Arulmodss"),
        types.InlineKeyboardButton("👑 OWNER", url="https://t.me/Arulmodss")
    )
    bot.send_message(message.chat.id, get_dashboard(message.from_user.username, message.from_user.id), reply_markup=markup)

@bot.message_handler(commands=['setmail'])
def cmd_setmail(message):
    global current_email
    if message.from_user.id == OWNER_ID:
        try:
            new_mail = message.text.split()[1]
            # Logika sensor email
            current_email = f"{new_mail[:3]}****@gmail.com"
            bot.reply_to(message, f"✅ **EMAIL BERHASIL DIGANTI!**\nSekarang sender: `{new_mail}`")
        except:
            bot.reply_to(message, "❌ Format: `/setmail email@gmail.com`")

@bot.message_handler(commands=['addprem'])
def cmd_addprem(message):
    if message.from_user.id == OWNER_ID:
        try:
            target_id = int(message.text.split()[1])
            if target_id not in premium_users:
                premium_users.append(target_id)
            bot.reply_to(message, f"💎 **SUKSES!** ID `{target_id}` sekarang Premium.")
        except:
            bot.reply_to(message, "❌ Format: `/addprem ID`")

@bot.message_handler(commands=['f'])
def cmd_fix(message):
    global total_banding
    if message.from_user.id in premium_users:
        try:
            num = message.text.split()[1]
            total_banding += 1
            res = (
                f"🚀 **BANDING TERKIRIM BOS**\n\n"
                f"🎯 Target: `{num}`\n"
                f"📧 Pake Email: {current_email}\n"
                f"📊 Status: SPAM 20x SENT\n\n"
                f"*Tunggu 20 detik dulu baru cek kode!*"
            )
            bot.reply_to(message, res, parse_mode="Markdown")
        except:
            bot.reply_to(message, "⚠️ Format: `/f +628xxx`")
    else:
        bot.reply_to(message, "❌ Beli akses premium ke @Arulmodss")

# --- CALLBACKS ---
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "mail":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"📧 **SENDER SAAT INI:**\n`{current_email}`\n\nGunakan `/setmail` untuk mengubah.")
    elif call.data == "buy":
        bot.send_message(call.message.chat.id, "💎 **HARGA PREMIUM**\n- 7 Hari: 10k\n- 30 Hari: 25k\n- Perm: 50k\n\nHubungi @Arulmodss")
    elif call.data == "fix":
        bot.send_message(call.message.chat.id, "Ketik `/f [nomor]` untuk gas!")

bot.polling(none_stop=True)
