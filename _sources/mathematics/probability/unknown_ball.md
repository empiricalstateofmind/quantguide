# The Unknown Ball


We have a single bag, with a single ball in it.
This ball is either red or green with equal probability.
I add a green ball to the bag, and pick out a ball at random.
What is the probability that the remaining ball is green, given I pick out a green ball?

````{toggle} Click to reveal answer
**Answer**


In problems such as this where there is a small probability space it is often easiest to enumerate them and work out probabilities by counting.
In this case we have only two options, GG or RG.
When picking out a green, we have three choices (two from the first case, and one from the second).
In the first two cases the remaining ball is green, and in the last the remaining ball is red.
This immediately gives $\Pr(\text{Remaining=G}|\text{Picked=G}) = 2/3$.

Using Bayes' Theorem, we can write
\begin{align*}
    \Pr(\text{Original=G}|\text{Picked=G}) &= \frac{\Pr(\text{Picked=G}|\text{Original=G}) \Pr(\text{Original=G})}{\Pr(\text{Picked=G})} \\
    &= \frac{1 \cdot 1/2}{(1\cdot\frac{1}{2} + \frac{1}{2}\cdot\frac{1}{2})} \\
    &= 2/3,
\end{align*}
which equally probable.


````




