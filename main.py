import telebot
import random

# Replace with your actual Telegram bot token (obtained from BotFather)
BOT_TOKEN = "7317579489:AAHS1KZIvXjkayQCUJOTpIpLGv03jNB2OXM"
bot = telebot.TeleBot(BOT_TOKEN)

# Define functions for button actions (replace placeholders with your logic)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton("Adulteration Information"),
        telebot.types.KeyboardButton("Detection Tests"),
        telebot.types.KeyboardButton("Nutritional Information"),
        telebot.types.KeyboardButton("Ask a Question"),
        telebot.types.KeyboardButton("Bye"),
    ]
    keyboard.add(*buttons)
    welcome_message = (
        "Hello and welcome to the Food Safety Bot! 🌟\n\n"
        "I am here to help you stay informed and safe about the food you consume. "
        "Here are the things I can assist you with:\n\n"
        "1️⃣ *Adulteration Information*: Learn interesting facts about common food adulterants.\n"
        "2️⃣ *Detection Tests*: Discover simple tests you can do at home to check for food adulteration.\n"
        "3️⃣ *Nutritional Information*: Get detailed nutritional information about various foods.\n"
        "4️⃣ *Ask a Question*: Have any food-related questions? Ask away!\n"
        "5️⃣ *Bye*: End our conversation."
    )
    bot.send_message(message.chat.id, welcome_message, reply_markup=keyboard)

