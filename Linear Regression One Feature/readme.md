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

