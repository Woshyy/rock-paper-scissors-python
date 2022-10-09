#!/usr/bin/env python3

import random

possible_actions = ["rock", "papper", "scissors"]
while True:
    user_action = input("Rock Papper or Scissors!")
    computer_action = random.choice(possible_actions)

    print("You choose ", user_action, " and the computer choose ", computer_action)

    if (user_action == computer_action):
        print ("It is a tie")
    elif (user_action == "papper"):
        if (computer_action == "rock"):
            print("Papers covers rock! You win")
        else:
            print("Scissors cuts paper! I win")
    elif (user_action == "rock"):
        if (computer_action == "scissors"):
            print("Rock smashes scissors! You win ")
        else:
            print("Papers covers rock! I win")
    else:
        if (computer_action == "papper"):
            print("Scissors cuts papper! You win ")
        else:
            print("Papers covers rock! I win")

    if (input("Do you want to play again? (y/n)") == "n"):
        break
