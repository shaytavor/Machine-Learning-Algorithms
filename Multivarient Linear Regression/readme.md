# Multivarient Linear Regression

We already saw how to create a simple linear regression model. This model had one input feature - x - and our goal was to fit a line to it, of the form:

$h(x) = \theta_0 + \theta_1 x$

In this chapter we'll see how to expand this model to more than one feature.

## 1. What is multivarient linear regression

Suppose we have a set of samples, and for each sample we take n features. For example, suppose we measure the temperature (x1), wind speed (x2) and humidity (x3)
and with these values we count how many people bought ice cream (y). The temperature, wind and humidity are called **features**. 

As with simple uni-varient linear regression, we want to fit a line that is the best for all samples and on all features. This is called **multivarient linear regression**.

The outcome should be a hypothessis function:

$h(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + ... + \theta_nx_n$

where $[x_1, ..., x_n]$ is the features values for a single sample, and $[\theta_0, ..., \theta_1]$ is the coefficients vector for the line.

## 2. Representing the data

Since multivarient regression involves a lot of variables, it's easier to write it with matrix writing.

First of all, we see that we have n features, but n+1 coefficients (since $\theta_0$ is the intercept and doesn't multiply any x). For convinience we'll expand 
the input features vector to contains another "dummy" feature - x0 - which would be equal to 1. So the features vector for a single sample would look like that:

$[1, x_1, ..., x_n]$

We are given m samples, each of them consists of n features, plus the y observation. So we can represent this input as a matrix:

$$\begin{bmatrix}1 & x^{(1)}_1 & x^{(1)}_2 & ... & x^{(1)}_n & y^{(1)} \\
1 & x^{(2)}_1 & x^{(2)}_2 & ... & x^{(2)}_n & y^{(2)}\\
...\\
1 & x^{(m)}_1 & x^{(m)}_2 & ... & x^{(m)}_n & y^{(m)}\end{bmatrix}$$

- The first column of 1's is the column added artificially as discussed.
- $x^{i}_j$ is the value of the jth feature of the ith sample
- $y^{i}$ is the observed result of the ith sample.

We want to create the h(x) function, that would be:

$$\begin{bmatrix}1 & x^{(1)}_1 & x^{(1)}_2 & ... & x^{(1)}_n \\
1 & x^{(2)}_1 & x^{(2)}_2 & ... & x^{(2)}_n\\
...\\
1 & x^{(m)}_1 & x^{(m)}_2 & ... & x^{(m)}_n\end{bmatrix} \cdot 
\begin{bmatrix}
{\theta_0} \\ 
{\theta_1} \\ 
... \\ 
{\theta_n}
\end{bmatrix}
= \\begin{bmatrix}
h(x^{1}) \\
h(x^{2}) \\ 
... \\
h(x^{m})
\end{bmatrix}$$

which can be abbriviated to:

$$h(x) = X \cdot {\theta}^T$$
