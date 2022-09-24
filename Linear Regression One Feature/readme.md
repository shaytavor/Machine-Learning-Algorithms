# Linear Regression with One Feature

Linear regression is maybe the most known and easy ml algorithm, and in this chapter I'll write an even easiest version, using only one feature.

# 1. What is Linear Regression

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
