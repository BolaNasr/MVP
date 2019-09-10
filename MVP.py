from Calculate_MVP import Calculate
from Basketball_model import BasketBallSystem
from Handball_model import HandBallSystem


class MVP:
    def __init__(self):
        self.start = False
        self.basketball_player = BasketBallSystem()
        self.handball_player = HandBallSystem()
        self.calculate = Calculate()

    def readFile(self):
        f = open("data/Basketball.txt", "r")

        content = f.readlines()

        for player in content:
            if "BASKETBALL" in player:
                self.start = True
                continue
            elif not self.start:
                self.calculate.bug_file("wrong files format")
            self.basketball_player.set_basketball_player(player_content=player)
        self.Winner_player("BASKETBALL")
        f.close()

        # reset to start calculate another one
        self.reset()

        f = open("data/handball.txt", "r")
        content = f.readlines()
        for player in content:
            if "HANDBALL" in player:
                self.start = True
                continue
            elif not self.start:
                self.calculate.bug_file("wrong files format")
            self.handball_player.set_handball_player(player_content=player)
        f.close()

        self.Winner_player("HANDBALL")
        f.close()

    def Winner_player(self, type_game):

        if type_game == "HANDBALL":
            print("************************ HANDBALL************************")
            team_points = self.handball_player.get_team_points()
            player_list = self.handball_player.handball_player_list
        else:
            print("************************ BASKTBALL************************")
            team_points = self.basketball_player.get_team_points()
            player_list = self.basketball_player.BasketBallPlayer_list

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


if __name__ == "__main__":
    MVP().readFile()
