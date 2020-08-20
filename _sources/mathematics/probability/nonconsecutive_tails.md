# Non-consecutive Tails


We toss a fair coin $n$ times.
What is the probability that there are no consecutive tails?

````{toggle} Click to reveal answer
**Answer**


If a coin is tossed $n$ times, there are $2^n$ possible combinations of heads/tails.
We now need to count how many of these have no consecutive tails.
Let $f(n)$ be the number of sequences without two consecutive tails.
The base cases are $f(1) = 1$ and $f(2)=3$, which can be seen easily by inspection.
Suppose we have a sequence of length $n$.
This was made either by adding a $H$ to a sequence of length $n-1$, or by adding $HT$ to a sequence of length $n-2$.
We therefore have the recurrence relationship
\begin{align*}
    f(n) = f(n-1) + f(n-1).
\end{align*}
For those familiar with it, this is the *Fibonacci sequence*, $F(n)$, shifted by two terms.
This has closed form solution $F(n) = (\phi_+^n - \phi_-^n)/\sqrt{5}$, where $\phi_\pm = (1 \pm \sqrt{5})/2$.

The probability that no two consecutive tails appear in a sequence of $n$ coin tosses is therefore 
\begin{align*}
    F(n+2)/2^n = (\phi_+^{n+2} - \phi_-^{n+2})/(\sqrt{5} \cdot 2^n).
\end{align*} 


````


**Interviews**

This question has been asked at the following companies:
 
- GSA (Telephone Interview)




