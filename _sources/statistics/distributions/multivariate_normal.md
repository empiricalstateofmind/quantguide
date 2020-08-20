# Multivariate Normal Distribution

```{margin} Metadata
**Tags**: 

**Date Added**: 20/08/2020

**Difficulty**: Easy
```


What is the PDF of the multivariate normal distribution?
Explain what each term means.

````{toggle} Click to reveal answer
**Answer**


Let $\vec{\mu}$ be a $p$-vector, and $\Sigma$ a $p \times p$ symmetric, positive definite matrix, and let $|\Sigma|$ denote the determinant of $\Sigma$.
We say $\vec{X} = (X_1,  X_2, \dots, X_p)$ has a multivariate normal distribution with mean vector $\vec{\mu}$ and covariance matrix $\Sigma$, i.e. $\vec{X} \sim N(\vec{\mu}, \Sigma)$, if it has a PDF
\begin{align*}
    f(\vec{x}) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}}\exp\left[-\frac{1}{2}(\vec{x}-\vec{\mu}^T)\Sigma^{-1}(\vec{x}-\vec{\mu}))\right].
\end{align*}

Some simple results follow:
- $E[X_i] = \mu_i$
- $Var(X_i) = \Sigma_{ii}$ and $Cov(X_i,X_j) = \Sigma_{ij}$
- If $\vec{a}$ is any non-random $p$-vector then $\vec{a}^T\vec{X} \sim N(\vec{a}^T\vec{\mu}, \vec{a}^T\Sigma\vec{a})$
- If $\vec{a} = \vec{e}_j$, where $e_j=1$ and is zero otherwise, we get the marginal distribution of $X_j$.


````




**Links and Further Reading**
 
- [Wikipedia](https://en.wikipedia.org/wiki/Multivariate_normal_distribution)  


