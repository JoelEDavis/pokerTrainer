from functools import wraps


def check_active(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.folded:
            raise ValueError(
                f"{self.name} has already folded and cannot take an action."
            )
        if self.all_in:
            raise ValueError(f"{self.name} is all-in and cannot take an action.")
        return func(self, *args, **kwargs)

    return wrapper


class Player:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack
        self.hole_cards = []
        self.folded = False
        self.current_bet = 0
        self.all_in = False
        self.action_history = []  # Track player actions (optional for future use)

    @check_active
    def bet(self, amount):
        # If the amount is greater than the player's stack, the player goes all-in.
        if amount >= self.stack:
            amount = self.stack
            self.all_in = True

        self.stack -= amount
        self.current_bet += amount
        self.action_history.append(f"bet {amount}")
        return amount

    @check_active
    def call(self, amount):
        # Call amount is min(amount, remaining stack)
        call_amount = min(amount, self.stack)
        self.stack -= call_amount
        self.current_bet += call_amount

        if self.stack == 0:
            self.all_in = True

        self.action_history.append(f"call {call_amount}")
        return call_amount

    @check_active
    def check(self):
        # Check is only allowed if there's no current bet to call
        if self.current_bet > 0:
            raise ValueError("Can't check - bet, call or fold.")

        self.action_history.append("check")
        return 0

    @check_active
    def fold(self):
        if self.folded:
            raise ValueError(f"{self.name} has already folded.")

        self.folded = True
        self.current_bet = 0
        self.action_history.append("fold")
        return 0

    def reset_for_next_round(self):
        # Reset the player's current bet for the next round
        self.current_bet = 0

    def is_active(self):
        # Player is active if they haven’t folded or gone all-in
        return not self.folded and not self.all_in
