import os
import json
import re
from collections import defaultdict
from pprint import pprint
	
curr_dir = 'C:\Users\Hannah\Documents\GitHub\ExpertiseMapper'
#curr_dir = 'C:\GitHub\ExpertiseMapper'

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
    
    print raw[0]
    #print json.loads(raw[0][0])["user_skill"][0]["skill"]["name"]

    i = 0
    for row in raw :
        try :
            print json.loads(raw[row][0])["user_skill"]
            for s in json.loads(raw[row][0])["user_skill"] :
                if (s.find("{") == null) :
                    pass
                else :
                    print s["skill"]["name"]
                    i = i + 1
        except :
            pass
            
    print i
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
        with open(curr_dir + '\Parser\skills_500.json', 'r') as source:
            for line in source:
                i = i + 1
                if line.find(user) != -1:
                    #get user id
                    id = "{" + line
                elif line.find(skill) != -1:
                    #Clean up escapes
                    #Replace "" with []s
                    # print line
                    parts = line.replace("\\", "")
                    start =  parts.find("user_skill")
                    parts = parts[:start+12] + " [" + parts[start+14:]
                    parts = parts[0:len(parts)-2] + "}]}"
                    parts = id + parts

                    data[i].append(parts)
            source.close()
        return data
 
        
main()