---
quang.bui.2@city.ac.uk: N3061/INM430 Principles of Data Science
---

# DIY Exercises - 1 : Outliers
Here we consider ways in which we can identify outliers and the effect that these have.

Load the data on properties of cars  into a pd dataframe
Plot suitable graphs to show the distributions and help indicate outliers of priceand mileage (e.g. with boxplots) and their joint distribution (e.g. with a scatterplot)
(Visually) identify the outliers.
Add two new columns to the dataframe called isOutlierPrice, isOutlierMileage. For the price column, calculate the mean and standard deviation. Use the standard deviation and mean to try to identify outliers for these two variables and mark them with a 1 in the isOutlierPrice and isOutlierMilage columns. For example, you could look for values that are more than 2 standard deviations away from the mean. You can either use a loop and the Pandas loc() function to access and update values, or you can use the more efficient Pandas methods that are summarised in the Cheat Sheet that you used a bit of last week.
Show these "outliers" using a different colour (hue) in the plot. Are these what you would consider outliers? Observe whether they are the same as you would mark them.
Optional: Use Mahalanobis distance to identify 2D outliers. You can compute a 2D Mahalanobis distance for each row using a scipy's cdist() function). For this, you need to find the 2D mean vector and find the 2D Mahalanobis distance of each point to this mean vector. Finally, colour all the points according to their Mahalanobis Distance. Here is a matplotlib example that uses colouring and choose an appropriate colour map here (use a sequential lightness-based colour scheme). Compare your outlier observation step-3 to the resulting scatterplot.
# DIY Exercises - 2 : Q-Q Plots
Q-Q Plots are designed for visually comparing your distributions to known distributions. Here we use statsmodels qqplot() function to compare the distributions of our data to known theoretical distributions.

Download the csv data file from WHO on Tuberculosis (from Week01)  . Information on the data can be found on WHO's web page. You may need to replace missing values before you start.
Pick one of the columns from the Tuberculosis data and compare to a normal distribution. See this link for various distributions and functions to use in data sampling and in particular consider sampling from the normal distribution in this case as explained in this example. Use the statsmodels qqplot() function to generate a qqplot. Compare this to a histogram representation.
# DIY Exercises - 3 : Distributions & Sampling & Robust Statistics
During the lectures, we discussed on how we make inferences based on the samples we get from distributions and how volatile they can be. We looked into this interactive tool to discuss how much descrtiptive statistics can vary and tell a different story regarding the underlying data and the models that they follow. You can take some time to play with this interactive tool to observe that.

In the first part of this example, we'll get samples of varying sizes from different distributions and observe how the descriptive statistics change.

Randomly sample data from a known distribution (you can choose to sample from a normal distribution as we did on Step-2 above) with varying sample sizes of n = 5, 10, 100 and varying s = standard deviations (try 3 different values, you can have a look at this Wikipedia figure to get inspiration on the standard deviation measures) and make observations on how well the "underlying distribution" is preserved in the sampled data you are drawing from.
In order to do this:

Sample n data points from a distribution for a given variance s.
Compute the mean, standard deviation, skewness and kurtosis statistics for each sampling round
Repeat these two steps with varying n and varying s, i.e., covering all the n vs. s combinations, 3 x 3 = 9 combinations.
Once you save all the values above, observe how they change over the different conditions (i.e., the varying sample size and varying standard deviation you set for the underlying distribution) you are setting.
You can even consider visualising that data if you will.
(Optional) Also try the above for a different underlying distribution such as a Poisson. The only part that needs to change is the part you sample the data and of course the underlying parameters for a Poisson distribution -- refer to this link for the Scipy function for a Poisson distribution.
(Optional) And also try the same process to generate a simple bimodal distribution (a link to a Wikipedia page with an image of a bi-Modal distribution) and observe how the statistics vary this time. Hint: you can generate a bimodal distribution as a mixture of two Gaussion distributions with non-overlapping parameters.
Here, we'll briefly look into how robust statistics can vary compared to their non-robust counterparts. As we discussed in the lectures, robust statistics are statistics that are more resilient to outliers and can provide cleaner estimations in cases where the data has non-standard behaviour.

Choose a number of columns with different shapes, for instance, "e_prev_100k_hi" is left skewed or some columns where the variation is high or you notice potential outliers. You can make use of a series of boxplots to exploratively analyse the data for outliers, a link here for boxplots.
For the chosen columns, estimate both the conventional and the robust descriptive statistics and compare. Some couples to try are: mean vs. median, standard deviation vs. inter-quartile range, standard deviation vs.median absolute deviation (statsmodels have a function for MAD). Observe how these pairs deviate from each other based on the characteristics of the underlying data.