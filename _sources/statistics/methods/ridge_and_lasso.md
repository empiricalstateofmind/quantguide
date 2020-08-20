# Ridge and Lasso Regression

```{margin} Metadata
**Tags**: 

**Date Added**: 20/08/2020

**Difficulty**: Easy
```


What is the difference between lasso and ridge regression, i.e. the difference between the L1- and L2-norm?
Why does the L1-norm specifically produce zero (or extremely small coefficients)?

````{toggle} Click to reveal answer
**Answer**


The lasso regression uses the L1-norm as a coefficient penalty, whereas ridge regression uses the L2-norm as a coefficient penalty.
Specifically the loss functions are:
\begin{align*}
    L_{\rm Ridge} &= (y - X \beta)^T(y - X \beta) - \beta^T\beta, \\
    L_{\rm Lasso} &= (y - X \beta)^T(y - X \beta) - |\beta|.
\end{align*}
Alternatively we can write these elementwise as
\begin{align*}
    L_{\rm Ridge} &= \sum_{i}(y_i - \sum_j X_{ij} \beta_i)^2 - \lambda \sum_i \beta_i^2, \\
    L_{\rm Lasso} &= \sum_{i}(y_i - \sum_j X_{ij} \beta_i)^2 - \lambda \sum_i |\beta_i|.
\end{align*}

The second question aims to test whether you know the consequences of these penalties.
There is a geometric explanation, and an algebraic one, with the geometric explanation perhaps easier to understand. 
The region formed by the region $|\beta| < t$, introduces corners to the constraint, whereas $\beta^T\beta < t$ is smooth.
If the optimisation hits one of these corners, then the corresponding coefficient in that axis is zero.
As we increase the number of covariates we have a multidimensional diamond which has an increasing number of corners, and so it is likely that the solution lies near a corner.

Algebraically, we can consider the loss function for some $\beta > 0$, where $|\beta| = \beta$.
When $\beta$ crosses $\beta=0$ we can look at the derivative of the loss function with respect to $\beta$ we can show that moving away from $\beta=0$ in the negative direction increases our loss, i.e. moving away from the solution.
This is not the case when we use the quadratic penalty of ridge regression.


````




