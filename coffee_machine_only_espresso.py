class CoffeeMachine:
    def __init__(self):
        self.machine_stocks = {'water': 400, 'beans': 120, 'cups': 2}
        self.cash = 550
        self.espresso = {'water': 200, 'beans': 15, 'cups': 1}
        self.turn = 'on'

    def print_status(self):
        """
        Displays the stock values of the coffee machine:
        water, milk, coffee beans, disposable cups and the amount of cash.
        """
        status = self.machine_stocks
        print(f'''
The coffee machine has:
{status['water']} ml of water
{status['beans']} g of coffee beans
{status['cups']} disposable cups
${self.cash} of money"
''')

    def choose_action(self):
        """The function displays a list of actions for the user.
        """
        action = input('Write action (buy espresso(1), fill(2), take(3), remaining(4), exit(5)):')
        if action == '1':
            self.buy()
        elif action == '2':
            self.fill()
        elif action == '3':
            self.take()
        elif action == '4':
            self.print_status()
        elif action == '5':
            self.turn = 'off'

    def buy(self):
        """The function starts stock check and coffee preparation.
        """
        if self.checking_stocks():
            print("I have enough resources, making you a coffee!")
            self.prepare_espresso()

    def checking_stocks(self):
        """The function checks that there are enough supplies to prepare one cup of espresso.
        """
        absent = []
        if self.machine_stocks['water'] < self.espresso['water']:
            absent.append('water')
        if self.machine_stocks['beans'] < self.espresso['beans']:
            absent.append('beans')
        if self.machine_stocks['cups'] < self.espresso['cups']:
            absent.append('cups')
        if not absent:
            return True
        else:
            print(f"Sorry, not enough {absent}")

    def prepare_espresso(self):
        """The function subtracts the ingredients for preparing one cup of espresso from the total supply
        and replenishes the cash account. At the end, informs about the readiness of coffee.
        """
        self.machine_stocks['water'] -= 200
        self.machine_stocks['beans'] -= 15
        self.machine_stocks['cups'] -= 1
        self.cash += 4
        print('Espresso ready.')

    def fill(self):
        """"
        The function allows you to replenish the coffee machine:
        water, coffee beans, disposable cups.
        """
        add_water = int(input('Write how many ml of water you want to add:'))
        add_beans = int(input('Write how many grams of coffee beans you want to add:'))
        add_cups = int(input('Write how many disposable cups you want to add:'))
        self.machine_stocks['water'] += add_water
        self.machine_stocks['beans'] += add_beans
        self.machine_stocks['cups'] += add_cups

    def take(self):
        """The function allows you to cash out the coffee machine.
        """
        print('I gave you ${}'.format(self.cash))
        self.cash = 0


def main():
    coffee_machine = CoffeeMachine()
    while True:
        coffee_machine.choose_action()
        if coffee_machine.turn == 'off':
            break


if __name__ == '__main__':
    main()
