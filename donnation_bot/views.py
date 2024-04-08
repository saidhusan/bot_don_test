
import json
import multiprocessing

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .credentials import TELEGRAM_API_URL,TOKEN
import telebot



bot = telebot.TeleBot(TOKEN)


@csrf_exempt
def telegram_bot(request):
  print("connect")
  if request.method == 'POST':
    message = json.loads(request.body.decode('utf-8'))
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    bot.reply_to(message, message.text)

  #  send_message("sendMessage", {
   #   'chat_id': f'your message {text}'
    #})
  return HttpResponse('ok')

#def send_message(method, data):
 # return requests.post(TELEGRAM_API_URL + method, data)


def webhook(request):
    bot.remove_webhook()
    bot.set_webhook(url="https://donnationbottest-55407c9b6d9e.herokuapp.com/getpost/")
    return HttpResponse("WebHook set Done!")


def StartBot(request):
    bot.delete_webhook()
    p = multiprocessing.Process(target=BotRun())
    p.start()
    return HttpResponse('ServerStarted')


def BotRun():
    bot.polling(none_stop=True)
