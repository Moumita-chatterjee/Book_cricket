'''Created on: 4-03-2025
Created by: Moumita
Objective:1. Book cricket assignment using random library
'''
#import ramdom library for selecting random numbers
import random

#Defining two teams and taking names for both team
def teams():
    team_a = []
    team_b = []
    for names in range(2):
        name_player_a = input("Enter name of player for team A: ")
        team_a.append(name_player_a)

    print("Team A",team_a, "\n")

    for names in range(2):
        name_player_b = input("Enter name of player for team B: ")
        team_b.append(name_player_b)

    print("Team B",team_b)

#Function to perform toss to check who will play first
def toss():
    value = ["head", "tail"] #String value is taken to store head and tail value
    while True:

        random.choice(value) #For string use random.choice
        if random.choice(value) == "head":
            print("Team A won the Toss and batting first")
        elif random.choice(value) == "tail":
            print("Team B won the toss and batting first")
        break


def match():
    run_a = 0
    run_b = 0
    team_one = 0
    team_two =0

    #Two for loops for two teams and no. of players playing in each team is 2
    for players in range (2):
        print("new player of first team ")
        while True:
            random_integer = random.randint(0, 6) #To select random integer use randint
            if random_integer > 0:
                print(random_integer)
                run_a = run_a + random_integer
                print("run", run_a)
                input("press any button to continue next ball: ")
            else:
                print(random_integer)
                print("out")
                break
    print("Total Score of the first team : ", run_a)
    team_one = run_a

    for players in range (2):
        print("new player of second team ")
        while True:
            random_integer = random.randint(0, 6)
            if random_integer > 0:
                print(random_integer)
                run_b = run_b + random_integer
                print("run", run_b)
                input("press any button to continue next ball: ")
            else:
                print(random_integer)
                print("out","\n")
                break
    print("Total Score of second team  : ", run_b)
    team_two = run_b
    if team_one > team_two:
        difference_score = team_one - team_two
        print("Team A wins the match by ",difference_score,"runs")
    else:
        differ_score = team_two - team_one
        print("Team A wins the match by ",differ_score,"runs")

if __name__ == "__main__":
    try:
        print("Welcome to book cricket game","\n")
        print("There will be two teams","\n","Team A and Team B","\n")
        print("Enter names of player for both teams","\n")
        teams()
        print("\n","Begin the toss","\n")
        toss()
        print("Congratulations, let's begin the match","\n")
        match()
    except:
        print("Some error happens")
    finally:
        print("\n","Match is over")

