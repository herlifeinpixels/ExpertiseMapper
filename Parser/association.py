import os, sys, json, re, orange, Orange
from textProcessing import Parser
import networkx as nx
from pprint import *
from collections import defaultdict

def main() :

    dir = 'C:\\GitHub\\ExpertiseMapper\\Parser\\'
    raw = 'skills500.json'
    filename = 'skillTab.basket'
    
    # filter out all skills that occur below this threshold
    threshold = 3
    # frequency of association
    sup = 0.015
    
    os.chdir(dir)
    skills = Parser(dir, raw)
    
    #populateTable(dir + filename, skills)
    data = orange.ExampleTable(filename)
    
    # Apply association rules
    rules = orange.AssociationRulesSparseInducer(data, support = sup)
    
    #printRules(rules)
    
    #generate node data struct with weights
    nodes = generateNodes(skills, threshold)
    #generate edge data struct with supp and conf from association rules
    #generateEdges(skills, rules)
    exportToGML(nodes)
    
def generateNodes(s, t) :
    
    # an element is significant when count is above the threshold
    isSignificant = lambda elm: (elm[1] >= t)
    # apply threshold to list of elements and their counts
    counts = filter(isSignificant,[[i, s.skillsList.count(i)] for i in s.skillsList])
    
    #print pprint(counts)
    #print "number of significant nodes: " + str(len(counts))
    
    return counts

def exportToGML(n) :
    
    G=nx.Graph()
    
    for node in n :
        G.add_node(node[0], frequency=node[1])
    print G.nodes()

def populateTable(dir, s) :
    #save as tab
    with open(dir, 'a') as file:
        
        for i, key in enumerate(s.userSkills) :
            #u = ', '.join(sum((i.split() for i in s.userSkills[key]), [])) 
            u = ', '.join(s.userSkills[key])
            if (i+1) == len(s.userSkills):
                file.write(u)
            else:
                file.write(u + '\n')

def printRules(rules) :

    print "%5s   %5s" % ("supp", "conf")
    for r in rules:
        print "%5.3f   %5.3f   %s" % (r.support, r.confidence, r)
        
main()