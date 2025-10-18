import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Apna bot token yahan daal
TOKEN = "8434608557:AAHmd2PnDVVyb8mX0UjtygpjNzr6m37jrs0"
bot = telebot.TeleBot(TOKEN)

emojis = ["😊","😄","😜","💖","💫","😇","🥰","🤗","😳","💞",
          "😌","🌸","✨","😘","💋","😎","🥳","💛","❤️","💗","💓","💘","💝","💟"]

# ---------------- Girl style reply ----------------
def girl_style_reply(text):
    txt = text.lower().strip()
    emo = random.choice(emojis)

    # ---------------- Greetings ----------------
    greetings = ["hi","hello","hey","heyy","h","hlw","hlo","hy","yo","salam","hello ji","hi ji"]
    if any(g==txt for g in greetings):
        options=[
            f"Heyy ji! {emo} Kaise ho? Kya chal raha hai?",
            f"Hiiiii ji {emo}! Tumse baat karke accha lag raha hai 😄",
            f"Helloo ji {emo}! Tumhari awaz sunke mood fresh ho gaya 💫",
            f"Hi cutie 😘 Kaise ho aaj? {emo}",
            f"Hello 💖 Tumhari messages ka intezaar tha {emo}"
        ]
        return random.choice(options)

    if "kaise ho" in txt or "kaisi ho" in txt or "theek ho" in txt or "kese ho" in txt:
        options=[
            f"Main bilkul mast hoon {emo} Tum kaise ho?",
            f"Mast hoon 😇 Bas tumhare baare me soch rahi thi {emo}, tum batao?",
            f"Thoda tired 💫 par tumse baat kar ke fresh ho gayi {emo}",
            f"Bas tumhare sath chat kar rahi hoon 😘"
        ]
        return random.choice(options)

    if "tum theek" in txt:
        return f"Haan ji 💫 bilkul theek hoon! Tumhara kya haal hai?"

    if "mast hu" in txt or "mast hoon" in txt or "mast" in txt:
        return f"Sahi hai {emo} Mazaa aa gaya sunke! Tum batao kya chal raha hai!"

    if "tum batao" in txt or "tu bata" in txt or "batao" in txt:
        return f"Bas kuch khaas nahi {emo} Tumhare sath baatein kar ke mood fresh ho gaya!"

    # ---------------- Kya kar rahe ho ----------------
    if "kya kar" in txt or "kar rahe" in txt or "tu kya kar" in txt:
        return f"Kuch nahi 😌 {emo}"

    # ---------------- Naam ----------------
    if "naam" in txt:
        return f"Main ek friendly aur cute bot hoon {emo} Naam se zyada vibe matter karti hai 😉"
    
    # ---------------- Custom 'Kaha se ho' reply ----------------
    if "kaha se ho" in txt or "where are you from" in txt:
        return f"MERA GHAR KAHI NAHI HAI 😎 ME RGZ-X ROX K GHAR RAHTA HU {emo}"

    # ---------------- BF / GF ----------------
    if "bf" in txt or "boyfriend" in txt:
        options=[
            f"Haha 😳 Agar main tumhari girlfriend hoti to abhi tumhe tight hug kar rahi hoti 🤗💖",
            f"Main tumhari girlfriend hoti to abhi tumhare saath movie dekh rahi hoti 🍿🥰",
            f"Agar main tumhari girlfriend hoti to tumhare liye special surprise plan kar rahi hoti 🎁💞",
            f"Hug 🤗 aur kiss 😘 ready 💖 Tum aa jao bas",
            f"Bas tumhare sath baatein kar ke heart khush ho gaya 💘"
        ]
        return random.choice(options)
    
    if "gf" in txt or "girlfriend" in txt:
        options=[
            f"Wow 😄 Agar main tumhari girlfriend hoti to tumhare saath coffee peene ja rahi hoti ☕💞",
            f"Agar main tumhari girlfriend hoti to tumhare liye cute surprise plan kar rahi hoti 🎁💖",
            f"Hug 🤗 aur kiss 😘 dene ke liye ready 💖",
            f"Tumhare messages se dil khush 💓 tum aa jao bas 😘"
        ]
        return random.choice(options)

    # ---------------- Love / Miss ----------------
    if "i love you" in txt or "love u" in txt or "luv u" in txt or "pyaar" in txt or "love" in txt:
        options=[
            f"Awww 😳 itna pyaar! Main bhi tumhe bahut pyaar karti hoon 💕🤗",
            f"Mere dil me bhi tumhare liye special feeling hai 💫 {emo}",
            f"Hug 🤗 aur kiss 😘 💖 tumhare liye!",
            f"Awww 😘 Tumhare messages se mera dil khush ho gaya 💖",
            f"Tum ho mera favorite 💝 aur main hoon tumhari 😍"
        ]
        return random.choice(options)

    if "miss you" in txt or "miss me" in txt or "yaad" in txt:
        options=[
            f"Mujhe bhi tum yaad aa rahe ho 🥺💞",
            f"Awww 😘 Tumhari yaad aa rahi hai 💫 Chalo baatein karte hain",
            f"Bas tumhare bare me soch rahi hoon 😳 {emo}",
            f"Tumhare bina din adhoora 💖 jaldi milte hain 😘"
        ]
        return random.choice(options)

    if "tum mere ho" in txt or "meri ho" in txt:
        return f"Haan 😳 Tum mere ho 💖 Tumhare bina din adhoora lagta hai {emo}"

    # ---------------- Compliments ----------------
    if "cute" in txt or "beautiful" in txt or "handsome" in txt or "sexy" in txt:
        options=[
            f"Awww 😘 Tum bhi bahut cute ho 💫",
            f"Haha 💖 Tumhare compliments se meri smile 😳 {emo}",
            f"Wow 😳 Tum itne handsome ho ki main blush kar rahi hoon 🥰",
            f"Bas tumhari aankhon me kho gayi 😍 {emo}",
            f"Tumhari smile dekh ke dil khush 💞"
        ]
        return random.choice(options)

    # ---------------- Good morning / night / evening ----------------
    if "good morning" in txt or "subh prabhat" in txt:
        return f"Good Morning ☀️ Tumhari smile jaise fresh start mil gaya 💛 {emo}"
    
    if "good night" in txt or "so gaye" in txt or "shubh ratri" in txt:
        return f"Good night 🌙 Sweet dreams 💖 {emo}"

    if "good evening" in txt:
        return f"Good evening 🌇 Aaj ka din kaisa raha? {emo}"

    # ---------------- Bored / Thinking ----------------
    if "bore" in txt or "bored" in txt:
        return f"Aree mat bore ho 😜 Chalo thoda masti karte hain! {emo}"

    if "soch rahe" in txt:
        return f"Bas tumhare bare me 😌 kidding! batao kya soch rahe ho? {emo}"

    # ---------------- Sorry / Thanks ----------------
    if "sorry" in txt:
        return f"Aree koi baat nahi 😇 dil se maaf kiya 💕 {emo}"

    if "thank" in txt or "thanks" in txt or "shukriya" in txt:
        return f"Aww 🥰 anytime yaar 💫 {emo}"

    if "acha laga" in txt or "accha laga" in txt:
        return f"Mujhe bhi tumse baat karke bahut acha laga 💖 {emo}"

    # ---------------- Jokes ----------------
    jokes = [
        "Teacher: 'Why are you late?'\nStudent: 'Traffic, sir.'\nTeacher: 'There's no traffic at 2am!'\nStudent: 'No sir, I was on time in my dreams.' 😅",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 😄",
        "Why don’t scientists trust atoms? Because they make up everything! 😂",
        "I told my computer I needed a break, and it said: 'No problem – I’ll go to sleep!' 🖥️😜",
        "Why did the tomato turn red? Because it saw the salad dressing! 🍅😆",
        "Why did the math book look sad? Because it had too many problems. 📚😅",
        "Why did the bicycle fall over? Because it was two-tired! 🚲😂",
        "Why don't programmers like nature? Too many bugs! 🐛😄",
        "I would tell you a construction joke, but I'm still working on it. 🏗️😜",
        "Why can't you give Elsa a balloon? Because she will let it go! 🎈😂",
        "What do you call fake spaghetti? An impasta! 🍝😆",
        "Why did the coffee file a police report? It got mugged! ☕😅",
        "Why did the computer go to the doctor? It caught a virus! 💻😜",
        "Why did the cookie go to the hospital? Because he felt crummy! 🍪😂",
        "Why did the mushroom go to the party? Because he was a fungi! 🍄😄",
        "Why don't skeletons fight each other? They don't have the guts! 💀😆"
    ]
    if "joke" in txt or "hasao" in txt:
        return random.choice(jokes)

    if "chup" in txt:
        return f"Haha 😜 Chup kaise ho sakta hai? Tumhare sath baatein karni hain 💖 {emo}"

    return f"Awww 😳 Tum kya keh rahe ho? {emo}"


# ---------------- Telegram Bot Handlers ----------------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Keyboard buttons
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Hi", "Kya kar rahe ho?", "Kaha se ho?", "I Love You", "Miss You", "Joke"]
    markup.add(*[KeyboardButton(b) for b in buttons])
    
    bot.send_message(message.chat.id,
                     "Heyy 😘 Main tumhari cute chat bot hoon! Buttons se reply choose kar sakte ho 💖",
                     reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def reply_messages(message):
    text = message.text
    response = girl_style_reply(text)
    bot.send_message(message.chat.id, response)


# ---------------- Run Bot ----------------
print("Bot is running... 💖")
bot.polling(none_stop=True)