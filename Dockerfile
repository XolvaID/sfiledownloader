FROM python:3.10.0

RUN git clone https://github.com/xolvaid/sfiledownloader /home/sfile \

WORKDIR /home/sfile

CMD python3 sfile_downloader_bot.py
