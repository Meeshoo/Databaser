from django.db import models

from dotenv import load_dotenv
import os

load_dotenv()
botName = os.getenv('Pynamo_DB_Endpoint')