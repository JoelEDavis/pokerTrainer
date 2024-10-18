from base_game import PokerGame


class CashGame(PokerGame):
    def __init__(self, players, blind_structure, min_buy_in, max_buy_in):
        super().__init__(players, blind_structure, starting_stack=None)
        self.min_buy_in = min_buy_in
        self.max_buy_in = max_buy_in

    def handle_buy_in(self, player):
        # Add logic for player buy-ins in cash games
        pass
