#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b 𝗡𝗮𝗻𝗱𝗲 𝘛𝘦𝘭𝘦𝘵𝘩𝘰𝘯 https://github.com/sip-Userbot/Nande-Telethon /home/nandetelethon/ \
    && chmod 777 /home/nandetelethon \
    && mkdir /home/nandetelethon/bin/

COPY ./sample_config.env ./config.env* /home/nandetelethon/

WORKDIR /home/nandetelethon/

RUN pip install -r requirements.txt

CMD ["bash","start"]
