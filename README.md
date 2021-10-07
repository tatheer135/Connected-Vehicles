# Connected-Vehicles
need to make website for V2V
Need to add templates, static files etc

A connected car is one that has its own connection to the internet, usually via a wireless local area network (WLAN) that allows the car to share internet access and data with other devices inside and outside the car. 

Simple Linear Regression
Simple linear regression is useful for finding relationship between two continuous variables. 
One is predictor or independent variable and other is response or dependent variable. It 
looks for statistical relationship but not deterministic relationship. Relationship between two 
variables is said to be deterministic if one variable can be accurately expressed by the other. 
For example, using temperature in degree Celsius it is possible to accurately predict 
Fahrenheit. Statistical relationship is not accurate in determining relationship between two 
variables. For example, relationship between height and weight.
The core idea is to obtain a line that best fits the data. The best fit line is the one for which 
total prediction error (all data points) are as small as possible. Error is the distance between 
the point to the regression line.
Real-time example
We have a dataset which contains information about relationship between ‘number of hours 
studied’ and ‘marks obtained’. Many students have been observed and their hours of study 
and grade are recorded. This will be our training data. Goal is to design a model that can 
predict marks if given the number of hours studied. Using the training data, a regression line 
is obtained which will give minimum error. This linear equation is then used for any new 
2
data. That is, if we give number of hours studied by a student as an input, our model should 
predict their mark with minimum error.
Y(predicted) = b0 + b1*x
The values b0 and b1 must be chosen so that they minimize the error. If sum of squared error 
is taken as a metric to evaluate the model, then goal to obtain a line that best reduces the 
error.
If we don’t square the error, then positive and negative point will cancel out each other.
For model with one predictor,
(Intercept Calculation)
(Co-efficient Formula)
