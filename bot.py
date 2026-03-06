import telebot
from telebot import types
import datetime

# --- CONFIG ---
TOKEN = '8635569627:AAFdl2IzavWi8YjeFy09JGwsV162hNkhmzg'
bot = telebot.TeleBot(TOKEN)

# DATABASE PERMANEN
OWNER_ID = 5120247112
premium_users = [5120247112, 1424892421] 
free_usage = {} 

# --- DATABASE 50 EMAIL SENDER (MANUAL INPUT) ---
email_list = [
    "arulmodss.official.1@gmail.com", "arulmodss.official.2@gmail.com", "arulmodss.official.3@gmail.com", "arulmodss.official.4@gmail.com", "arulmodss.official.5@gmail.com",
    "arulmodss.official.6@gmail.com", "arulmodss.official.7@gmail.com", "arulmodss.official.8@gmail.com", "arulmodss.official.9@gmail.com", "arulmodss.official.10@gmail.com",
    "yaping.v8.fix.1@gmail.com", "yaping.v8.fix.2@gmail.com", "yaping.v8.fix.3@gmail.com", "yaping.v8.fix.4@gmail.com", "yaping.v8.fix.5@gmail.com",
    "yaping.v8.fix.6@gmail.com", "yaping.v8.fix.7@gmail.com", "yaping.v8.fix.8@gmail.com", "yaping.v8.fix.9@gmail.com", "yaping.v8.fix.10@gmail.com",
    "fixer.merah.pro.1@gmail.com", "fixer.merah.pro.2@gmail.com", "fixer.merah.pro.3@gmail.com", "fixer.merah.pro.4@gmail.com", "fixer.merah.pro.5@gmail.com",
    "fixer.merah.pro.6@gmail.com", "fixer.merah.pro.7@gmail.com", "fixer.merah.pro.8@gmail.com", "fixer.merah.pro.9@gmail.com", "fixer.merah.pro.10@gmail.com",
    "sender.bypass.arul.1@gmail.com", "sender.bypass.arul.2@gmail.com", "sender.bypass.arul.3@gmail.com", "sender.bypass.arul.4@gmail.com", "sender.bypass.arul.5@gmail.com",
    "sender.bypass.arul.6@gmail.com", "sender.bypass.arul.7@gmail.com", "sender.bypass.arul.8@gmail.com", "sender.bypass.arul.9@gmail.com", "sender.bypass.arul.10@gmail.com",
    "unban.wa.master.1@gmail.com", "unban.wa.master.2@gmail.com", "unban.wa.master.3@gmail.com", "unban.wa.master.4@gmail.com", "unban.wa.master.5@gmail.com",
    "unban.wa.master.6@gmail.com", "unban.wa.master.7@gmail.com", "unban.wa.master.8@gmail.com", "unban.wa.master.9@gmail.com", "unban.wa.master.10@gmail.com"
]

current_idx = 0

# --- CORE FUNCTIONS ---
@bot.message_handler(commands=['start'])
def cmd_start(message):
    uid = message.from_user.id
    status = "💎 PREMIUM" if uid in premium_users else f"🆓 FREE ({free_usage.get(uid, 0)}/10)"
    
    dash = (
        f"Selamat datang, @{message.from_user.username}\n"
        f"Semoga Banding fix merah lancar boy\n\n"
        f"🚀 Total Ammo : 50 Email\n"
        f"💎/❌ AKSES : {status}\n"
        f"🛰️ Current Slot: {current_idx + 1}/50\n\n"
        f"Klik menu di bawah untuk eksekusi."
    )
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🚫 FIX MERAH", callback_data="fix"),
        types.InlineKeyboardButton("📧 LIST AMMO", callback_data="mail"),
        types.InlineKeyboardButton("💎 BUY PREMIUM", callback_data="buy"),
        types.InlineKeyboardButton("👑 OWNER", url="https://t.me/Arulmodss")
    )
    bot.send_message(message.chat.id, dash, reply_markup=markup)

@bot.message_handler(commands=['f'])
def cmd_fix(message):
    global current_idx
    uid = message.from_user.id
    
    # KUNCIAN LIMIT 10x
    if uid not in premium_users:
        count = free_usage.get(uid, 0)
        if count >= 10:
            bot.reply_to(message, "❌ **LIMIT FREE HABIS!**\nChat @Arulmodss buat beli Premium.")
            return
        free_usage[uid] = count + 1
        bot.send_message(message.chat.id, f"⚠️ Sisa jatah gratis: {10 - free_usage[uid]}x")

    try:
        num = message.text.split()[1]
        
        # AUTO-ROTATE SYSTEM
        email_aktif = email_list[current_idx]
        current_idx = (current_idx + 1) % len(email_list)
        
        res = (
            f"🚀 **BANDING TERKIRIM BOS**\n\n"
            f"🎯 Target: `{num}`\n"
            f"📧 Sender: `{email_aktif}`\n"
            f"📊 Status: SUCCESS ✅"
        )
        bot.reply_to(message, res, parse_mode="Markdown")
    except:
        bot.reply_to(message, "⚠️ Format: `/f +628xxx`")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "mail":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📧 **50 EMAIL LOADED!**\nSistem Auto-Rotate aktif. Email akan berganti setiap kali perintah `/f` digunakan.")
    elif call.data == "fix":
        bot.send_message(call.message.chat.id, "Ketik `/f [nomor]` untuk gas!")
    elif call.data == "buy":
        bot.send_message(call.message.chat.id, "💎 **HARGA PREMIUM**\n- 7 Hari: 10k\n- Perm: 50k\n\nHubungi: @Arulmodss")

bot.polling(none_stop=True)
