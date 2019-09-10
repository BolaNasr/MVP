from calculateMVP import calculate


class MVP:
    def __init__(self):
        self.calculate_class = calculate()
        self.start = False

    def readFile(self):
        f = open("MVP/data/Basketball.txt", "r")

        content = f.readlines()

        for player in content:
            if "BASKETBALL" in player:
                self.start = True
                continue
            elif not self.start:
                self.calculate_class.bug_file("wrong files format")
            self.calculate_class.set_basketball_player(player_content=player)
        self.Winner_player("BASKETBALL")

        # reset to start calculate another one
        self.reset()

        f = open("MVP/data/handball.txt", "r")
        content = f.readlines()
        for player in content:
            if "HANDBALL" in player:
                self.start = True
                continue
            elif not self.start:
                self.calculate_class.bug_file("wrong files format")
            self.calculate_class.set_handball_player(player_content=player)

        self.Winner_player("HANDBALL")

    def Winner_player(self, type_game):

        if type_game == "HANDBALL":
            print("************************ HANDBALL************************")
            team_points = self.calculate_class.team_points_handball
            player_list = self.calculate_class.handball_player_list
        else:
            print("************************ BASKTBALL************************")
            team_points = self.calculate_class.team_points_basketball
            player_list = self.calculate_class.BasketBallPlayer_list
        team_winner = ""
        team_score = 0
        for team, score in team_points.items():
            if score > team_score:
                team_winner = team
                team_score = score

        player_winner = ""
        player_score = 0
        for player in player_list:
            if player.team_name == team_winner:
                player.rating += 10
                if player_score < player.rating:
                    player_score = player.rating
                    player_winner = player.player_name

        print("MVP: {} with rating :{}".format(player_winner, player_score))
        print("Winner Team: {} with score :{}".format(team_winner, team_score))

    def reset(self):
        self.start = False
        self.calculate_class.players_nickname = []


if __name__ == "__main__":
    MVP().readFile()
