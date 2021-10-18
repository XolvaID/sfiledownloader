FROM xolvaid/main

RUN git clone -b sfiledownloader https://github.com/XolvaID/sfiledownloader /home/sfile/ \
    && chmod 777 /home/sfiledownloader \
    && mkdir /home/sfiledownloader/bin

COPY ./sample_config.env ./config.env* /home/sfiledownloader/

WORKDIR /home/sfiledownloader/

CMD ["python3", "sfile_downloader_bot.py"]
