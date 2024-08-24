import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26303261"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e924187728893dd49765079342ea3d21")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Cicada:<db_password>@cicada.nho1f.mongodb.net/?retryWrites=true&w=majority&appName=Cicada")
