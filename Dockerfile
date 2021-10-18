FROM python:3.10.0

RUN git clone https://github.com/xolvaid/sfiledownloader /home/sfiledownloader/

WORKDIR /home/sfiledownloader/

CMD python3 -m sfile_downloader_bot
