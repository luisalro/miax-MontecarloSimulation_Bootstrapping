This lab was created by Fernando de la Calle, Python programming professor from mIA-X master's degree at BME Institute.

Check out his LinkedIn profile.

<a href="https://www.linkedin.com/in/fernando-de-la-calle-silos/" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a> 

### Instructions

In this exercise we are going to make a series of projections of the returns, investing in IBEX for a period of 5 years. 
The final goal is to obtain an analysis that tells the investor the average, worst and best situations that could be obtain when making the investment.  We will make these projections in three ways: Simple Monte Carlo, Simple Bootstrapping and Block Bootstrapping.

The steps will be as follows:

1. Load the closing data of the Ibex with dividends that are in the file: <b> ibex_div_data_close.csv. </b>

2. Calculate the logarithmic returns of the series.

3. Plot the distribution of returns (you can use the function seaborn distplot). - > What do you observe ?.

## Method I: Monte Carlo simulation.

4. Calculate the mean and the standard deviation of the returns obtained in the section. Generate a dataframe with 1000 columns, which will be each of the simulations and where they will extend to a term of 5 years, from the last day of the original series. The data of the dataframe is generated randomly following a normal distribution with the mean and the standard deviation obtained previously.

## Method II: Simple Bootstrapping.

5. In Simple Bootstrapping instead of generating the returns randomly,we performed a random sampling of the returns of the original series. Generate the dataframe with the 1000 simulations, randomly sampling with replacement the returns of the original series.

## Method III: Block Bootstrapping.

6. The Block Bootstrapping method is an evolution of the previous one, where the series original is divided into contiguous blocks. Generate the dataframe with the 1000 simulations by randomly sampling the blocks. That is, we obtain the necessary returns of the blocks chosen at random with replacement to generate the simulations. The size of the blocks can be configured. In this case we will use blocks of a size of 20 days.

7. For each method, using the returns of a single simulation (a single column), make a figure of the distribution of the returns (you can use the distplot function of seaborn). Compare the figure for each method. -> What conclusions can you draw?

8. For each method using simulated returns, calculate the time evolution of investing a monetary unit in each of the simulations generated.

9. For each method using the result of the previous section, obtain in a figure where you show 100 simulations.


### Deliverable



