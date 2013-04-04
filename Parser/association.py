import os, sys, json, re, orange, Orange
from textProcessing import Parser
import networkx as nx
from pprint import *
from collections import defaultdict

dir = 'C:\\GitHub\\ExpertiseMapper\\Parser\\'
raw = 'skills5000'
filename = 'skills.basket'
output = '5000'

def main() :
    
    # filter out all skills that occur below this threshold
    threshold = 2
    # frequency of association
    sup = 0.003
    
    os.chdir(dir)
	
    fileList = ["skills5000", "skills5000_2", "skills5000_3", "skills5000_4", "skills5000_5", "skills5000_6", "skills5000_7", "skills5000_8", "skills5000_9", "skills5000_10", "skills5000_11", "skills5000_12"]

    for file in fileList :
        skills = Parser(dir, file + ".json")
        populateTable(dir + filename, skills)
'''
    # Apply association rules
    data = orange.ExampleTable(filename)
    itemsets = associationRules(data, sup)

    #printRules(rules)
    
    #generate node data struct with weights
    #generate edge data struct with supp and conf from association rules
    nodes, edges = generateEdges(data, itemsets)
    exportToGML(nodes, edges)
'''

def associationRules(data, sup) :
    rules = Orange.associate.AssociationRulesSparseInducer(support = sup, storeExamples = True, maxItemSets=100000)
    itemsets = rules.get_itemsets(data)
    
    return itemsets
    
def generateNodes(s, t) :
    
    # an element is significant when count is above the threshold
    isSignificant = lambda elm: (elm[1] >= t)
    # apply threshold to list of elements and their counts
    counts = filter(isSignificant,[[i, s.skillsList.count(i)] for i in s.skillsList])
    
    #print pprint(counts)
    #print "number of significant nodes: " + str(len(counts))
    
    return counts
    
def generateEdges(d, r) :
    
    nodes = []
    edges = []
    length = len(d)
    for itemset, tids in r:
        weight = len(tids)/float(length)*1000.0
        #we only want support between 2 nodes
        if len(itemset) == 2 :
            nodes.append(d.domain[itemset[0]].name)
            nodes.append(d.domain[itemset[1]].name)
            edges.append((d.domain[itemset[0]].name, d.domain[itemset[1]].name, {"w": weight}))
        #print "%2.4f %s" % (len(tids)/float(len(d)),
        #" ".join(d.domain[item].name for item in itemset))
    return nodes, edges

def exportToGML(n, e) :
    
    G=nx.Graph()
    
    #for node in n :
        #G.add_node(node[0], frequency=node[1])
        
    G.add_nodes_from(n)
    G.add_edges_from(e)
    print len(G.edges())
    
    graph = nx.generate_gml(G)
    print graph
    
    nx.write_gml(G, dir + output)

def populateTable(dir, s) :
    #save as tab
    with open(dir, 'a') as file:
        for i, key in enumerate(s.userSkills) :
            #u = ', '.join(sum((i.split() for i in s.userSkills[key]), [])) 
            u = ', '.join(s.userSkills[key])
            file.write(u)
            '''
            if (i+1) == len(s.userSkills):
                file.write(u)
            else:
                file.write(u + '\n')
            '''

def printRules(rules) :

    print "%5s   %5s" % ("supp", "conf")
    for r in rules:
        print "%5.3f   %5.3f   %s" % (r.support, r.confidence, r)
        
main()