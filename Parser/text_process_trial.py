import os
import json
import re
from collections import defaultdict
from pprint import pprint
	
#curr_dir = 'C:\Users\Hannah\Documents\GitHub\ExpertiseMapper'
curr_dir = 'C:\GitHub\ExpertiseMapper'

def main()  :
        # TODO catch IO errors
        raw = readfile()
        #print json.loads(raw[0][0])["user_id"]
        
        # TODO: Save backup
        # f = open('backup.txt', 'w')
        # f.close()
        
        # Users and skills
        users_and_skills = getAllSkills(raw)
        print users_and_skills
        
        #

# Sort into dictionary of skills        
def getAllSkills(raw) :
    skills = defaultdict(list)
    # d = {'technology': {'importance': 1, 'users': [1 , 2]}, 
    #            'java': {'importance': 3, 'users': [4}}

    #print json.loads(raw[0][0])["user_skill"][0]["skill"]["name"]

    i = 0
    for row in raw :
        try :
            #print json.loads(raw[row][0])["user_skill"]
            for s in json.loads(raw[row][0])["user_skill"]:
                if "skill" in s :
                    skillName = s["skill"]["name"]
                    skills[json.loads(raw[row][0])["user_id"]].append(skillName)
                    #skills[skillName].append(json.loads(raw[row][0])["user_id"])
                    
                    i+=i

                else :
                    pass
        except :
            pass
            
    print "total # of skills: " + str(i)
    return skills

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
        with open(curr_dir + '\Parser\skills500.json', 'r') as source:
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
                    start = parts.find("user_skill")
                    parts = parts[:start+12] + " [" + parts[start+14:]
                    parts = parts[0:len(parts)-2] + "}]}"
                    parts = id + parts

                    data[i].append(parts)
            source.close()
        return data
 
        
main()