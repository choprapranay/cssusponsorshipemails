import requests
import dotenv
import os

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

search_query = "best guitar picks"

url = "https://www.googleapis.com/customsearch/v1"
params = {
    "q": search_query,
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID,
}

response = requests.get(url, params=params).json()
print(response)