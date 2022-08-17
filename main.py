from migho_yt import *
from telebot import *
import os


bot = TeleBot('5455649236:AAGcWUp5w5jPhnyqFcNL7ASR5hVAcFpoUe8')

def downxg(message):
	url = message.text
	mp4(url,storage=None)
	ali = info(url)['title']
	if '#' in str(ali):
		newn = str(ali).replace('#','')
		vid = open(f'{newn}.mp4','rb')
		bot.send_video(message.chat.id,video=vid)
		vid.close()
		os.remove(f'{newn}.mp4')
	elif '.' in str(ali):
		nn = str(ali).replace('.','')
		vid = open(f'{nn}.mp4','rb')
		bot.send_video(message.chat.id,video=vid)
		
		vid.close()
		os.remove(f'{nn}.mp4')
	elif '.' and '#' in str(ali):
		x = str(ali).replace('.','')
		xx = x.replace('#','')
		vid = open(f'{xx}.mp4','rb')
		bot.send_video(message.chat.id,video=vid)
		vid.close()
		os.remove(f'{newn}.mp4')
	else:
		Ali = str(ali)
		vidxx = open(f'{Ali}.mp4','rb')
		bot.send_video(message.chat.id,vidxx)
		vidxx.close()
		os.remove(f'{Ali}.mp4')
@bot.message_handler(func=lambda m:True)
def ss(m):
	downxg(m)
	

bot.infinity_polling()