# Adulterants information dictionary
adulterants_info = {
    'Milk': 'Did you know? 💧 Water is the most common adulterant found in milk to increase its volume.',
    'Turmeric': 'Fun Fact: ☠️ Lead chromate, a toxic compound, is sometimes used to give turmeric a bright yellow color.',
    'Chilli Powder': 'Interesting Fact: 🧱 Brick powder or artificial colors may be added to chili powder for bulk and color enhancement.',
    'Honey': 'Did you know? 🍯 Some commercially sold honey is adulterated with high fructose corn syrup or other sweeteners.',
    'Olive Oil': 'Fun Fact: 🫒 Olive oil is often adulterated with cheaper oils like sunflower oil or canola oil.',
    'Coffee': 'Interesting Fact: ☕ Coffee may be adulterated with chicory powder or cereals to increase its quantity.',
    'Sugar': 'Did you know? 🍬 Sugar can be adulterated with chalk powder or other inedible substances to increase weight.',
    'Tea Leaves': 'Fun Fact: 🍵 Tea leaves can be adulterated with used tea leaves or colored leaves to cut costs.',
    'Black Pepper': 'Interesting Fact: 🌶️ Black pepper may be adulterated with papaya seeds or dried colored berries.',
    'Butter': 'Did you know? 🧈 Butter can be adulterated with margarine or vegetable oil to reduce costs.',
    'Ghee': 'Fun Fact: 🐄 Adulterants in ghee may include vanaspati, palm oil, or animal fats to mimic the texture and taste.',
    'Mustard Seeds': 'Interesting Fact: 🌱 Mustard seeds can be adulterated with argemone seeds, which are toxic if consumed.',
    'Rice': 'Did you know? 🍚 Stones, plastic pellets, or cheaper grains may be added to rice to increase weight.',
    'Wheat Flour': 'Fun Fact: 🌾 Wheat flour can be adulterated with chalk powder or starch to increase bulk.',
    'Cumin Seeds': 'Interesting Fact: 🌿 Cumin seeds may be adulterated with gravel, dirt, or other seeds to increase weight.',
    'Coriander Powder': 'Did you know? 🍲 Coriander powder can be adulterated with sawdust or husk to dilute its strength.',
    'Cardamom': 'Fun Fact: 🍡 Cardamom can be adulterated with colored seeds or artificial flavorings to increase aroma.',
    'Mango Pulp': 'Interesting Fact: 🥭 Mango pulp may be adulterated with artificial colors or sweeteners to enhance appearance and taste.',
    'Coconut Oil': 'Did you know? 🥥 Coconut oil can be adulterated with cheaper oils like palm oil or soybean oil.',
    'Pulses': 'Fun Fact: 🌱 Pulses may be adulterated with stones, sand, or dirt to increase weight.',
    'Hing (Asafoetida)': 'Interesting Fact: 🌿 Hing can be adulterated with gum arabic or wheat flour to reduce purity.',
    'Haldi (Turmeric) Powder': 'Did you know? 🌾 Turmeric powder can be adulterated with metanil yellow dye, which is harmful to health.',
    'Dairy Products': 'Fun Fact: 🥛 Dairy products may be adulterated with starch, soap, or chemicals to improve texture or appearance.',
    'Saffron': 'Interesting Fact: 🌼 Saffron can be adulterated with colored corn silk or artificial dyes to increase quantity.',
    'Vegetable Oils': 'Did you know? 🌿 Vegetable oils like sunflower oil or palm oil may be adulterated with cheaper oils or recycled oils.',
    'Pickle': 'Fun Fact: 🥒 Pickles may be adulterated with artificial colors or preservatives to extend shelf life.',
    'Fruit Juices': 'Interesting Fact: 🍹 Fruit juices may be adulterated with water, sugar, or artificial flavors to dilute and sweeten.',
    'Jam': 'Did you know? 🍓 Jam may be adulterated with fruit peels or artificial flavors to enhance taste and reduce costs.',
    'Paneer': 'Fun Fact: 🧀 Paneer may be adulterated with starch or synthetic paneer to increase volume and reduce costs.',
    'Vermicelli': 'Interesting Fact: 🍜 Vermicelli may be adulterated with cheaper flours or synthetic colorants to mimic quality.',
    'Jaggery': 'Did you know? 🍯 Jaggery may be adulterated with molasses, chalk powder, or sugarcane residue to increase weight.',
    'Chocolates': 'Fun Fact: 🍫 Chocolates may be adulterated with vegetable oils, cocoa substitutes, or non-cocoa fats.',
    'Salt': 'Interesting Fact: 🧂 Salt may be adulterated with chalk powder or other minerals to increase weight.',
    'Maida (Refined Flour)': 'Did you know? 🌾 Maida may be adulterated with alum, soapstone powder, or other bleaching agents.',
    'Milk Products': 'Fun Fact: 🥛 Milk products like yogurt or cheese may be adulterated with starch or synthetic substances.',
    'Carbonated Drinks': 'Interesting Fact: 🥤 Carbonated drinks may be adulterated with artificial sweeteners, flavors, or colors.',
    'Bread': 'Did you know? 🍞 Bread may be adulterated with baking soda, artificial preservatives, or non-food-grade ingredients.',
    'Sweets': 'Fun Fact: 🍬 Sweets may be adulterated with artificial colors, flavors, or non-food-grade ingredients.',
    'Snacks': 'Interesting Fact: 🍿 Snacks like chips or namkeen may be adulterated with recycled oils or artificial additives.',
    'Rice Flour': 'Did you know? 🍚 Rice flour may be adulterated with cheaper flours, starch, or other fillers.',
    'Wheat Flour': 'Fun Fact: 🌾 Wheat flour may be adulterated with chalk powder, soapstone powder, or other non-food-grade substances.',
    'Besan (Gram Flour)': 'Interesting Fact: 🌱 Besan may be adulterated with cheaper flours, artificial colors, or fillers.',
}


