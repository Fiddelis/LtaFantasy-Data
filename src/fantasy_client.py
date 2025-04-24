import requests
import logging
import pandas as pd

class FantasyClient:
    def __init__(self):
        self.url_base = "https://api.ltafantasy.com/"

    def __request(self, url: str):
        headers = { "Accept": "application/json" }
        response = requests.get(url, headers)

        if response.status_code == 200:
            return response.json()
        logging.error("Error trying to receive status")
        return  

    def get_split_score(self, split_id: str = None) -> pd.DataFrame:
        url = f'{self.url_base}/player-stats'
        response = self.__request(url)
        return pd.DataFrame(response) if response else pd.DataFrame()

    def get_player_stats(self, player_id: str) -> pd.DataFrame:
        url = f'{self.url_base}/player-stats/{player_id}'
        response = self.__request(url)
        return pd.DataFrame(response) if response else pd.DataFrame()
    
    def get_market_stats(self) -> pd.DataFrame:
        url = f'{self.url_base}/market'
        response = self.__request(url)
        return pd.DataFrame(response) if response else pd.DataFrame()