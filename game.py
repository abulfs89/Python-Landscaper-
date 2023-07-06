
money = 0
tools = []
tool_prices = {
    "teeth": 0,
    "scissors": 5,
    "push lawnmower": 25,
    "battery-powered lawnmower": 250,
    "team of starving students": 500
}
tool_earnings = {
    "teeth": 1,
    "scissors": 5,
    "push lawnmower": 50,
    "battery-powered lawnmower": 100,
    "team of starving students": 250
}


def display_status():
    print(f"\nMoney: ${money}")
    print(f"Tools: {tools}")


def reset_game():
    global money, tools
    money = 0
    tools = []
    print("Game has been reset.")


# def sell_tool(tool_name):
#     global money, tools
#     if tool_name in tools:
#         tool_value = tool_prices[tool_name] // 2
#         money += tool_value
#         tools.remove(tool_name)
#         print(f"You sold {tool_name} for ${tool_value}.")
#     else:
#         print("You don't have that tool to sell.")


display_status()

while money < 1000:
    action = input("\nWhat do you want to do? (cut/buy/sell/reset/quit): ")
    display_status()
    if action == "cut":
        earning = sum([tool_earnings[tool] for tool in tools])
        money += earning
        print(f"You cut the grass using your tools and earned ${earning}.")
    elif action == "buy":
        tool_name = input("Which tool do you want to buy? (scissors/push lawnmower/battery-powered lawnmower/team of starving students): ")
        if tool_name in tool_prices:
            if money >= tool_prices[tool_name]:
                money -= tool_prices[tool_name]
                tools.append(tool_name)
                print(f"You bought a {tool_name}!")
            else:
                print("You don't have enough money to buy that tool.")
        else:
            print("Invalid tool. Please try again.")

    elif action == "sell":
        tool_name = input("Which tool do you want to sell? (scissors/push lawnmower/battery-powered lawnmower/team of starving students): ")
    if tool_name in tools:
        tool_value = tool_prices[tool_name] // 2
        money += tool_value
        tools.remove(tool_name)
        print(f"You sold {tool_name} for ${tool_value}.")   
    else:
        print("You don't have that tool to sell.")
    if action == "reset":
        reset_game()
    elif action == "quit":
        break
    else:
        print("Invalid action. Please try again.")
    
    display_status()


if money >= 1000:
    print("\nCongratulations! You won the game!")
else:
    print("\nGame over!")

display_status()
