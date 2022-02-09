from fetch_data import NFT

from datetime import datetime
import json

today_date = datetime.now().date()
data = NFT(freq="1d") #frequency -> daily


#data_collections = data.collections()
data_nfts =  data.nfts()


with open(f'api/data/{today_date}-nfts-daily.json', 'w+') as f:
    json.dump(data_nfts, f ,ensure_ascii=False, indent=4)

