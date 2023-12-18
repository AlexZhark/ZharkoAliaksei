import requests

class Telegram:
    
    TOKEN = "6632966062:AAGkysdJ4WEUL6ny1XgXh652mDR32FubAys"
    chat_id = "-4005385617"

    def send_message(self):
        message = f'''Имя клиента: {self.name}
Телефон: {self.phone}'''
        url = f"https://api.telegram.org/bot{Telegram.TOKEN}/sendMessage?chat_id={Telegram.chat_id}&text={message}"
        print(requests.get(url).json())
