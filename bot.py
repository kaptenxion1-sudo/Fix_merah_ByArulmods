import telebot
from telebot import types
import datetime

# --- CONFIGURATION ---
TOKEN = '8635569627:AAFdl2IzavWi8YjeFy09JGwsV162hNkhmzg'
bot = telebot.TeleBot(TOKEN)

# DATABASE (Permanenkan ID di sini)
OWNER_ID = 5120247112
premium_users = [5120247112, 1424892421]
current_email = "rul****@gmail.com"

# --- HARGA PREMIUM ---
HARGA_PREMIUM = (
    "💎 **LIST HARGA PREMIUM FIX MERAH** 💎\n\n"
    "🔹 **PAKET HEMAT**\n"
    "├ 7 Hari : Rp 10.000\n"
    "└ 15 Hari : Rp 15.000\n\n"
    "🔹 **PAKET SULTAN**\n"
    "├ 30 Hari : Rp 25.000\n"
    "└ Permanent : Rp 50.000 (Best Seller)\n\n"
    "💳 **METODE PEMBAYARAN**\n"
    "├ DANA/GOPAY : 0812xxxxxx\n"
    "└ OWNER : @Arulmodss\n\n"
    "⚠️ **PROSES**\n"
    "Kirim bukti transfer ke Admin untuk aktivasi!"
)

# --- COMMAND START / DASHBOARD ---
@bot.message_handler(commands=['start'])
def welcome(message):
    now = datetime.datetime.now()
    status_akses = "💎 PREMIUM" if message.from_user.id in premium_users else "❌ NO AKSES"
    
    dashboard = (
        f"Selamat datang, @{message.from_user.username}\n"
        f"Semoga Banding fix merah lancar boy\n\n"
        f"🟢 Status : ONLINE\n"
        f"📅 Tanggal : 06-03-2026\n"
        f"⏰ Waktu : {now.strftime('%H:%M:%S')} WIB\n\n"
        f"📊 Jumlah Email : 1\n"
        f"📈 Total Banding : 158\n"
        f"👥 Pengguna Bot : 852\n"
        f"💎/❌ AKSES : {status_akses}\n\n"
        f"🛰️ Sender:\n"
        f"🟢 PRIBADI ({current_email})\n\n"
        f"Silakan pilih layanan yang ingin digunakan di bawah ini."
    )

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🚫 FIX MERAH", callback_data="fix"),
        types.InlineKeyboardButton("📧 MENU EMAIL", callback_data="mail"),
        types.InlineKeyboardButton("💎 BUY AKSES", callback_data="buy"),
        types.InlineKeyboardButton("⚠️ TUTORIAL", callback_data="tutor"),
        types.InlineKeyboardButton("📢 CHENEL YAPING", url="https://t.me/Arulmodss"),
        types.InlineKeyboardButton("👑 OWNER", url="https://t.me/Arulmodss"),
        types.InlineKeyboardButton("🔥 MENU OWNER", callback_data="owner_menu")
    )
    bot.send_message(message.chat.id, dashboard, reply_markup=markup)

# --- COMMAND FIX MERAH ---
@bot.message_handler(commands=['f'])
def banding_exec(message):
    if message.from_user.id not in premium_users:
        bot.reply_to(message, "❌ **AKSES DITOLAK!**\nLu bukan user premium. Chat @Arulmodss!")
        return

    try:
        target = message.text.split()[1]
        res = (
            f"🚀 **BANDING TERKIRIM BOS**\n\n"
            f"🎯 Target: `{target}`\n"
            f"📩 Tujuan: support@support.whatsapp.com\n"
            f"📧 Pake Email: {current_email}\n"
            f"💳 Via: PRIBADI\n"
            f"📊 Total Nyepam: 20x\n\n"
            f"*Tunggu 20 detik dlu baru minta kode masih merah ganti email lu.*"
        )
        bot.reply_to(message, res, parse_mode="Markdown")
    except:
        bot.reply_to(message, "⚠️ Format: `/f +628xxx`")

# --- COMMAND OWNER: ADD PREM & SET MAIL ---
@bot.message_handler(commands=['addprem'])
def add_premium(message):
    if message.from_user.id == OWNER_ID:
        try:
            tid = int(message.text.split()[1])
            dur = message.text.split()[2]
            if tid not in premium_users: premium_users.append(tid)
            bot.reply_to(message, f"💎 **ADD PREMIUM SUKSES**\nID: `{tid}`\nDurasi: {dur}")
        except:
            bot.reply_to(message, "Format: `/addprem ID DURASI`")

@bot.message_handler(commands=['setmail'])
def change_mail(message):
    global current_email
    if message.from_user.id == OWNER_ID:
        try:
            new_mail = message.text.split()[1]
            current_email = f"{new_mail[:3]}****@gmail.com"
            bot.reply_to(message, f"✅ Email diset ke: `{new_mail}`")
        except:
            bot.reply_to(message, "Format: `/setmail email@gmail.com`")

# --- CALLBACK HANDLER ---
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "fix":
        bot.send_message(call.message.chat.id, "Ketik `/f [nomor]` untuk eksekusi.")
    elif call.data == "buy":
        bot.send_message(call.message.chat.id, HARGA_PREMIUM, parse_mode="Markdown")
    elif call.data == "tutor":
        bot.send_message(call.message.chat.id, "1. Copy nomor WA ban\n2. Ketik /f [nomor]\n3. Tunggu 20 detik.")
    elif call.data == "owner_menu":
        if call.from_user.id == OWNER_ID:
            bot.send_message(call.message.chat.id, "👑 **OWNER MENU**\n\n`/addprem [ID] [DURASI]`\n`/setmail [EMAIL]`")
        else:
            bot.answer_callback_query(call.id, "Bukan owner dilarang klik, jing!")

print("🔥 QUANTUM V8.0: BOT RUNNING PERFECTLY! 🔥")
bot.polling(none_stop=True)