# Nutritional information dictionary
nutri_info = {
    'apple': {'calories': 95, 'protein': 0.3, 'carbs': 25, 'fiber': 4.4},
    'banana': {'calories': 105, 'protein': 1.3, 'carbs': 27, 'fiber': 3.1},
    'spinach': {'calories': 7, 'protein': 0.9, 'carbs': 1.1, 'fiber': 0.7},
    'rice': {'calories': 345, 'protein': 7.1, 'carbs': 77.5, 'fiber': 1.6},
    'wheat flour': {'calories': 364, 'protein': 10.3, 'carbs': 73, 'fiber': 10.7},
    'whole wheat bread': {'calories': 247, 'protein': 8.7, 'carbs': 45.5, 'fiber': 6.5},
    'white bread': {'calories': 265, 'protein': 8.8, 'carbs': 49.5, 'fiber': 2.7},
    'whole milk': {'calories': 61, 'protein': 3.2, 'carbs': 4.8, 'fiber': 0},
    'skimmed milk': {'calories': 35, 'protein': 3.4, 'carbs': 4.8, 'fiber': 0},
    'curd': {'calories': 98, 'protein': 3.5, 'carbs': 3.4, 'fiber': 0},
    'paneer': {'calories': 265, 'protein': 18.3, 'carbs': 1.2, 'fiber': 0},
    'chicken (skinless, raw)': {'calories': 165, 'protein': 31, 'carbs': 0, 'fiber': 0},
    'chicken (skinless, cooked)': {'calories': 239, 'protein': 27.6, 'carbs': 0, 'fiber': 0},
    'fish': {'calories': 147, 'protein': 25.5, 'carbs': 0, 'fiber': 0},
    'egg': {'calories': 68, 'protein': 6.5, 'carbs': 0.6, 'fiber': 0},
    'potato': {'calories': 77, 'protein': 2, 'carbs': 17, 'fiber': 2.2},
    'onion': {'calories': 40, 'protein': 1.1, 'carbs': 9.3, 'fiber': 1.7},
    'tomato': {'calories': 18, 'protein': 0.9, 'carbs': 3.9, 'fiber': 1.2},
    'carrot': {'calories': 41, 'protein': 0.9, 'carbs': 9.6, 'fiber': 2.8},
    'beetroot': {'calories': 43, 'protein': 1.6, 'carbs': 9.6, 'fiber': 2.8},
    'capsicum ': {'calories': 20, 'protein': 0.9, 'carbs': 4.6, 'fiber': 1.7},
    'lettuce': {'calories': 15, 'protein': 1.4, 'carbs': 2.9, 'fiber': 1.3},
    'cucumber': {'calories': 15, 'protein': 0.7, 'carbs': 3.6, 'fiber': 0.5},
    'pumpkin': {'calories': 26, 'protein': 1, 'carbs': 6, 'fiber': 0.5},
    'ladyfinger': {'calories': 33, 'protein': 1.9, 'carbs': 7, 'fiber': 2.5},
    'brinjal': {'calories': 25, 'protein': 1, 'carbs': 6, 'fiber': 3},
    'beans': {'calories': 31, 'protein': 1.8, 'carbs': 7, 'fiber': 3.4},
    'green peas': {'calories': 81, 'protein': 5, 'carbs': 14, 'fiber': 5},
    'green gram dal': {'calories': 347, 'protein': 24, 'carbs': 62, 'fiber': 16},
    'black gram dal': {'calories': 105, 'protein': 8, 'carbs': 19, 'fiber': 6},
    'bengal gram dal': {'calories': 165, 'protein': 9, 'carbs': 27, 'fiber': 5},
    'red gram dal': {'calories': 155, 'protein': 9, 'carbs': 28, 'fiber': 5},
    'soybean': {'calories': 446, 'protein': 39, 'carbs': 30, 'fiber': 9},
    'peanuts': {'calories': 567, 'protein': 26, 'carbs': 16, 'fiber': 8},
    'peanut butter': {'calories': 598, 'protein': 22, 'carbs': 20, 'fiber': 6},
    'almonds': {'calories': 579, 'protein': 21, 'carbs': 22, 'fiber': 12},
    'cashews': {'calories': 553, 'protein': 18, 'carbs': 30, 'fiber': 3},
    'pistachios': {'calories': 562, 'protein': 21, 'carbs': 28, 'fiber': 10},
    'walnuts': {'calories': 654, 'protein': 15, 'carbs': 14, 'fiber': 7},
    'raisins': {'calories': 299, 'protein': 3.1, 'carbs': 79, 'fiber': 3.7},
    'dates': {'calories': 282, 'protein': 2.5, 'carbs': 75, 'fiber': 8},
    'jaggery': {'calories': 383, 'protein': 3.9, 'carbs': 98, 'fiber': 0.5},
    'sugar': {'calories': 387, 'protein': 0, 'carbs': 99, 'fiber': 0},
    'honey': {'calories': 304, 'protein': 0.3, 'carbs': 82, 'fiber': 0.2},
    'butter': {'calories': 717, 'protein': 0.9, 'carbs': 0.1, 'fiber': 0},
    'ghee': {'calories': 900, 'protein': 0, 'carbs': 0, 'fiber': 0},
    
}

