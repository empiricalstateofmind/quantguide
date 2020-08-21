# Bias-Variance Tradeoff


What is the variance-bias trade-off?

````{toggle} Click to reveal answer
**Answer**


Suppose we have a statistical estimator $T$ (for example of the population mean of a set of random variables $X_i$).
Let the true value of the mean be $\mu$ and let $E[T] = \theta$.

The mean-squared error of our estimator is given by $MSE(T) = E[(T-\mu)^2]$.
The bias of our estimator is $b(T) = E[T] - \mu = \theta - \mu$.
Rewritting our expression for the MSE we get
\begin{align*}
    MSE(T) &= E[\{ (T-\theta) + (\theta - \mu)\}^2] \\\\\\\\
    &= E[ (T-\theta)^2 + 2(T-\theta)(\theta - \mu) + (\theta - \mu)^2] \\\\\\\\
    &= E[(T-\theta)^2] + 2(\theta - \mu) \cdot 0 + b(T)^2 \\\\\\\\
    &= Var(T) + b(T)^2.
\end{align*}
This shows us that if we want to minimise the error on our estimator then this is not necessarily achieved with an unbiased estimator if it has high variance. 
We might want to access a slight bias in the estimator if our estimator has low variance.

The same logic applies to more general models where we have a prediction based on data, such a regression.
For a model $\hat{y}_i = f(x_i)$ our MSE (ignoring normalisation) is $\sum_i \hat{y}_i - y_i$, were $y_i$ are the true values.
We make a trade off between our model variance, and the bias in the model. 


````




