class DataLogger:
    def __init__(self):
        self.data = []

    def log_action(self, player, action, current_state):
        self.data.append(
            {
                "player": player.name,
                "action": action,
                "stack": player.stack,
                "current_state": current_state,
                # Add more relevant details...
            }
        )

    def log_outcome(self, winner, amount):
        self.data.append(
            {
                "winner": winner.name,
                "amount_won": amount,
                # Other outcome details...
            }
        )

    def export_to_file(self, filename):
        # Export collected data for ML training
        pass
