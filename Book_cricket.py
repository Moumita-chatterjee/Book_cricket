'''Created on: 4-03-2025
Created by: Moumita
Objective:1. Book cricket assignment using random library
'''
#import ramdom library for selecting random numbers
import random

class Cricket:
    def __init__(self):
        self.team1 = []
        self.team2 = []
        self.over =0
        self.balls = 0
        self.team1_score = 0
        self.team2_score = 0
        #file = open("E:/Workspace/Python/Classes/python_classes/Book_cricket_log.txt","w+")

    def team_player(self):
        self.no_players = int(input("Enter number of players per team (between:1-5):"))
        for team in range (self.no_players):
            team_a = input("Enter player's name for team1:")
            self.team1.append(team_a)
            team_b = input("Enter player's name for team2:")
            self.team2.append(team_b)


    def view_team(self):
        print("\n","Team1:",self.team1,"\n","Team2:",self.team2)

    def overs(self):
        print("*" * 80)
        self.over = int(input("Choose overs between 1-5:"))
        self.total_balls = self.over * 6
        print("Total Overs =",self.over)
        self.balls = self.total_balls

    def toss(self):
        value = ["head", "tail"]  # String value is taken to store head and tail value
        while True:
            #random.choice(value)  # For string use random.choice
            if random.choice(value) == "head":
                print("Team1 won the Toss and batting first")
                print("*" * 80)
                return "team1"
            else:
                print("Team B won the toss and batting first")
                print("*" * 80)
                return "team2"
            break

    def match(self, toss_winner):
        for team_num, team in enumerate([self.team1, self.team2], start=1):
            # Decide batting order based on toss
            if (toss_winner == "team1" and team_num == 1) or (toss_winner == "team2" and team_num == 2):
                print(f"\n--- Team {team_num} is Batting ---")
            else:
                # Reset balls for second innings
                self.balls = self.total_balls
                print(f"\n--- Team {team_num} is Batting ---")

            total_runs = 0
            for i in range(self.no_players):
                player = team[i]
                print(f"\nNew player: {player}")
                player_run = 0
                while self.balls > 0:
                    run = random.randint(0, 6)
                    print(f"Ball {self.total_balls - self.balls + 1}: ", end="")

                    if run == 0:
                        print("OUT!")
                        print(f"{player} scored {player_run} runs.")
                        break
                    else:
                        print(f"{run} runs")
                        player_run += run
                        self.balls -= 1
                        input("Press Enter for next ball...")

                total_runs += player_run

            print(f"Total Score for Team {team_num}: {total_runs}")
            if team_num == 1:
                self.team1_score = total_runs
            else:
                self.team2_score = total_runs

    def winner(self):
        print("*"*80)
        if self.team1_score > self.team2_score:
            difference_score = self.team1_score - self.team2_score
            print("Team A wins the match by ", difference_score, "runs")
        elif self.team2_score > self.team1_score:
            differ_score = self.team2_score - self.team1_score
            print("Team B wins the match by ", differ_score, "runs")
        else:
            print("Match Draw")




if __name__ == "__main__":
  
    cricket = Cricket()
    cricket.team_player()
    cricket.view_team()
    cricket.overs()
    toss_winner = cricket.toss()
    cricket.match(toss_winner)
    cricket.winner()


