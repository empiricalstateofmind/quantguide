# Precision and Recall


Explain what precision and recall are.
How do they relate to the ROC curve?

````{toggle} Click to reveal answer
**Answer**


There are a number of statistics to examine when assessing model performance:
- **Accuracy** The number of correct classifications.
- **Precision** The number of true positives over all predicted positives.
- **Recall (Sensitivity)** The number of true positives over all actual positives
- **F1-Score** The weighted average of Precision and Recall, \begin{align} \rm  2 \cdot (Recall \cdot Precision) / (Recall + Precision). \end{align}   

The ROC curve is a plot of the false positive rate against the true positive rate.
Ideally we want a low false positive rate and high true positive rate.
If we have a model that we can vary continuously we can see how these rates change.


````




