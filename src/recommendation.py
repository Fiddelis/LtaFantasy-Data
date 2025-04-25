from fantasy_client import FantasyClient
import pandas as pd
import itertools
import argparse

class Recommendation:
    def __init__(self, role_weights=None, budget=50):
        self.client = FantasyClient()
        self.budget = budget
        self.role_weights = role_weights or {
            'top': 1,
            'jungle': 2,
            'mid': 3,
            'bottom': 2,
            'support': 1
        }

    def run(self):
        market = self.client.get_market_stats()
        players_data = market['data']['roundPlayers']
        df = pd.DataFrame(players_data)

        df = df[['proPlayerId', 'summonerName', 'role', 'price']]
        df['priority'] = df['role'].map(self.role_weights)
        df['weighted_value'] = df['price'] * df['priority']

        # Separate players by role
        roles = ['top', 'jungle', 'mid', 'bottom', 'support']
        role_groups = [df[df['role'] == role].to_dict('records') for role in roles]

        # Generate all combinations with exactly one player per role
        combinations = list(itertools.product(*role_groups))

        valid_teams = []
        for team in combinations:
            total_price = sum(player['price'] for player in team)
            if total_price <= self.budget:
                total_weighted_value = sum(player['weighted_value'] for player in team)
                valid_teams.append((team, total_weighted_value))

        best_team, best_score = max(valid_teams, key=lambda x: x[1])

        print(f"\nBest team (budget ≤ {self.budget}):\n")
        total_price = 0
        for player in best_team:
            player['role'] = player['role'].capitalize()
            total_price = total_price + player['price']

        
        df_best_team = pd.DataFrame([{
            'Role': player['role'],
            'Name': player['summonerName'],
            'Price': f"{player['price']:.2f}",
            'Priority': player['priority']
        } for player in best_team])

        print(df_best_team.to_string(index=False))
        print(f'\nTotal price: {total_price:.2f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate best fantasy team based on lane priorities and budget.")
    parser.add_argument("--top", type=int, required=False, help="Priority for the Top lane (default: 1)")
    parser.add_argument("--jungle", type=int, required=False, help="Priority for the Jungle role (default: 2)")
    parser.add_argument("--mid", type=int, required=False, help="Priority for the Mid lane (default: 3)")
    parser.add_argument("--bottom", type=int, required=False, help="Priority for the Bottom lane (default: 2)")
    parser.add_argument("--support", type=int, required=False, help="Priority for the Support role (default: 1)")
    parser.add_argument("--budget", type=float, required=False, default=50, help="Maximum budget to build the team (default: 50)")

    args = parser.parse_args()

    custom_weights = {
        'top': args.top if args.top is not None else 1,
        'jungle': args.jungle if args.jungle is not None else 1,
        'mid': args.mid if args.mid is not None else 1,
        'bottom': args.bottom if args.bottom is not None else 1,
        'support': args.support if args.support is not None else 1,
    }

    app = Recommendation(role_weights=custom_weights, budget=args.budget)
    app.run()
