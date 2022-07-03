class Coffee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Coffee {self.name}"


class CoffeeMachine:
    water = 400
    milk = 540
    dollar = 550
    beans = 120
    cups = 9

    def remaining(self):
        """
        Displays the stock values of the coffee machine:
        water, milk, coffee beans, disposable cups and the amount of cash.
        """
        print(f'''The coffee machine has:
    {self.water} ml of water
    {self.milk} ml of milk
    {self.beans} g of coffee beans
    {self.cups} disposable cups
    ${self.dollar} of money''')

    def prepare_espresso(self):
        """
        Checks if the coffee machine has enough stock to prepare one cup of espresso.
        If there is enough stock returns the class Сoffee("Espresso").
        :return:
        """
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.dollar += 4
            return Coffee(name="Espresso")
        else:
            if self.water < 250:
                print('Sorry, not enough water!')
            if self.beans < 16:
                print('Sorry, not enough coffee beans!')
            if self.cups < 1:
                print('Sorry, not enough disposable cups!')

    def prepare_latte(self):
        """
        Checks if the coffee machine has enough stock to prepare one cup of latte.
        If there is enough stock returns the class Сoffee("Latte").
        :return:
        """
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.dollar += 7
            return Coffee(name="Latte")
        else:
            if self.water < 350:
                print('Sorry, not enough water!')
            if self.milk < 75:
                print('Sorry, not enough milk!')
            if self.beans < 20:
                print('Sorry, not enough coffee beans!')
            if self.cups < 1:
                print('Sorry, not enough disposable cups!')

    def prepare_cappuccino(self):
        """
        Checks if the coffee machine has enough stock to prepare one cup of cappuccino.
        If there is enough stock returns the class Сoffee("Cappuccino").
        :return:
        """
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.dollar += 6
            return Coffee(name="Cappuccino")
        else:
            if self.water < 200:
                print('Sorry, not enough water!')
            if self.milk < 10:
                print('Sorry, not enough milk!')
            if self.beans < 12:
                print('Sorry, not enough coffee beans!')
            if self.cups < 1:
                print('Sorry, not enough disposable cups!')

    def buy(self):
        """
        Requests the user what kind of coffee he wants to buy.
        After input, it calls up the coffee preparation function. There is an option to go back to the menu.
        :return:
        """
        type_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if type_coffee == 'back':
            return
        elif type_coffee == '1':
            return self.prepare_espresso()
        elif type_coffee == '2':
            return self.prepare_latte()
        elif type_coffee == "3":
            return self.prepare_cappuccino()

    def fill(self):
        """"
        The function allows you to replenish the coffee machine:
        water, milk, coffee beans, disposable cups.
        """
        add_water = int(input('Write how many ml of water you want to add:'))
        add_milk = int(input('Write how many ml of milk you want to add:'))
        add_beans = int(input('Write how many grams of coffee beans you want to add:'))
        add_cups = int(input('Write how many disposable cups you want to add:'))
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups

    def take(self):
        """The function allows you to cash out the coffee machine.
        """
        print('I gave you ${}'.format(self.dollar))
        self.dollar = 0

    def interaction(self):
        """The function displays a list of actions for the user.
        """
        while True:
            options = input('Write action (buy, fill, take, remaining, exit): ')
            if options == 'exit':
                break
            elif options == 'remaining':
                self.remaining()
            elif options == 'buy':
                self.buy()
            elif options == 'fill':
                self.fill()
            else:
                self.take()


coffee = CoffeeMachine()
coffee.interaction()
