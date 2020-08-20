# Covariance of Two Brownian Motions


Consider two Brownian motions $B_t$ and $B_s$.
Show that $Cov(B_t,B_s) = \min(t,s)$.

````{toggle} Click to reveal answer
**Answer**


To answer this question we need to know a few facts about Brownian motion (BM).
The definition is $B_t \sim N(0,t)$.
The second fact is that two non-overlapping BMs are independent, i.e $B_t$ and $B_s - B_t$ are independent for $s>t$.

Without loss of generality, suppose $s<t$.
Then,
\begin{align*}
    Cov(B_t, B_s) &= E[B_t B_s] \\
    &= E[((B_t-B_s)+B_s)B_s] \\
    &= E[B_s^2] + E[(B_t-B_s)B_s] \\
    &= s 
\end{align*}


````


**Interviews**

This question has been asked at the following companies:
 
- Natwest eFX Desk (Telephone Interview)




