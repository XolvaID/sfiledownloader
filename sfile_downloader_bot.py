"""
NO RECODE, ALL CREDITS GOES TO :
github.com/xolvaid & github.com/kgyya
"""


from telethon import TelegramClient, events
import re,json,requests,os
from bs4 import BeautifulSoup as bs
api_id = os.get("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
ses = requests.Session()
bot = TelegramClient('bot',api_id,api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern=r"/login(?: |$)(.*)"))
async def login(event):
	d = event.pattern_match.group(1)
	email = str(d).split(":")[0]
	pw = str(d).split(":")[1]
	dat = {
   "mail":email,
   "pass":pw,
   "LogIn":"Login"
}
	pos = ses.post("https://sfile.mobi/login.php", data=dat,headers={"User-Agent":"Chrome"})
	if "User Panel" in pos.text:
		raw = ses.get("https://sfile.mobi/user/",headers={"User-Agent":"Chrome"})
		revenue = re.search("Your Revenue: <b>(.*?)</b><br>\s", str(raw.text)).group(1)
		earning = re.search("Total Earning: <b>(.*?)</b>\s", str(raw.text)).group(1)
		downloaded = re.search("Total Downloaded: <b>(.*?)</b><br>\s", str(raw.text)).group(1)
		disk = re.search("Disk space: (.*?)<br/>\s", str(raw.text)).group(1)
		free = re.search("Free space: (.*?) <br/>\s", str(raw.text)).group(1)
		user = re.search("(\w+)\sPanel</h3>", str(raw.text)).group(1)
		await event.reply(f"""**
[@] User       : {user}
[E] Email      : {email}
[$] Revenue    : {revenue}
[+] Downloaded : {downloaded}
[$] Earning    : {earning}
[📁] Total Space: {disk}
[📂] Free Space : {free}**""")



@bot.on(events.NewMessage(pattern=r"/search(?: |$)(.*)"))
async def search(event):
	count = 0
	jud = []
	q = event.pattern_match.group(1)
	url = f"https://sfile.mobi/search.php?q={q}"
	raw = requests.get(url,headers={"User-Agent":"Chrome"}).text
	for list in re.findall('(.*?)</div><div class="list">', raw):
		count += 1
		data = list.strip()
		for href in re.findall('a\shref="(.*?)"',data):
			link = href.strip()
			judul = re.findall('">(.*?)</a>\s', data)
			await event.reply("**LINK: "+link+"\nTITLE: "+str(judul).replace("[","").replace("]","").replace("'","")+"**")




@bot.on(events.NewMessage(pattern=r"/check(?: |$)(.*)"))
async def _(event):
                print(event)
                msg = event.pattern_match.group(1)
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
                await event.reply(f"""**================================
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
		capt = f"""**================================
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
Author : @xolvaid **"""
		r = ses.get(load,headers={"User-Agent":"Chrome"},stream=True,allow_redirects=True)
		open(judul_link,"wb").write(r.content)
		await bot.send_file(event.chat_id,judul_link,reply_to=event.id,caption=capt)

@bot.on(events.NewMessage(pattern="/start"))
async def help(event):
        await event.reply("""** Available Commands:

/login email:password
To Check Revenue.
(WARNING: DO NOT USE THIS CMD IF YOU IN GROUPS)
=================
/search <query>
To Search Files.
=================
/download <link>
To Download Files.
=================
/check <link>
To Check Files Information.
=================
/help
To Show This Message.
=================
Author : github.com/xolvaid & github.com/Kgyya
Bot       : @sfile_downloader_bot
=================**""")

@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
	await event.reply("""** Available Commands:

/login email:password
To Check Revenue.
(WARNING: DO NOT USE THIS CMD IF YOU IN GROUPS)
=================
/search <query>
To Search Files.
=================
/download <link>
To Download Files.
=================
/check <link>
To Check Files Information.
=================
/help
To Show This Message.
=================
Author : github.com/xolvaid & github.com/Kgyya
Bot       : @sfile_downloader_bot
=================**""")

bot.start()
bot.run_until_disconnected()
