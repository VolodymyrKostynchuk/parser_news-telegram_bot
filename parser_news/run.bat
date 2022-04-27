@echo off 

set TOKEN=TOKEN

cd parser/
python main.py 

cd .. 

cd tg_bot/
python main.py

pause