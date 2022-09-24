# Linear Regression with One Feature

Linear regression is maybe the most known and easy ml algorithm, and in this chapter I'll write an even easiest version, using only one feature.

## 1. What is Linear Regression

Linear regression is a statistic method of fitting a linear line for n samples such that the line is best fitted for all of them. 

Suppose we have n samples that are represented in (x, y) pairs. Those samples can stand for anything: x can be a house size and y can be the house price, x may be the temperature and y may be number of ice creams sold or any other example. The set of samples may look like that:

|x|y|
|--|--|
|3|7|
|4|6|
|6|10|
|...|...|

We can draw the points on a graph. Here is a graph that shows ten sample points:

<img width="602" alt="001 - lr samples" src="https://user-images.githubusercontent.com/10141163/192054023-b01c91c1-da6f-4937-831a-b2f437b67109.png">

The question that interests us is "if we get a new x value, what would be the expected y for it?". In other woeds, we want to **predict** the value of y from the given x and by using the historical knowledge of (x, y) samples. It's a very interesting question - as we said earlier, suppose (x, y) represents the temperature of the day (x) and amount of ice cream sold (y). The ability to predict how many ice cream would be sold according to a given temperature can help in my decisions as ice cream seller.

So, how can we predict? We try to draw a straight line on the graph, that is the best for all the points. Ideally we could draw a line that goes through all the points, but that not very practical since the points are'nt really originated from a pure mathematic equation. So we try to draw a line that would be close enough.

For example, let's look at the previous samples on the graph, with two lines:

<img width="568" alt="002 - lr lines" src="https://user-images.githubusercontent.com/10141163/192104575-250ae062-56ee-4212-b85c-2eae18f7485b.png">

You can see that the green line is above all the sample points, hence it does not reflect a good line for this set of samples. 

The red line is better - although it does not run through all the points, you can see that all the points arranged pretty close to this line, hence it would be a better line.

After we drew the regression line, we can predict an outcome of a new value - given the line equation, and a sample x, we will assign x in the line equation and get the y. The y is called the **the predicted value** for x, and the more the line would be better fitted to the points, the better the prediction would be.

## 2. Linear Regression in Practice
Given a vector $X = (x_1, x_2, ..., x_n)$ of n input values, and $Y = (y_1, y_2, ..., y_n)$ which are the vector of dependent variables to X repectively, our goal is to find a function $h(x) = \theta_0 + \theta_1 x$ where $\theta = (\theta_0, \theta_1)$ is the coefficient vector.

A good question is how can we find the optimal line? We'll deal with that later, but first we have to define a way of estimating how good (or bad) is our line.

## 3. Cost Function
Given the X, Y vectors as mentioned earlier, and the $\theta$ (the line's coefficients vector) we'll define the **error** of an input xi as:

$err_i = y_i - \hat{y}_i$

where $y_i$ is the real result for input $x_i$ and $\hat{y}_i = h(x_i) = \theta_0 + \theta_1 x_i$

In simple words - the error per input is simply the difference between the real value and the value that was calculated with the line.
Let's see an example:

Suppose $\theta = (2, 3)$, so the line equation is h(x) = 2 + 3x. Here is some values and their errors:

|x|y|$\hat{y}$|err|
|--|--|--|--|
|2|3|8|-5|
|1|6|5|1|
|3|13|11|2|

Now we have the individual error for each sample, but what is the total cost of our line? There are many methods of estimating the total cost, I'll use here one of the most popular - **Mean Squared Error (MSE)**. The MSE is calculated by taking each individual error and take square of it, sum all squares and divide with the number of samples (i.e. the mean). Here is the formula for that:

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

Let's calculate the MSE for our example:

$MSE = \frac{(-5)^2 + 1^2 + 2^2}{3} = \frac{30}{3} = 10$

Is it good or bad? Hard to tell, but you can play with the coefficients and see how they effect the MSE, for example, if the coefficient were (1, 2), would it make the things better or worse? Try it yourself.

## 4. Gradient Descent
We can easily pick some random coefficients and create a line equation from them, but we want to minimize the cost function, and to do that we have to have some way of altering and changing the coefficients so the result would be diminishing the cost. The trick is called **gradient descent** and it goes like that:

1. we'll take the first derivative of the MSE with respect to $\theta_1$ and $\theta_2$. Remember that the derivative (gradient) gives the direction on which we have to move toward the minimum. 
2. We'll assign X in the gradients and multiply the result with the **learning rate** which is a number that determines how big (or small) would be the adjusting steps.
3. Now we'll decrease the result from the coefficients and we have new values for the coefficients.

We can iterate this as long as we want, after some time the coefficients arrive a plateau and won't change anymore.

Here are the formulas:

Reminder, the mse function is: $$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

The partial derivative of MSE w.r.t $\theta_0$ is:
$$\frac{\partial MSE}{\partial \theta_0} = \frac{2}{n}\sum_{i=1}^{n}(\theta_0 + \theta_1 x_i - y_i)$$


The partial derivative of MSE w.r.t $\theta_1$ is:
$$\frac{\partial MSE}{\partial \theta_1} = \frac{2}{n}\sum_{i=1}^{n}(\theta_0 + \theta_1 x_i - y_i)x_i$$

After calculating the gradients, we can adjust the coefficients like that:

$\theta_0 = \theta_0 - \alpha \frac {\partial MSE}{\partial \theta_0}$

$\theta_1 = \theta_1 - \alpha \frac {\partial MSE}{\partial \theta_1}$

where $\alpha$ is the learning rate.



