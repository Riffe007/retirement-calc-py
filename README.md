# retirement-calc-py
# Retirement Calculator
This is a simple Python script that calculates the balance at retirement based on four input variables:

Starting balance
Annual contribution
Interest rate
Years until retirement
The script uses the RetirementCalculator class to perform the calculations, and it also uses the Slider class from matplotlib.widgets to create sliders that allow the user to adjust the input variables and see the resulting balance on a graph.

To use the script, simply run it with Python:

# Copy code
python retirement_calculator.py
The sliders will appear at the bottom of the window, and you can adjust them to see how the balance at retirement changes.

Note that this script requires the following packages:

matplotlib
numpy
Make sure these packages are installed before running the script.

# Customization
You can customize the default values of the input variables by modifying the following lines in the code:

# Copy code
starting_balance_slider = Slider(plt.axes([0.25, 0.1, 0.65, 0.03]), "Starting balance", 0, 100000, valinit=50000)
annual_contribution_slider = Slider(plt.axes([0.25, 0.15, 0.65, 0.03]), "Annual contribution", 0, 10000, valinit=5000)
interest_rate_slider = Slider(plt.axes([0.25, 0.2, 0.65, 0.03]), "Interest rate", 0, 0.1, valinit=0.05)
years_until_retirement_slider = Slider(plt.axes([0.25, 0.25, 0.65, 0.03]), "Years until retirement", 0, 50, valinit=25)
The valinit parameter in each of these lines sets the default value of the corresponding input variable. You can adjust these values to customize the default inputs.

# Limitations
This script is intended as a simple example of how to create a retirement calculator using
classes and sliders in Python, and it is not intended to be a comprehensive retirement planning
tool. There are many factors that can affect retirement planning, such as inflation, taxes, and
other sources of income, that are not taken into account by this script. It is important to consult
with a financial advisor or do further research before making any decisions about retirement planning.
