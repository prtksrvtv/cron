import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

subprocess.run(['curl', os.environ['MAIN_APP']], shell=True)
subprocess.run(['curl', os.environ['DB_SEARCH_API']], shell=True)
subprocess.run(['curl', os.environ['TELEGRAM_API']], shell=True)
subprocess.run(['curl', os.environ['EMAILER_API']], shell=True)
