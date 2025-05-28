class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise TypeError("Title must be an instance of str and must be longer than 0 characters!")
        self._title = title


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        return "Title cannot be changed once the game is instantiated!"

    def results(self):
        #pass
        return [result for result in Result.all if result.game == self]

    def players(self):
        #pass
        all_players = [result.player for result in self.results()]
        uniq_players_set = set(all_players)
        return list(uniq_players_set)

    def average_score(self, player):
        #pass
        all_scores_for_this_player = [result.score for result in self.results() if result.player == player]
        return sum(all_scores_for_this_player)/len(all_scores_for_this_player)
        
class Player:
    all = []
    def __init__(self, username):
        self.username = username
        self.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or len(value)< 2 or len(value) > 16:
            raise TypeError("Username must be an instance of str and must be between 2 and 16 characters, inclusive!")
        self._username = value

    def results(self):
        #pass
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        #pass
        all_games = [result.game for result in self.results()]
        uniq_games_set = set(all_games)
        return list(uniq_games_set)

    def played_game(self, game):
        #pass
        if game in self.games_played():
            return True
        return False

    def num_times_played(self, game):
        #pass
        all_games_played = [result.game for result in self.results()]
        return all_games_played.count(game)
    
    @classmethod
    def highest_scored(cls, game):
        top_player = None
        top_avg_score = -1  # Assuming all scores are >= 1

        for player in cls.all:
            if player.played_game(game):
                avg_score = game.average_score(player)
                if avg_score > top_avg_score:
                    top_avg_score = avg_score
                    top_player = player

        return top_player

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if not isinstance(score, int) or score < 1 or score > 5000:
            return None
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        return "Score cannot be changed once the result is instantiated!"
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise TypeError("Player must be an instance of Player!")
        self._player = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise TypeError("Player must be an instance of Player!")
        self._game = value