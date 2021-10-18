FROM xolvaid/sfiledownloader:buster

RUN git clone https://github.com/xolvaid/sfiledownloader && cd sfiledownloader

CMD ["python3", "sfile_downloader_bot.py"]
