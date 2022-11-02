---
id: Principles of Data Science
---

# Exercise 1 : Correlation Analysis
We will be analysing a data set made available by the UCI Machine Learning Repository a good place to find example data sets. The data, Communities in the US., combines socio-economic data from the 1990 Census, law enforcement data from the 1990 Law Enforcement Management and Admin Stats survey, and crime data from the 1995 FBI UCR. We provide two versions of the data, a problematic one with some missing values  , and a clean version  where the problematic columns have been removed. Detailed information on column names can be found here  .
Here we investigate how we can perform correlation analysis using Python. Let's start will looking about socialdemographic variables correlate to crime levels.

Load the Communities in the US (cleaned version)  into a Pandas dataframe.
Choose two columns as save as variables. You can choose any but an interesting pair could be "medIncome" and "ViolentCrimesPerPop".
Perform a Pearson correlation and note the correlation value.
Perform a Spearman correlation computation and note the correlation value.
Comment on the differences / similarities in relation to a scatterplot visualisation of the two columns.
Have a go at comparing other columns to crimes. You might want to select some columns and calculate correlation coefficients and draw scatterplots in a loop
# Exercise 2: Significance testing
Here, we will experiment with significance testing (how likely the effect observed in the sample exists in the population) and quantifying the effect sizes. We will work with some Heart Disease data  from US that came from Kaggle (see website for descriptions of the columns).

The sex column has a 0 for female and 1 for male. The target column indicated if the patient has heart disease and where (confusingly) 0 is for those with heart disease

Preparation
Load the data into a pandas dataframe and create additional columns. Create gender and hasHeartDisease columns with the correct values (as above) to make it easier to read.
Does the resting blood pressure (trestbps) differ between those with the disease and those without?
Calculate the means and standard deviations. How do they compare between groups and by how much? If someone asked you whether they vary, what would you say? Discuss in your groups.
Create boxplots and histograms to compare the means and distributions. Make sure you use the same scales on the axes. Tip: If using matplotlib, you might want to use subplots(ncols=2,sharey=True) to create two plots side-by-side with a shared y axis. Same question as above, do these value vary and by how much?
Compare the means using scipy.stat's ttest_ind() function. What is the p-value telling you? Does this relate to the judgements you made above?
Calculate Cohen's d. (Search for "cohen's d" on this page which gives the formula and also the formula for the pooled standard deviation which you also need. Note that it doesn't give the Python code directly - you may need to use math.sqrt() and pow()). Interpret this value and consider how it relates to your other interpretations (above).
Try some other (quantitative) variables and compare between heart disease groups. You could also compare by gender but there's probably no good reason to.
Tip: think about the different between statistical significance and effect size.

Is the proportion of men and women who get heart disease the same?
Calculate the proportion of men and women who have heart disease from the sample. To save you time, this code (is one of many ways that) will do it.

#Count the number with the disease for each gender type
hasDiseaseCount=df[df.hasDisease==True].groupby("gender").count().hasDisease

#Count the number of gender type
totalCount=df.groupby("gender").count()['hasDisease']

#combine into a dataframe (both are indexed with gender, so will be matched) and specify the columns
p=pd.concat([hasDiseaseCount, totalCount], axis=1)
p.columns = ["heartDiseaseCount", "totalCount"]

#create a new column and calculate the proportion
p['propHeartDisease']=p["heartDiseaseCount"]/p["totalCount"]

#print the results
print(p.head())
Look at the numbers in the table. Does there appear to be a difference?
We will use a Null Hypothesis Statistical Testing (NHST) to help determine whether this difference is likely to be present in the population. Use the procedure outlined here in the section labelled "CI for the Difference in Population Proportion". I'd recommend you read the top part of the page too. What you'll be doing is:

Calculate the male population proportion with heart disease.
Calculate the standard error (estimate of standard deviation) for the male population proportion
Calculate the difference in the standard error of male and female population with heart disease
Use this standard error to calculate the difference in the population proportion of males and females with heart disease and construct the CI of the difference.
Interpret the result. Since the null hypothesis is that there's no difference, if the CI of the difference in the population proportion of males and females with heart disease contains 0, then we accept the null hypothesis (and reject the alternative hypothesis) with 95% confidence.
Note that the data are not quite the same (so values will be different) and columns have different names. Don't worry if you're not sure if the result is correct - we'll discuss next time.

What is your answer to the question: Is the proportion of men and women who get heart disease the same? Reflect on the NHST approach for doing this.

## OPTIONAL: An alternative visualisation library: Seaborn
So far we made use of Matplotlib to visualise the data and the results. Seaborn is an alternative (http://seaborn.pydata.org/index.html) and as the developers state "Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.". Seaborn is a layer on top of Matplotlib. Although you can do anything with Matpotlib, Seaborn might make some operations easier. Have a look at the gallery here: http://seaborn.pydata.org/examples/index.html. Also they share a tutorial on their page: http://seaborn.pydata.org/tutorial.html. The examples are the best entry into generating the charts you need. You do not need to use Seaborn in this or following exercises but consider this an alternative.