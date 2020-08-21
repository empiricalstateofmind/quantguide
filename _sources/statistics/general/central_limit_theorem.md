# The Central Limit Theorem


What is the central limit theorem and why is it important?

````{toggle} Click to reveal answer
**Answer**


Let $X_1, X_2, \dots, X_n$ be i.i.d. from *any* distribution with mean $\mu$ and variance $\sigma^2 \in (0,\infty)$. Then, for all $x$,
\begin{align*}
    \Pr\left(\frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \le x \right) \to \Phi(x) \quad \text{as } n \to \infty.
\end{align*}
This means that the random variable $\frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \approx N(0,1)$, regardless of the distribution of $X_i$.

- The Weak Law of Large Numbers tells us that the distribution of $\bar{X}$ centers around $\mu$ as $n$ becomes large.
- The CLT states that fluctuations of $\bar{X}$ around $\mu$ are of order $1/\sqrt{n}$.
- The CLT states that the distribution of these fluctuations is normal.

Why is this important? 
This powerful result shows that if we collect enough samples, the distribution of our statistics will be well behaved and follow a Gaussian distribution.
This means that we can address many questions about our statistics very simply, e.g. find confidence intervals.
This result does not however provide any intuition on how fast we converge to a normal distribution as the number of samples increases.


````




**Links and Further Reading**
 
- [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)  


