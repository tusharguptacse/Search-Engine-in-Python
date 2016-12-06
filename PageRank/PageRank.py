import operator
from collections import Counter
import math
import operator
import sys

def initialize_variables():
    global inlinks
    inlinks={}
    global outlinks
    outlinks={}
    global sinklinks
    sinklinks=[]
    global rankinglist
    rankinglist={}
    global newrankinglist
    newrankinglist={}
    global pages
    pages=[]
    global sorted_inlinks
    sorted_inlinks={}
    global d
    d=0.85
    global total_links
    total_links=0


def algorithm_of_page_rank():
    flag=1  
    oldp=0.0  
    chk=0

    while chk < 4:
    	e=0
    	p=0
        spr=0
        for itm in sinklinks:
            spr=spr+rankinglist[itm]
        for itm in pages:
            newrankinglist[itm]=(1-d)/total_links
            newrankinglist[itm]=newrankinglist[itm]+d*(spr/total_links)
            if itm not in inlinks:
                continue
            for in_link in inlinks[itm]:
                newrankinglist[itm]=newrankinglist[itm]+d*(rankinglist[in_link]/outlinks[in_link])
        for link in pages:
            rankinglist[link]=newrankinglist[link]
    	for link in pages:
            pr=rankinglist[link]
            e=e+pr*math.log(1/pr,2)
    	newp=math.pow(2,e)

  
        if ((abs(oldp - newp))<1):
            chk=chk+1
        else:
            chk=0
        oldp=newp
        


if __name__=='__main__':


    file="graph.txt"

    initialize_variables()

    f=open(file,'r')
    line=f.readline()
    while line:
        links=line.split()   
        if links[0] not in outlinks:
            outlinks[links[0]]=0
        for link in links[1:]:
            if link not in outlinks:
                outlinks[link]=1
            else:
                outlinks[link]=outlinks[link]+1
        inlinks[links[0]]=links[1:]
        pages=pages+links
        line=f.readline()  
    pages=set(pages)
    counter=0
    for itm in inlinks:
    	if (len(inlinks[itm])==0):
    	    counter=counter+1
    print counter
    outlist={}
    #sorted_inlinks = sorted(inlinks.items(), key=operator.itemgetter(1), reverse=True)
    for page in inlinks:
        outlist[page]=len(inlinks[page])

    sorted_inlinks=sorted(outlist.items(),key=operator.itemgetter(1),reverse=True)
    print sorted_inlinks[0][0],sorted_inlinks[0][1]
    print sorted_inlinks[1][0],sorted_inlinks[1][1]
    print sorted_inlinks[2][0],sorted_inlinks[2][1]
    print sorted_inlinks[3][0],sorted_inlinks[3][1]
    print sorted_inlinks[4][0],sorted_inlinks[4][1]
    f=open('outlinks_rank_files.txt', 'w+')
    for item in outlinks:
        f.write(item+' '+str(outlinks[item])+'\n')
    
    total_links=len(pages)
    probability_of_each_link=1.0/total_links
    for link in pages:
        rankinglist[link]=probability_of_each_link
    for page in outlinks:
        if outlinks[page]==0:   
            sinklinks.append(page) 
    f=open('page_rank_sink_nodes2.txt', 'w+')
    for item in sinklinks:
        f.write(item + "\n")     
    print (len(sinklinks))

    algorithm_of_page_rank()

    output_list=[]
    sorted_rankinglist=sorted(rankinglist.items(),key=operator.itemgetter(1),reverse=True)
    count=1 
    for page in sorted_rankinglist:
        output_list.append(str(count) + ' ' + str(page[0]) + ' ' + str(page[1]) + '\n')
        count += 1
    
    f=open('page_rank_files.txt','w+')
    for item in output_list:
        f.write(item)
