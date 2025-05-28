import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year', y= 'CSIRO Adjusted Sea Level', data= df)

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = list(range(df['Year'].min(), 2051))
    y_all = [slope_all * x + intercept_all for x in x_all]
    plt.plot(x_all, y_all, 'r')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = list(range(2000, 2051))
    y_recent = [slope_recent * x + intercept_recent for x in x_recent]
    plt.plot(x_recent, y_recent, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

