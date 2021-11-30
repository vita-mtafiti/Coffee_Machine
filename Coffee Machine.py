class CoffeeMachine():
    def __init__(self, water, milk, coffee, cups, cash):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.cash = cash

    def display(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.cash} of money""")

    def buy(self):
        buy_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_choice == "1":
            self.coffee_brewing(250, 0, 16, 1, 4)
        elif buy_choice == "2":
            self.coffee_brewing(350, 75, 20, 1, 7)
        elif buy_choice == "3":
            self.coffee_brewing(200, 100, 12, 1, 6)
        elif buy_choice == "back":
            return

    def coffee_brewing(self, water_used, milk_used, coffee_used, cups_used, income):
        if self.water < water_used:
            print("Sorry, not enough water!")
        elif self.milk < milk_used:
            print("Sorry, not enough milk!")
        elif self.coffee < coffee_used:
            print("Sorry, not enough coffee beans!")
        elif self.cups < cups_used:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            print()
            self.water -= water_used
            self.milk -= milk_used
            self.coffee -= coffee_used
            self.cups -= cups_used
            self.cash += income

    def process(self, some_list):
        self.water += some_list[0]
        self.milk += some_list[1]
        self.coffee += some_list[2]
        self.cups += some_list[3]

    def fill(self):
        fill_water = int(input("Write how many ml of water you want to add:"))
        fill_milk = int(input("Write how many ml of milk you want to add:"))
        fill_coffee = int(input("Write how many grams of coffee beans you want to add:"))
        fill_cups = int(input("Write how many disposable coffee cups you want to add:"))
        fill_ingredients = [fill_water, fill_milk, fill_coffee, fill_cups]
        self.process(fill_ingredients)

    def take(self):
        print(f"I gave you ${self.cash}")
        self.cash = 0

    def main(self):
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.display()
        elif action == "exit":
            exit()

coffee_cup = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    coffee_cup.main()

