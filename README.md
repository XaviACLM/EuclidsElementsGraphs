# EuclidsElementsGraphs

A program that scrapes data on the dependency graph of Euler's elements and drawns out this graph (vertically, taking advantage of the fact that it is a partial order).

The code itself might be the worst I've ever written: this is from before I knew anything about software design, and it had to be rushed for a number of reasons. Nonetheless, it's kept here because

a) The results are interesting

b) It's very likely it will be rewritten from the ground up in the future.

The dependency data itself is extracted from David E. Joyce's online version of Euclid's elements, available [here](https://mathcs.clarku.edu/~djoyce/java/elements/elements.html)

Note that Euclid's Elements is (are?) not formal in a modern sense. This shows up in the graph in having multiple definitions that are never used - for instance, it is unclear how "a point is that which has no parts" might come up in proving later propositions. Joyce's webpage provides some valuable insight about this - but not the kind that can be represented by a picture of a graph, so go read it :)

Here is the graph for the first four books, eschewing definitions:

![](/results/euc_firstfour.png?raw=true)

A graph for the first nine is available in the resources folder. It is interesting to note that, following the topic division among Euclid's Elements, there is distinctly little interplay between books 1-4 and books 5-9: Only 7 statements from 1-4 and used in 5-9.

The graph is also a nice tool to find and illustrate important propositions. To test this, I randomly picked a proposition that seemed to be connected to a lot of other statements, and applied some judicious photoshop to get this drawing illustrating the relevance of proposition I47:

![](/results/I47.png?raw?true)

I later realized this was the Pythagorean theorem.
