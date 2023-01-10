import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class RetirementCalculator:
    def __init__(self, starting_balance, annual_contribution, interest_rate, years_until_retirement):
        self.starting_balance = starting_balance
        self.annual_contribution = annual_contribution
        self.interest_rate = interest_rate
        self.years_until_retirement = years_until_retirement

    def calculate_balance(self):
        balance = self.starting_balance
        for i in range(self.years_until_retirement):
            balance += self.annual_contribution
            balance *= (1 + self.interest_rate)
        return balance

def update(val):
    starting_balance = starting_balance_slider.val
    annual_contribution = annual_contribution_slider.val
    interest_rate = interest_rate_slider.val
    years_until_retirement = years_until_retirement_slider.val

    calculator = RetirementCalculator(starting_balance, annual_contribution, interest_rate, years_until_retirement)
    balance = calculator.calculate_balance()

    ax.clear()
    ax.plot([0, years_until_retirement], [starting_balance, balance])
    plt.draw()

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

starting_balance_slider = Slider(plt.axes([0.25, 0.1, 0.65, 0.03]), "Starting balance", 0, 100000, valinit=50000)
annual_contribution_slider = Slider(plt.axes([0.25, 0.15, 0.65, 0.03]), "Annual contribution", 0, 10000, valinit=5000)
interest_rate_slider = Slider(plt.axes([0.25, 0.2, 0.65, 0.03]), "Interest rate", 0, 0.1, valinit=0.05)
years_until_retirement_slider = Slider(plt.axes([0.25, 0.25, 0.65, 0.03]), "Years until retirement", 0, 50, valinit=25)

starting_balance_slider.on_changed(update)
annual_contribution_slider.on_changed(update)
interest_rate_slider.on_changed(update)
years_until_retirement_slider.on_changed(update)

plt.show()
