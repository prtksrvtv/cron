import os
from dotenv import load_dotenv

load_dotenv()

cata={'Main App':os.environ['MAIN_APP'], 'DB Search API':os.environ['DB_SEARCH_API'], 'Telegram API':os.environ['TELEGRAM_API'], 'Emailer API':os.environ['EMAILER_API']}

os.system("echo Draugar Cron Job")
os.system("echo To keep the APIs and MicroServices Live")
for x in cata:
    os.system("echo Performing Curl on "+x)
    os.system('curl '+ cata[x])
    os.system("echo Success")

