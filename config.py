from dotenv_config import Config
config = Config('.env')
import os


USER=config('USER')
PASS=config('PASS')