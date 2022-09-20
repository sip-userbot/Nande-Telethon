#==============×==============#
#      Created by: Nande
#=========× Nande ×=========#

FROM nandeuserbot/nandebot:nande

RUN git clone -b Nande-Telethon https://github.com/sip-Userbot/Nande-Telethon /home/nandetelethon/ \
    && chmod 777 /home/nandetelethon \
    && mkdir /home/nandetelethon/bin/

COPY ./sample_config.env ./config.env* /home/nandetelethon/

WORKDIR /home/nandetelethon/

RUN pip install -r requirements.txt

CMD ["bash","start"]
