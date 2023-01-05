import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(1880, 2051)
    y = x * res.slope + res.intercept
    plt.plot(x, y)

    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(2000, 2051)
    y = x * res.slope + res.intercept
    plt.plot(x, y)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
