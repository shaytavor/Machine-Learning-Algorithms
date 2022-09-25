# implements two variables linear regression
# Shay Tavor, shay.tavor@gmail.com
import numpy as np
import matplotlib.pyplot as plt

class LinearRegressor:
    def __init__(self, Xs, Ys):
        self.theta = [1.5, 1.5]     # coefficients vector for line y = a0 + a1x
        self.Xs = Xs                # input X vector
        self.Ys = Ys                # true Y results
        self.lr = 0.0001            # learning rate
        self.iterations = 1000      # max allowed iterations

    # calculate the mean squared errors for the regression line
    def mse(self):
        self.y_hat = []

        for x in Xs:
            res = self.theta[0] + x * self.theta[1]
            self.y_hat.append(res)

        # calculate mse
        sumSquares = 0
        for i in range(len(self.y_hat)):
            sumSquares += (self.y_hat[i] - Ys[i]) ** 2

        mse = sumSquares / len(Ys)
        return mse

    # plot the actual points vs. the line y's
    def plot(self):
        plt.plot(self.Xs, self.Ys, color='blue', linestyle='none', marker='o')
        plt.plot(self.Xs, self.y_hat, color = 'black', marker = 'x')
        plt.show()

    # gradient descent algorithm - adjust the coefficients
    def gradientDescent(self):
        # every iteration is one step in the gradient descent
        for i in range(self.iterations):
            # 1. calculate loss function for Xs
            err = self.mse()

            # 2. calculate derivatives of theta
            a0 = a1 = 0
            derT0 = derT1 = 0
            for j in range(len(self.Xs)):
                derT0 += self.theta[0] + self.theta[1] * self.Xs[j] - self.Ys[j]
                derT1 += self.Xs[j] * (self.theta[0] + self.theta[1] * self.Xs[j] - self.Ys[j])

            # 3. adjust theta
            derT0 *= (2 / len(self.Xs))
            derT1 *= (2 / len(self.Xs))

            self.theta[0] = self.theta[0] - self.lr * derT0
            self.theta[1] = self.theta[1] - self.lr * derT1

            print(i, self.theta[0], self.theta[1], err)





#########
# create some inputs
Xs = np.array([7, 8, 6, 10, 7, 11,5, 7, 8, 10])
Ys = np.array([10, 9, 7, 10, 8, 13, 10, 11, 10, 11])

reg = LinearRegressor(Xs, Ys)
reg.gradientDescent()   # fit a line
reg.plot()

