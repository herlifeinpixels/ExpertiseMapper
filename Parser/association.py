import os, json, re, orange, Orange
from textProcessing import Parser

from collections import defaultdict

def main() :

    dir = 'C:\\GitHub\\ExpertiseMapper\\Parser\\'
    raw = 'skills500.json'
    filename = 'skillTab.basket'
    
    # filter out all skills that occur below this threshold
    threshold = 2
    # frequency of association
    sup = 0.015
    
    os.chdir(dir)
    skills = Parser(dir, raw)
    
    #populateTable(dir + filename, skills)
    data = orange.ExampleTable(filename)
    
    # Apply association rules
    rules = orange.AssociationRulesSparseInducer(data, support = sup)
    
    #printRules(rules)
    
    #populate the graph with nodes
    generateNodes(skills, threshold)
    #makes weighted edges between
    #generateEdges(skills, rules)
    
def generateNodes(s, t) :
    #seperate get at the duplicate nodes
    
    dups = s.getDuplicates()
    print "number of significant skills: " + str(len(dups))

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