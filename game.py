money = 0
tool = "teeth"


def display_status():
 print(f"\nMoney: ${money}")
 print(f"Tool: {tool}")
 print()

def reset_game():
    global money, tool
    money = 0
    tool = "teeth"
    print("Game has been reset. You're back to using your teeth.")


display_status()

while money < 1000:
    
    action = input("\nWhat do you want to do? (cut/buy/reset/quit): ")
    display_status()
    if action == "cut":
        if tool == "teeth":
            money += 1
            print("You cut the grass using your teeth and earned $1.")
        elif tool == "scissors":
            money += 5
            print("You cut the grass using the rusty scissors and earned $5.")
        elif tool == "push lawnmower":
            money += 50
            print("You cut the grass using the old-timey push lawnmower and earned $50.")
        elif tool == "battery-powered lawnmower":
            money += 100
            print("You cut the grass using the fancy battery-powered lawnmower and earned $100.")
        elif tool == "team of starving students":
            money += 250
            print("You cut the grass using the team of starving students and earned $250.")
        else:
            print("Invalid action. Please try again.")
        display_status()      
    elif action == "buy":
        if tool == "teeth":
            if money >= 5:
                money -= 5
                tool = "scissors"
                print("You bought a pair of rusty scissors!")
            else:
                print("You don't have enough money to buy scissors.")
        elif tool == "scissors":
            if money >= 25:
                money -= 25
                tool = "push lawnmower"
                print("You bought an old-timey push lawnmower!")
            else:
                print("You don't have enough money to buy a push lawnmower.")
        elif tool == "push lawnmower":
            if money >= 250:
                money -= 250
                tool = "battery-powered lawnmower"
                print("You bought a fancy battery-powered lawnmower!")
            else:
                print("You don't have enough money to buy a battery-powered lawnmower.")
        elif tool == "battery-powered lawnmower":
            if money >= 500:
                money -= 500
                tool = "team of starving students"
                print("You hired a team of starving students!")
            else:
                print("You don't have enough money to hire a team of starving students.")
        else:
            print("Invalid action. Please try again.")
    elif action == "reset":
        reset_game()
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")



if money >= 1000 and tool == "team of starving students":
    print("\nCongratulations! You won the game!")
else:
    print("\nGame over!")


