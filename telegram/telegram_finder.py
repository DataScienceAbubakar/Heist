from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.types import User

# Replace these with your own values from https://my.telegram.org
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

# Function to search for accounts based on keywords
def search_telegram_profiles(keywords):
    with TelegramClient('session_name', api_id, api_hash) as client:
        for keyword in keywords:
            print(f"Searching for accounts related to: {keyword}")
            result = client(SearchRequest(q=keyword, limit=50))  # Adjust limit as needed
            for user in result.users:
                if isinstance(user, User):
                    print(f"Username: @{user.username}, Name: {user.first_name} {user.last_name}")

if __name__ == "__main__":
    # Input keywords to search for
    keywords = input("Enter keywords separated by commas: ").split(',')
    keywords = [keyword.strip() for keyword in keywords]
    search_telegram_profiles(keywords)