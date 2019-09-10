from Calculate_MVP import Calculate


class BasketBallPlayer:
    def __init__(self):
        player_name = None
        team_name = None
        nick_name = None
        player_number = None
        position = None
        scored_points = None
        rebounds = None
        assists = None
        rating = 0


class BasketBallSystem:
    def __init__(self):

        self.calculate_class = Calculate()
        self.team_points = {}
        self.BasketBallPlayer_list = []
        self.players_nickname = []

    def set_basketball_player(self, player_content):
        """
        set all data i have in list of basketball player
        """
        player = player_content.split(";")
        if player[1] in self.players_nickname:
            self.calculate_class.bug_file("you have same NickName called %s" % player[1])
            raise KeyError("NickName should be unique")

        B_player = BasketBallPlayer()
        B_player.player_name = player[0]
        B_player.nick_name = player[1]
        B_player.player_number = player[2]
        B_player.team_name = player[3]
        B_player.position = player[4]
        B_player.scored_points = int(player[5])
        B_player.rebounds = int(player[6])
        B_player.assists = int(player[7])

        B_player.rating = self.calculate_class.calculate_Player_Rating_basketball(
            B_player.position, B_player.scored_points, B_player.rebounds, B_player.assists
        )
        self.players_nickname.append(B_player.nick_name)

        self.team_points = self.calculate_class.calculate_team_points_basketball(B_player)
        self.BasketBallPlayer_list.append(B_player)

    def get_team_points(self):
        return self.team_points

