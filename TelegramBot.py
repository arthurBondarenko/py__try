import telebot
import pyowm

bot = telebot.TeleBot("1175108719:AAFpqFe52DWkICwfRcCtzdRIun2vZUq9ItE")
owm = pyowm.OWM('c70315986d991a3cb420534ccbb05af5')


@bot.message_handler(content_types=["text"])
def send_echo(message): 
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()           
    answer = message.text + "\n" + w.get_detailed_status() + "\n"
    answer += str(temp) + "\n" 
    answer += str(wind)


    bot.send_message(message.chat.id, answer)

if __name__ == '__main__':
    bot.polling(none_stop=True)