# Detection tests dictionary
detection_tests = {
    'milk': 'To check for water adulteration in milk, place a drop of milk on a polished surface. Pure milk will flow slowly, leaving a white trail, while milk with water will flow immediately without leaving a mark.',
    'turmeric': 'Mix a teaspoon of turmeric powder in a glass of warm water. If the residue settles at the bottom, it might contain artificial colors.',
    'chilli powder': 'Add a small amount of chilli powder to a glass of water. Artificial colorants will start to streak in the water immediately.',
    'sugar': 'Mix sugar in water and shake vigorously. Pure sugar will dissolve completely, while adulterated sugar may leave a residue.',
    'tea leaves': 'Put tea leaves in a glass of water. Pure tea leaves will sink, while colored or artificial leaves may float.',
    'coffee powder': 'Add coffee powder to a glass of water. Pure coffee will sink immediately, while adulterated coffee may stay on the surface.',
    'ghee': 'Heat a small quantity of ghee. Pure ghee will melt easily and leave no residue, while adulterated ghee may contain impurities or residues.',
    'honey': 'Add honey to a glass of water. Pure honey will settle at the bottom in a lump, while adulterated honey may dissolve quickly or spread.',
    'olive oil': 'Place a drop of olive oil on paper. Pure olive oil will not leave any grease stains when the paper is pressed, while adulterated oil may leave stains.',
    'mustard seeds': 'Put mustard seeds in a glass of water. Pure seeds will sink, while colored or adulterated seeds may float or change the color of the water.',
    'salt': 'Dissolve salt in water. Pure salt will dissolve completely without leaving any residue, while adulterated salt may leave impurities.',
    'hing': 'Mix asafoetida with water. Pure asafoetida will dissolve quickly and evenly, while adulterated asafoetida may leave gritty or uneven residue.',
    'butter': 'Melt butter in a pan. Pure butter will melt evenly without separating, while adulterated butter may separate into components.',
    'elaichi': 'Add cardamom powder to a glass of water. Pure powder will sink immediately, while adulterated powder may float or leave color.',
    'jeera': 'Place cumin seeds in a glass of water. Pure seeds will sink, while colored or adulterated seeds may float or change water color.',
    'coriander powder': 'Mix coriander powder in water. Pure powder will dissolve easily, while adulterated powder may leave residues or not dissolve completely.',
    'vinegar': 'Mix vinegar with baking soda. Pure vinegar will react and fizz immediately, while adulterated vinegar may have delayed or no reaction.',
    'milk powder': 'Mix milk powder in water. Pure powder will dissolve completely without leaving lumps or residues, while adulterated powder may not dissolve properly.',
    'besan': 'Mix gram flour in water. Pure gram flour will dissolve smoothly without lumps, while adulterated gram flour may leave residues or not dissolve properly.',
    'mango pulp': 'Add mango pulp to water. Pure pulp will mix evenly, while adulterated pulp may leave lumps or color streaks.',
    'coconut oil': 'Place a drop of coconut oil on paper. Pure oil will not leave any marks when the paper is pressed, while adulterated oil may leave stains.',
    'jaggery': 'Mix jaggery in water and heat. Pure jaggery will dissolve completely and smoothly, while adulterated jaggery may contain impurities or not dissolve properly.',
    'saffron': 'Add saffron to warm milk. Pure saffron will release color and fragrance quickly, while adulterated saffron may not impart color or fragrance.',
    'flour': 'Mix flour with water. Pure flour will form a smooth dough without impurities or discoloration, while adulterated flour may have lumps or discoloration.',
    'haldi powder': 'Add turmeric powder to a glass of lukewarm water. Pure powder will settle at the bottom without leaving any color, while adulterated powder may dissolve or leave color.'
}


