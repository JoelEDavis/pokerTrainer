from deck import Deck


class PokerGame:
    def __init__(self, players, blind_structure, starting_stack):
        self.players = players
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
        self.blind_structure = blind_structure  # Can be static or dynamic
        self.starting_stack = starting_stack

    def reset_game(self):
        # Reset deck, community cards, player states, etc.
        self.deck.shuffle()
        self.community_cards = []
        for player in self.players:
            player.reset_for_next_hand(self.starting_stack)

    def play_hand(self):
        # Modular function to play a single hand of poker
        self.deal_hole_cards()
        self.betting_round()

        self.deal_flop()
        self.betting_round()

        self.deal_turn()
        self.betting_round()

        self.deal_river()
        self.betting_round()

        self.showdown()
