"""
FILL THE API VARIABLE WITH YOUR API HASH, API ID, AND BOT TOKEN

exit?, Use : ctrl + x and ctrl + y

Getting Trouble?, Contact https://t.me/xolvaid
"""


from telethon import TelegramClient, events
import re,json,requests,env
from bs4 import BeautifulSoup as bs
api_id = "YOUR API ID"
api_hash = "YOUR API HASH"
bot_token = "YOUR BOT TOKEN"

bot = TelegramClient('bot',api_id,api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern=r"/check(?: |$)(.*)"))
async def _(event):
                print(event)
                msg = event.pattern_match.group(1)
                await bot.send_message(event.message.peer_id.user_id,"**Processing...**")
                ses = requests.Session()
                url = str(msg)
                raww = ses.get(url,headers={"User-Agent":"Chrome"}).text
                soup = bs(raww, "html.parser")
                down = re.search('href="https://sfile.mobi/download(.*?)"',raww).group(1)
                load = "https://sfile.mobi/download"+down
                judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
                oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
                pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
                tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
                tag = re.search("i> - (.*?)<", raww).group(1)
                penis = re.search('.html">(.*?)<',raww).group(1)
                ukuran = re.search("Download File (.*?)<",raww).group(1)
                await bot.send_message(event.message.peer_id.user_id,f"""**================================
[+] URL           : {url}
[*] Title         : {judul_link}
[#] Tags          : {tag}
[] File Type     : {penis}
[-] Bio File      :
[-] File Size     : {ukuran}
[=] Uploaded By   : {oleh}
[?] Upload Date   : {pada}
[*] Total Download: {tot_down}
================================
Bot    : @sfile_downloader_bot
Author : @xolvaid **""")


@bot.on(events.NewMessage(pattern=r"/download(?: |$)(.*)"))
async def _(event):
		print(event)
		msg = event.pattern_match.group(1)
		await bot.send_message(event.message.peer_id.user_id,"**Processing...**")
		ses = requests.Session()
		url = str(msg)
		raww = ses.get(url,headers={"User-Agent":"Chrome"}).text
		soup = bs(raww, "html.parser")
		down = re.search('href="https://sfile.mobi/download(.*?)"',raww).group(1)
		load = "https://sfile.mobi/download"+down
		judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
		oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
		pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
		tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
		tag = re.search("i> - (.*?)<", raww).group(1)
		penis = re.search('.html">(.*?)<',raww).group(1)
		ukuran = re.search("Download File (.*?)<",raww).group(1)
		await bot.send_message(event.message.peer_id.user_id,f"""**================================
[+] URL           : {url}
[*] Title         : {judul_link}
[#] Tags          : {tag}
[] File Type     : {penis}
[-] Bio File      :
[-] File Size     : {ukuran}
[=] Uploaded By   : {oleh}
[?] Upload Date   : {pada}
[*] Total Download: {tot_down}
================================
Bot    : @sfile_downloader_bot
Author : @xolvaid **""")
		r = ses.get(load,headers={"User-Agent":"Chrome"},stream=True,allow_redirects=True)
		open(judul_link,"wb").write(r.content)
		await bot.send_file(event.message.peer_id.user_id,judul_link)

@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
	chat = event.message.peer_id.user_id
	await bot.send_message(chat,"""** Available Commands:

/download <link>
To Download Files.

/check <link>
To Check Files Information.

/help
To Show This

Author : github.com/xolvaid & github.com/Kgyya
Bot       : @sfile_downloader_bot**""")

bot.start()
bot.run_until_disconnected()
