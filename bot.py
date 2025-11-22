import telebot
import requests

bot = telebot.TeleBot("8293760781:AAEzBA8E93ZNQ078g42XddIeroFiclgfrtc")
API_KEY = "7912c24b567deb740e210248968d527f"


# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hello! 🌤\nPlease write the name of the city to get current weather:"
    )


# Shahar nomini qabul qilish
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        # Agar shahar topilmasa
        if res.status_code != 200 or "main" not in data:
            bot.send_message(message.chat.id, "City not found. ❌ Please check the spelling.")
            return

        # Ob-havo ma'lumotlarini olish
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        desc = data['weather'][0]['description'].capitalize()

        # Javob xabari
        weather_text = (
            f"Weather in {city}:\n"
            f"🌡 Temperature: {temp}°C\n"
            f"🤔 Feels like: {feels_like}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind speed: {wind_speed} m/s\n"
            f"☁️ Condition: {desc}"
        )

        bot.send_message(message.chat.id, weather_text)

    except Exception:
        bot.send_message(message.chat.id, "Something went wrong! ❌ Please try again.")


# Botni ishga tushirish
bot.polling(none_stop=True)
