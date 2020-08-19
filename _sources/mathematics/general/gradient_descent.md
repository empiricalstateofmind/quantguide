# Gradient Descent

```{margin} Metadata
**Tags**: 

**Date Added**: 19/08/2020

**Difficulty**: Easy
```


What is the advantage of a convex loss function when using gradient descent?
Prove that a convex function has at most one minimum.

````{toggle} Click to reveal answer
**Answer**


A convex loss function ensures that a gradient descent algorithm will terminate at the global minimum.

A function $f(x)$ is convex if
\begin{align*}
    \frac{1}{2}\left[f(a)+f(b)\right] > f\left(\frac{1}{2}(a+b)\right).
\end{align*}
This is perhaps easiest to remember in words, or even easier still, a diagram.
If we draw a line between any two points on the curve $f$, then that line will *always* lie above the curve $f$.

The proof of only one minimum is usually done by assuming that two minima exist, and showing that convexity must fail.
This is again quite simple to show in a "proof by diagram.""

````


**Interviews**

This question has been asked at the following companies:
 
- NatWest eFX Desk (1st Interview)




**Links and Further Reading**
 
- ABC  


