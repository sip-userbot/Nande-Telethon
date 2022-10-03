NANDE="\n°Nande Userbot Install•"
NANDE+="\n "
NANDE+="\nMenjalankan Nande Userbot di Vps"
NANDE+="\n⚡ Sebelumnya Joinn Grup/Channel ⚡"
NANDE+="\n "
NANDE+="\n📣 Channel: @suportNande"
NANDE+="\n📢 GrupSupport: @NandeSupport"
NANDE+="\n "
LUQ="\n "
echo -e $NANDE
echo -e $LUQ
echo "Waiting..."
echo -e $LUQ
sudo apt update && upgrade -y
sudo apt install git -y
clear
echo -e $NANDE
echo -e $LUQ
echo "Menginstal python3"
echo -e $LUQ
sudo apt install python3
sudo apt install python3-pip
sudo apt install postgresql
sudo apt install neofetch
sudo apt install ffmpeg
sudo apt install curl
sudo apt install megatools
sudo apt install unzip
sudo apt install wget
sudo apt install liblapack-dev
sudo apt install aria2
sudo apt install zip
sudo apt install sudo
sudo apt install python3-wand
sudo apt install postgresql-client
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
cle
echo -e $NANDE
echo -e $LUQ
echo "⚙️ Github Installer"
echo -e $LUQ
clear
echo -e $NANDE
echo -e $LUQ
echo "Cloning Nande Userbot"
echo -e $LUQ
git clone https://github.com/sip-userbot/Nande-Telethon
clear
echo -e $NANDE
echo -e $LUQ
echo "Menginstall Pakages"
echo -e $LUQ
cd Nande-Telethon
pip3 install -U -r requirements.txt
python3 installer/termux.py
