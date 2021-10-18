FROM mrismanaziz/main

RUN git clone -b sfile https://github.com/mrismanaziz/Man-Userbot /home/sfile/ \
    && chmod 777 /home/sfile \
    && 

COPY ./sample_config.env ./config.env* /home/sfile/

WORKDIR /home/sfile/

CMD ["python3", "sfile_downloader_bot.py"]
