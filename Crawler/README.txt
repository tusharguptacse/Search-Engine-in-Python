Crawlers in Python
-----------------\


I have implemented three crawlers.

1. BFS Crawler- It takes in a seed page, crawls it and adds its links to the frontier. It crawls in BFS order.
		It stops once it reaches 1000 links. In this, the seed was a Wikipedia article about Sustainable Energy.
		A politeness policy with 1 second delay between requests has been used.

2. Focussed BFS Crawler- It takes a seed page, and a focus word. It begins crawling from the seed page in BFS order, and stores in 
			 the frontier those links which have the focus word in it, or those links whose text snippet has the focus word.

3. Focussed DFS Crawler- It takes a seed page, and a focus word. It begins crawling from the seed page in DFS order, and stores in 
			 the frontier those links which have the focus word in it, or those links whose text snippet has the focus word.
