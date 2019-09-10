from Calculate_MVP import Calculate


class HandBallPlayer:
    def __init__(self):
        player_name = None
        nickname = None
        player_number = None
        team_name = None
        position = None
        goals_made = None
        goals_received = None


class HandBallSystem:
    def __init__(self):
        self.players_nickname = []
        self.handball_player_list = []
        self.team_points = {}
        self.calculate_class = Calculate()

    def set_handball_player(self, player_content):
        """
        set all data i have in list of handball player
        """
        player = player_content.split(";")
        if player[1] in self.players_nickname:
            self.calculate_class.bug_file("you have same NickName called %s" % player[1])
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

        h_player.rating = self.calculate_class.calculate_Player_Rating_handball(
            h_player.position, h_player.goals_made, h_player.goals_received
        )

        self.team_points = self.calculate_class.calculate_team_points_handball(h_player)

        self.handball_player_list.append(h_player)

    def get_team_points(self):
        return self.team_points

