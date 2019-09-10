from basketball_model import BasketBallPlayer
from handball_model import HandBallPlayer


class calculate:
    def __init__(self):
        self.team_points_basketball = dict()
        self.BasketBallPlayer_list = []
        self.players_nickname = []
        self.team_points_handball = dict()
        self.handball_player_list = []

    def set_handball_player(self, player_content):
        """
        set all data i have in list of handball player
        """
        player = player_content.split(";")
        if player[1] in self.players_nickname:
            self.bug_file("you have same NickName called %s" % player[1])
            raise KeyError("NickName should be unique")

        h_player = HandBallPlayer()
        h_player.player_name = player[0]
        h_player.nickname = player[1]
        h_player.player_number = player[2]
        h_player.team_name = player[3]
        h_player.position = player[4]
        h_player.goals_made = int(player[5])
        h_player.goals_received = int(player[6])
        self.players_nickname.append(h_player.nickname)
        h_player.rating = self.calculate_Player_Rating_handball(
            h_player.position, h_player.goals_made, h_player.goals_received
        )

        self.calculate_team_points_handball(h_player)
        self.handball_player_list.append(h_player)

    def calculate_team_points_handball(self, h_player):
        """
        calculate team points 
        :param h_player: HandBallPlayer class
        """
        if h_player.team_name not in self.team_points_handball:
            self.team_points_handball[h_player.team_name] = h_player.goals_made
        else:
            self.team_points_handball[h_player.team_name] += h_player.goals_made

    def calculate_Player_Rating_handball(self, position, goals_made, goals_received):
        """
        calculate player rating 
        """
        if position.lower() == "g":
            rating = 50 + (5 * goals_made) - (2 * goals_received)
        elif position.lower() == "f":
            rating = 20 + (1 * goals_made) - (1 * goals_received)
        else:
            self.bug_file("you write wrong position")
            raise Exception("unknow position")
        return rating

    def set_basketball_player(self, player_content):
        """
        set all data i have in list of basketball player
        """
        player = player_content.split(";")
        if player[1] in self.players_nickname:
            self.bug_file("you have same NickName called %s" % player[1])
            raise KeyError("NickName should be unique")

        B_player = BasketBallPlayer()
        B_player.player_name = player[0]
        B_player.Nick_name = player[1]
        B_player.player_number = player[2]
        B_player.team_name = player[3]
        B_player.position = player[4]
        B_player.scored_points = int(player[5])
        B_player.rebounds = int(player[6])
        B_player.assists = int(player[7])
        B_player.rating = self.calculate_Player_Rating_basketball(
            B_player.position, B_player.scored_points, B_player.rebounds, B_player.assists
        )
        self.players_nickname.append(B_player.Nick_name)
        self.calculate_team_points_basketball(B_player)
        self.BasketBallPlayer_list.append(B_player)

    def calculate_team_points_basketball(self, B_player):
        """
        calculate team points
        """
        if B_player.team_name not in self.team_points_basketball:
            self.team_points_basketball[B_player.team_name] = B_player.scored_points
        else:
            self.team_points_basketball[B_player.team_name] += B_player.scored_points

    def calculate_Player_Rating_basketball(self, position, scored_points, rebounds, assists):
        """
        calculate player rating 
        """
        if position.lower() == "g":
            rating = (2 * scored_points) + (3 * rebounds) + (1 * assists)
        elif position.lower() == "f":
            rating = (2 * scored_points) + (2 * rebounds) + (2 * assists)
        elif position.lower() == "c":
            rating = (2 * scored_points) + (1 * rebounds) + (3 * assists)
        else:
            self.bug_file("you write wrong position")
            raise Exception("unknow position")
        return rating

    def bug_file(self, message):
        f = open("MVP/BUG.txt", "a+")
        f.write(message + "\n")
        f.close()

