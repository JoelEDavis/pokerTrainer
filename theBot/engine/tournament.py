from base_game import PokerGame


class Tournament(PokerGame):
    def __init__(
        self, players, blind_structure, starting_stack, blind_increase_interval
    ):
        super().__init__(players, blind_structure, starting_stack)
        self.blind_increase_interval = blind_increase_interval
        self.level = 0  # Track blind level

    def increase_blinds(self):
        # Increase blinds based on time or number of hands played
        self.level += 1
        self.blind_structure.increase_blinds(self.level)

    def check_game_end(self):
        # Tournament ends when one player has all the chips
        active_players = [p for p in self.players if not p.folded]
        if len(active_players) == 1:
            print(f"{active_players[0].name} wins the tournament!")
