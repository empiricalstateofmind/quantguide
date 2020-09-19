# Measuring Heights of People


Suppose we are on the street, measuring the heights of individuals as they pass by.
We measure the height of the first person that we see and record it as $h_1$.
What is the expected number of people that we need to measure subsequently until we see someone taller?
Discuss how you would go about this and state any assumptions you make.

Suppose that human heights are distributed uniformly on $[0,1]$.
What is your answer now? Does this make sense?

````{toggle} Click to reveal answer
**Answer**


This is a nice question since it tests not only basic probability, but also how one might approach a modelling question.
If we were to model the problem properly, we might want to consider a bimodal distribution (say a composition of two normals) to reflect the differences between men and women's heights.
A simpler case would be just to consider heights to be normally distributed.

Let $N$ be the number of people we need to measure before we find someone with a height greater than $h_1$.
We can find the expectation by conditioning over all possible heights $h_1$, finding the probability that $h>h_1$, and noting that $N$ is geometrically distributed.
This gives
\begin{align*}
E[N] = \int_{h_1=0}^\infty \frac{1}{P(h > h_1)} dh_1, 
\end{align*}
where we have used the fact that the expectation of a geometric distribution with success rate $p$ is $1/p$.
We can calculate this for a normal distribution, but as the question hints, we look at the uniform distribution for simplicity.

In this case we get
\begin{align*}
E[N] = \int_{h_1=0}^1 \frac{1}{1-h_1} dh_1. 
\end{align*}
Integrating we get 
\begin{align*}
E[N] = \left[ -\log(1-h_1) \right]_0^1. 
\end{align*}
We arrive at a problem - our expectation is infinite.
Our maths is correct, however our modelling assumption has lead to a poor conclusion.
The issue arises since extreme values of $h_1$ are likely ($h_1=0.99999$ is equally likely as $h_1=0.5$, for example).
However, the expected number of trials until success grows like $1/(1-h_1)$ which is much faster.
If we used a Gaussian distribution instead, the probability of extreme values decays exponentially and so we end up with a finite variance.


````


**Interviews**

This question has been asked at the following companies:
 
- HRT (Telephone Interview)




