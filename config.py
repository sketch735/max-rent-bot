import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("MAX_RENT_BOT_TOKEN")
ADMIN_ID: int = int(os.getenv("MAX_RENT_ADMIN_ID", "0"))

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден в .env файле!")

if not ADMIN_ID:
    raise ValueError("❌ ADMIN_ID не найден в .env файле!")

print("✅ Конфиг успешно загружен")
print(f"ADMIN_ID: {ADMIN_ID}")