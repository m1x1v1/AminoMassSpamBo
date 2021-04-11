from colorama import init
from colorama import Fore, Back, Style
init()
import time
import os
from threading import Thread
print(Back.BLACK)
print(Fore.BLUE)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █▄░▄█ ▄▀▀ ▄▀▀ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ █░█░█ ░▀▄ ░▀▄ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀░░░▀ ▀▀░ ▀▀░ ▀▀░ ░▀░")
import amino
from amino import Client
r = 0
email=input("Email/Почта:")
password=input('Password/Пароль:')
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
#  == config == 

msgSpam=input('Message/Сообщение:')
print('MessageTypes/Типы сообщений:Default-0,Transparent-110/100/115/108')
msgType=input('MessageType/Тип Сообщения:')

r = 400;

# == functions ==

def spam(sub_client, chatId, msgSpam, msgType):
	while True:
		try: sub_client.send_message(message=msgSpam, chatId=chatId, messageType=msgType)
		except: pass

def start_thread(sub_client, chatId, msgSpam, msgType):
	global r;
	for i in range(r):
		Thread(target=spam, args=(sub_client, chatId, msgSpam, msgType)).start();
        

# == source    ==

sub_client = amino.SubClient(comId=str(communityId), profile=client.profile)

threads_list = sub_client.get_chat_threads().json;

for t in threads_list:
	Thread(target=start_thread, args=(sub_client, t["threadId"], msgSpam, msgType)).start();

print("Spamming in all chats/Спамим во всех чатах!");
