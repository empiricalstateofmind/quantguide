# The Mystery Box

To make this question easier, it is useful to rescale everything to between zero and one, so that we know $T \sim \text{Unif}(0,1)$.
We want to work out the expected return from a guess $B$.
From the problem we have two things that happen, our bid is rejected and we win nothing, or our bid is accepted.
 
Without any prior information on the box we can easily calculate the expectation $E(T)=0.5$.
If our bid is accepted, we now know something else about the box, namely that $T<\frac{3}{2}B$.
In this case we now now that $(T|\text{Accepted}) \sim \text{Unif}(0,\frac{3}{2}B)$, which has expectation $\frac{3}{4}B$.
In this case our expected payoff is $P = \frac{3}{4}B - B = -\frac{1}{4}B$.
Clearly this is negative for any choice of $B$, and so our optimal choice is $B=0$.
Since we have a choice between a negative payoff and zero, we do not need to factor in the probabilities of acceptance.

Note, this question is sometimes equally phrased as ``acceptance if $B$ is greater than $T$, however the payoff is $1.5T$.''
You can repeat the exercise above to see they are equivalent.

{doc}`See Question <mystery_box_que>`