# Required Sample Size


You want to run an opinion poll (for an election) which has two possibilities (Party A and Party B). 
How many people do you need to query to get an error of $\pm x\%$?
To clarity this is $\Pr(\hat{p} - x/100 < p < \hat{p} + x/100)$, and not $\Pr(\hat{p}(100-x)/100 < p < \hat{p}(100+x)/100)$.

````{toggle} Click to reveal answer
**Answer**


Let $X_1, X_2, \dots, X_n$ be a random sample from the $Bernoulli(p)$ distribution, i.e., $\Pr(X_i=1)=p$ and $\Pr(X_i=0)=1-p$.
The maximum likelihood estimate of $p$ is $\bar{X}$.
We also know $E[X_i]=p$ and $Var{X_i} = p(1-p) = \sigma^2(p)$.

For large $n$, by the central limit theorem
\begin{align*}
    \frac{\bar{X}-p}{\sigma(p)/\sqrt{n}} \approx N(0,1),
\end{align*}
and so
\begin{align*}
    \Pr(\hat{p} - x < p < \hat{p} + x) &= \Pr\left( \frac{-x}{\sigma(p)/\sqrt{n}} < \frac{p-\hat{p}}{\sigma(p)/\sqrt{n}} < \frac{x}{\sigma(p)/\sqrt{n}} \right) \\
    &\approx \Phi\left(\frac{x}{\sigma(p)/\sqrt{n}}\right) - \Phi\left(\frac{-x}{\sigma(p)/\sqrt{n}}\right) \\
    &\ge \Phi(x\sqrt{4n}) - \Phi(x\sqrt{4n}).  
\end{align*}
The last line appears from the fact that $\sigma^2(p) = p(1-p) \le 1/4$ (as $p(1-p)$ is maximised for $p=1/2$).
For the probability to be at least $0.95$ we require $x\sqrt{4n} \ge 1.96$, or $n \ge (1.96/2x)^2$.
For $x=0.03$ ($3\%$ error), this require $n \ge 1067$ people.

More generally, the variance of $\bar{X}$ scales like $1/n$, and so the standard deviation scales like $1/\sqrt{n}$. 
As a consequence, if we wanted to halve the standard deviation, we would need to have four times more data.


````




