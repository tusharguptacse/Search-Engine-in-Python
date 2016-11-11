from collections import deque
from bs4 import BeautifulSoup
from urlparse import urljoin
import sys
import urllib2
import time


thefile = open('Task2A-URL.txt', 'w')
#create queue
queue = deque([])

counterbetter = 0

depth = 0

#maintain list of visited pages
visited_list = []

# Crawl the page and populate the queue with newly found URLs
def crawl(url, focus_word):
    while depth > 5:
        return
    visited_list.append(url)
    if len(queue) > 999:
        return
    urls = []
    urlf = urllib2.urlopen(url)
    soup = BeautifulSoup(urlf.read(), 'html.parser')
    for item in soup.find_all('a'):
        link = item.get('href')
        if link is not None:
            if ':' not in link and '#' not in link and 'Main_Page' not in link and link.find('/wiki/') == 0:
                var1 = item.text.lower()
                var2 = link.lower()
                if var1.find('solar') != -1 or var2.find('solar') != -1:
                    urls.append(link)

    for i in urls:
        flag = 0
        complete_url = ('https://en.wikipedia.org' + i)
        

        #check if it exists already in queue
        for j in queue:
            if j == complete_url:
                flag = 1
                break

        #if not in queue
        if flag == 0:
            if len(queue) > 999:
                return
            if (visited_list.count(complete_url)) == 0:
                queue.append(complete_url)

    # Pop one URL from the queue from the left side so that it can be crawled
    current = queue.popleft()
    # Recursive call to crawl until the queue is populated with 100 URLs
    time.sleep(1)
    crawl(current, focus_word)

crawl('https://en.wikipedia.org/wiki/Solar_power', 'solar')

# Print queue
for i in queue:
    counterbetter+=1
    print i

for it in queue:
    thefile.write("%s\n" % it)

# counter = 1
# for its in queue:
#     file1 = open(str(counter) + '.txt', 'w')  
#     urlf = urllib2.urlopen(its)
#     soup = BeautifulSoup(urlf.read(), 'html.parser')
#     file1.write(str(soup))

print
print
print
print "                 Pages crawled:                "
print "==============================================="
print

# Print list of visited pages
for i in visited_list:
    print i

print "Total Count of Links Found:" , counterbetter










                
