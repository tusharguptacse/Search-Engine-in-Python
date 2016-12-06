PageRank Implementation

In this, I implemented the PageRank Algorithm on two graphs.

Graph-1 is a crawl of 1000 pages from wikipedia starting with Sustainable Energy.
Graph-2 is the WT2g collection which is a 2GB crawl of a subset of the web,
containing 183,811 web documents. It is already cleaned.


Pseudocode of the PageRank implemented-

// P is the set of all pages; 
|P| = N // S is the set of sink nodes, i.e., pages that have no out links 
// M(p) is the set (without duplicates) of pages that link to page p
// L(q) is the number of out-links (without duplicates) from page q 
// d is the PageRank damping/teleportation factor;  use d = 0.85 as a fairly typical value 

foreach page p in P 
	PR(p) = 1/N	 				/* initial value */ 
while PageRank has not converged do 
	sinkPR = 0 
	foreach page p in S 				/* calculate total sink PR */ 
		sinkPR += PR(p) 
	foreach page p in P 
		newPR(p) = (1-d)/N 			/* teleportation */ 
		newPR(p) += d*sinkPR/N 			/* spread remaining sink PR evenly */ 
		foreach page q in M(p) 			/* pages pointing to p */ 
			newPR(p) += d*PR(q)/L(q) 	/* add share of PageRank from in-links */ 
	foreach page p 
		PR(p) = newPR(p) 
Return and output final PR score.

The code was run until the PageRank values converged.
To test for convergence, I calculated the "perplexity" of the PageRank distribution,
where perplexity is simple 2 raised to the (Shannon) entropy of the distribution, i.e., 
2^H (PR)

Perplexity is a measure of how "skewed" a distribution is:
Perplexity is a measure of how "skewed" a distribution is: the more "skewed" 
(i.e., less uniform) a distribution is, the lower its perplexity. Informally, you can think 
of perplexity as measuring the number of elements that have a "reasonably large" probability 
weight; technically, the perplexity of a distribution with entropy h is the number of 
elements n such that a uniform distribution over n elements would also have entropy h. 
(Hence, both distributions would be equally "unpredictable"). PageRank can be considered as 
converged if the change in perplexity is less than 1 for at least four consecutive iterations.	
