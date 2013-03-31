import os
import json
import re
from collections import defaultdict
from pprint import pprint
	
curr_dir = 'C:\Users\Hannah\Documents\GitHub\ExpertiseMapper'

def main()  :
        # TODO catch IO errors
        raw = readfile()
        #print json.loads(raw[0][0])["user_id"]
        
        # TODO: Save backup
        # f = open('backup.txt', 'w')
        # f.close()
        
        # Build skills repository
        allSkills = getAllSkills(raw)

# Sort into dictionary of skills        
def getAllSkills(raw) :
    data = {}
    # d = {'technology': {'importance': 1, 'users': [1 , 2]}, 
    #            'java': {'importance': 3, 'users': [4}}
    
    return data

# Parse JSON file
def readfile() :
        # ----------- SQL Query to list skills from each user --------------
        # SELECT `user_id`, GROUP_CONCAT(DISTINCT source_json ORDER BY source_json DESC SEPARATOR ', ')
        # FROM main_skill
        # GROUP BY `user_id`
        # ------------------------------------------------------------------
        data = defaultdict(list)
        user = "user_id"
        skill = "user_skill"
        i = 0
        
        # Validate 
        with open(curr_dir + '\Parser\main_skill50.json', 'r') as source:
            for line in source:
                if line.find(user) != -1:
                    #get user id
                    id = "{" + line
                elif line.find(skill) != -1:
                    #Clean up escapes
                    #Replace "" with []s
                    parts = line.replace("\\", "")
                    parts = parts[0:14] + " [" + parts[16:]
                    parts = parts[0:len(parts)-2] + "}]}"
                    parts = id + parts
                    #print parts
                    data[i].append(parts)
                    i = i + 1
            source.close()
        
        return data
 
        
main()