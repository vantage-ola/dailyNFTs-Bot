import requests

from dotenv import load_dotenv
import os
from pathlib import Path

# rapid api credentials
path = Path('.') / '.env'
load_dotenv(dotenv_path=path)
api_key = os.getenv('API_KEY')

url = "https://top-nft-sales.p.rapidapi.com/sales/30d"

headers = {
    'x-rapidapi-host': "top-nft-sales.p.rapidapi.com",
    'x-rapidapi-key': "{api_key}"
    }

#response = requests.request("GET", url, headers=headers)

##print(response.text)
#print(api_key)


