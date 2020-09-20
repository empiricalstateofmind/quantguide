# Weighing Rocks


Suppose we have $N$ rocks, all different weights.
How can I find the heaviest rock if we can only compare the weights of two rocks at a time?
How about the heaviest and second heaviest?

````{toggle} Click to reveal answer
**Answer**


This question examines both algorithmic analysis and efficient data structures.
While this is related to sorting, we don't require a fully sorted list, so for this question we need to look at the individual steps of a sorting algorithm.

The simplest way to find the heaviest rock is to perform one step of the bubblesort algorithm.
We pick up the first rock and iterate through all the rocks in sequence.
At each weigh we keep hold of the heaviest of the two.
This guarantees that we have the heaviest rock at the end, and it has only taken us $N-1$ comparisons.
This is in fact the best we can achieve.

For the second heaviest, we can perform the same operation on the now reduced number of rocks, taking $N-2$ comparisons.
As you might expect, this isn't the most optimal way.
Instead of iterating through the list, we can run a knockout competition for the rocks.
Suppose we have eight rocks to begin with.
We weigh them in pairs, and then weigh the winners in pairs until we have one left. 
This will be the heaviest.
This has also taken $N-1$ comparisons.
The efficiency saving comes from the binary tree we have constructed along the way.
The second heaviest:

* was beaten in the final comparison (so belongs to another tree)
* was beaten previously by the heaviest at some point

We therefore only need to go down the tree, at each time comparing the rock beaten in the final comparison to all rocks which were beaten by the heaviest. 
This takes $\log_2(N) - 1$ comparisons.

In total this takes $N + \log_2(N) - 2$ comparisons, beating the $2N-3$ if we iterated through the list twice.
Here it is important to notice that, at leading order, both algorithms are $\mathcal{O}(N)$, however the second method is provably faster.


````




