import requests
from decouple import config

# rapid api credentials
API_KEY = config('NFT_API_KEY')

# API parameters
# https://rapidapi.com/NovusAPI/api/top-nft-sales/

url = "https://top-nft-sales.p.rapidapi.com"
headers = {
    'x-rapidapi-host': "top-nft-sales.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
    }


class NFT:

    """
     A class to store endpoints and fetch data from api.

     ...

     Attributes
     ----------
     freq : str
        Frequency of api endpoints, e.g "7d" means weekly.

        30d -> Monthly
        7d -> Weekly
        1d -> Daily

    
    
    Methods
    ----------
    nfts():
        Fetches nfts data from the api.

    collections():
        Fetches nft collections from the api.
    """

    def __init__(self, freq):

        """ 
        Neccessary attributes for a NFT object. 
        
        Parameters
        ----------
        freq : str
            Frequency of api endpoints, e.g "7d" means weekly.
        """
        self.freq = freq

    def nfts(self):

        """
        Returns NFT sales from api.

        """
        endpoint=("{}/sales/{}".format(url, self.freq))
        return (requests.request("GET", endpoint, headers=headers).json())

    def collections(self):

        """
        Returns NFT collections from api.
        
        """

        endpoint=("{}/collections/{}".format(url, self.freq))
        return (requests.request("GET", endpoint, headers=headers).json())