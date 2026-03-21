#!/bin/bash
cd /home/pi/your-bot
git reset --hard
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart discord-bot