# Function to provide adulteration information
def Adulteration_Information(user_id):
    adulterant = random.choice(list(adulterants_info.keys()))
    fun_fact = adulterants_info[adulterant]
    bot.send_message(user_id, fun_fact)
    send_main_menu(user_id)

# Function to provide detection tests
def Detection_Tests(user_id, food_item):
    if food_item in detection_tests:
        test_info = detection_tests[food_item]
        bot.send_message(user_id, test_info)
    else:
        bot.send_message(user_id, "Sorry, I don't have a detection test for that food item.")
    send_main_menu(user_id)

# Function to provide nutritional information
def Nutritional_Information(user_id, food_item):
    if food_item in nutri_info:
        info = nutri_info[food_item]
        info_message = (
            f"Nutritional Information for {food_item}:\n"
            f"Calories: {info['calories']} kcal\n"
            f"Protein: {info['protein']} g\n"
            f"Carbohydrates: {info['carbs']} g\n"
            f"Fiber: {info['fiber']} g"
        )
        bot.send_message(user_id, info_message)
    else:
        bot.send_message(user_id, "Sorry, I don't have nutritional information for that food item.")
    send_main_menu(user_id)

# Function to handle asking a question
def Ask_a_Question(user_id):
    bot.send_message(user_id, "You pressed 'Ask a Question'! Action performed.")
    send_main_menu(user_id)

# Function to send the main menu options
def send_main_menu(user_id):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton("Adulteration Information"),
        telebot.types.KeyboardButton("Detection Tests"),
        telebot.types.KeyboardButton("Nutritional Information"),
        telebot.types.KeyboardButton("Ask a Question"),
        telebot.types.KeyboardButton("Bye"),
    ]
    keyboard.add(*buttons)
    bot.send_message(user_id, "What would you like to do next?", reply_markup=keyboard)

# User state to track the current operation
user_state = {}

# Handling all text messages
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.chat.id
    text = message.text.lower()  # Convert text to lowercase for case insensitivity

    if text == "adulteration information":
        Adulteration_Information(user_id)
        user_state[user_id] = None  # Reset the user state
    
    elif text == "detection tests":
        bot.send_message(user_id, "Please enter the name of the food item you want to test for adulteration:")
        user_state[user_id] = "detection_test"
    
    elif text == "nutritional information":
        bot.send_message(user_id, "Please enter the name of the food item you want to get Nutritional Information:")
        user_state[user_id] = "nutritional_info"
   
    elif text == "ask a question":
        Ask_a_Question(user_id)
        user_state[user_id] = None  # Reset the user state
    
    elif text == "bye":
        bot.send_message(user_id, "Goodbye! If you have more questions, feel free to ask anytime.")
        user_state[user_id] = None  # Reset the user state
    
    elif user_state.get(user_id) == "detection_test":
        food_item = text.lower()
        Detection_Tests(user_id, food_item)
        user_state[user_id] = None  # Reset the user state
    
    elif user_state.get(user_id) == "nutritional_info":
        food_item = text.lower()
        Nutritional_Information(user_id, food_item)
        user_state[user_id] = None  # Reset the user state
    
    else:
        bot.send_message(user_id, "Invalid selection. Please choose from the available buttons.")
        send_main_menu(user_id)  # Ensure main menu options are sent after an invalid selection

# Continuously listen for messages
bot.infinity_polling()
