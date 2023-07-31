import json
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score should nvr be reset
        self.high_score = self.get_save_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_save_high_score(self):
        """Retrieve the saved high score, if exists"""
        path = Path('__pycache__/game_saves.json')
        try:
            high_score_saved = json.loads(path.read_text())
            if high_score_saved is not None:
                result = high_score_saved
            else:
                result = 0
        except FileNotFoundError:
            result = 0
        else:
            return result
