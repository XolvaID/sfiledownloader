# SFILE DOWNLOADER BOT

<h3 align="center">Deploy To Heroku Using Simple Method</h3>
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/xolvaid/sfiledownloader"><img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy to Heroku" target="_blank"/></a></p>

<h3 align="center">Deploy To Heroku Using Terminal</h3>

```
apt-get install nano
apt-get install python3
apt-get install git
apt-get install nodejs
npm i -g heroku
heroku login -i # Buat Akun Terlebih Dahulu Di heroku.com
git clone https://github.com/xolvaid/sfiledownloader
cd sfiledownloader
nano sfile_downloader_bot.py
rm -rf app.json && rm -rf Dockerfile && rm -rf heroku.yml
heroku create sfiledownloader
heroku git:remote -a sfiledownloader
heroku buildpacks:add heroku/python
pip freeze > requirements.txt
git add .
git commit -am "Xolva Gamtenk"
git push heroku main
# Start Bot Using:
heroku ps:scale worker=1
```


## Updates & support
Follow Channel [@xolvacode](https://t.me/xolvacode) & [@channel_justinfo](https://t.me/channel_justinfo)

## Tutorial?
<h1 align="center">YNTKTS:v</h1>

## Contact Me
<p align="center">
  <a href="https://github.com/XolvaID" target="_blank"><img src="https://img.shields.io/badge/Github-XolvaID-green?style=for-the-badge&logo=github"></a>
  <a href="https://t.me/XolvaID" target="_blank"><img src="https://img.shields.io/badge/Telegram-%40XolvaID_-red?style=for-the-badge&logo=telegram"></a>
</p>

## Big Thanks For [Kgyya](https://github.com/Kgyya) For Helping This Project.
