class Calculate:
    def __init__(self):
        self.team_points_handball = dict()
        self.team_points_basketball = dict()

    def bug_file(self, message):
        f = open("MVP/BUG.txt", "a+")
        f.write(message + "\n")
        f.close()

    def calculate_team_points_basketball(self, B_player):
        """
        calculate team points
        """

        if B_player.team_name not in self.team_points_basketball:
            self.team_points_basketball[B_player.team_name] = B_player.scored_points
        else:
            self.team_points_basketball[B_player.team_name] += B_player.scored_points
        return self.team_points_basketball

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

    def calculate_team_points_handball(self, h_player):
        """
        calculate team points 
        :param h_player: HandBallPlayer class
        """
        if h_player.team_name not in self.team_points_handball:
            self.team_points_handball[h_player.team_name] = h_player.goals_made
        else:
            self.team_points_handball[h_player.team_name] += h_player.goals_made
        return self.team_points_handball

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
