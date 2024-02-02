import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

print(subprocess.run(['curl', os.environ['MAIN_APP']], shell=True))
print(subprocess.run(['curl', os.environ['DB_SEARCH_API']], shell=True))
print(subprocess.run(['curl', os.environ['TELEGRAM_API']], shell=True))
print(subprocess.run(['curl', os.environ['EMAILER_API']], shell=True))
