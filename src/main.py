from fantasy_client import FantasyClient
from logger import LoggerSetup

import os
import re
import logging
import pandas as pd
import argparse

class FantasyPickApp:
    def __init__(self):
        self.client = FantasyClient()
        self.path = str

    def sanitize_filename(self, name: str):
        return re.sub(r'[^\w\-_.]', '_', name.strip()).lower()

    def get_player_scores(self):
        data = self.client.get_split_score()
        players = pd.DataFrame(data['data']['players'])
        split = pd.DataFrame([data['data']['split']])

        split_name = self.sanitize_filename(f'score_{split['name'].iloc[0]}')
        players.to_csv(f'{self.path}/{split_name}.csv', index=False)
        logging.info(f"Scores | Split:{split_name}")

        return players

    def get_individual_players(self, players_id: list[str]):
        players = []
        for player_id in players_id:
            player = self.client.get_player_stats(player_id)

            player_info = pd.DataFrame([player['data']['player']])
            player_upcoming = pd.DataFrame(player['data']['upcomingMatches'])
            player_recent = pd.DataFrame(player['data']['recentMatches'])
            player_games = pd.DataFrame(player['data']['games'])

            role = self.sanitize_filename(player_info['role'].iloc[0])
            name = self.sanitize_filename(player_info['name'].iloc[0])
            player_path = f'{self.path}/players/{role}/{name}'
            os.makedirs(player_path, exist_ok=True)

            player_info.to_csv(f'{player_path}/infos.csv', index=False)
            player_upcoming.to_csv(f'{player_path}/upcomingMatches.csv', index=False)
            player_recent.to_csv(f'{player_path}/recentMatches.csv', index=False)
            player_games.to_csv(f'{player_path}/games.csv', index=False)
            logging.info(f"Player | Role:{role}\tName:{name}")
            players.append(player)
        return players

    def get_markets(self):
        market = self.client.get_market_stats()
        market_round = pd.DataFrame([market['data']['round']])
        market_teams = pd.DataFrame(market['data']['teams'])
        market_players = pd.DataFrame(market['data']['roundPlayers'])

        round_name = self.sanitize_filename(market_round['name'].iloc[0])
        market_path = f'{self.path}/market/{round_name}'
        os.makedirs(market_path, exist_ok=True)

        market_round.to_csv(f'{market_path}/infos.csv', index=False)
        market_teams.to_csv(f'{market_path}/teams.csv', index=False)
        market_players.to_csv(f'{market_path}/players.csv', index=False)
        logging.info(f"Market | Round:{round_name}")

        return market

    def get_all(self):
        player = self.get_player_scores()
        self.get_individual_players(player['proPlayerId'])
        self.get_markets()

class ArgumentParserBuilder:
    @staticmethod
    def build():
        parser = argparse.ArgumentParser(description="Fetch Fantasy data and export as CSV files.")
        parser.add_argument(
            "--path",
            type=str,
            required=False,
            help="Directory where CSV files will be saved. (default: './data')"
        )
        parser.add_argument(
            "--data",
            type=str,
            choices=["scores", "individual", "markets"],
            required=False,
            help="Type of data to fetch: 'scores' for player scores, 'individual' for detailed stats of specific players, or 'markets' for current market data.  If omitted, all data will be fetched."
        )
        parser.add_argument(
            "--player_id",
            type=str,
            nargs='+',
            required=False,
            help="One or more player IDs. Required only when --data is set to 'individual'."
        )
        return parser

if __name__ == '__main__':
    LoggerSetup().setup()

    parser = ArgumentParserBuilder.build()
    args = parser.parse_args()

    app = FantasyPickApp()

    app.path = args.path or 'data'
    os.makedirs(app.path, exist_ok=True)

    if args.data == "scores":
        app.get_player_scores()
    elif args.data == "individual":
        player = args.player_id or app.get_player_scores()
        app.get_individual_players(player)
    elif args.data == "markets":
        app.get_markets()
    else:
        app.get_all()