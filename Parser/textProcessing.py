import os
import json
import re
import Orange

from collections import defaultdict
from pprint import pprint

class Parser:
    #curr_dir = 'C:\Users\Hannah\Documents\GitHub\ExpertiseMapper'
    curr_dir = 'C:\GitHub\ExpertiseMapper'

    def __init__()  :
        # TODO catch IO errors
        self.raw = readfile()
        
        # Users and skills
        self.userSkills = getAllSkills(raw)
        # print users_and_skills

    # Sort into dictionary of skills        
    def getAllSkills(raw) :
        skills = defaultdict(list)
        num_parsed = 0
        # d = {'technology': {'importance': 1, 'users': [1 , 2]}, 
        #            'java': {'importance': 3, 'users': [4}}

        #print json.loads(raw[0][0])["user_skill"][0]["skill"]["name"]

        for row in raw :
            try :
                #print json.loads(raw[row][0])["user_skill"]
                for s in json.loads(raw[row][0])["user_skill"]:
                    if "skill" in s :
                    
                        skillName = s["skill"]["name"]
                        skills[json.loads(raw[row][0])["user_id"]].append(skillName)
                        
                        num_parsed += 1
                    else :
                        pass
            except :
                # print raw[row][0]
                pass
        print "total skills: " + str(num_parsed)
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
            num_rows = 0
            
            # Validate 
            with open(curr_dir + '\Parser\skills.json', 'r') as source:
                for line in source:
                    if line.find(user) != -1:
                        #get user id
                        id = "{" + line
                    elif line.find(skill) != -1:
                        parts = line.replace("\\", "")
                        start = parts.find("user_skill")
                        parts = parts[:start+12] + " [" + parts[start+14:]
                        
                        # Make this smarter
                        # parts.rfind("\"")
                        # replace whatever after with "}}]}"
                        # Some need }]}
                        indx = parts.rfind('}')
                        parts = parts[0:indx] + "}]}"
                        parts = id + parts
                        data[num_rows ].append(parts)
                        num_rows += 1
                source.close()
            print "total valid entries: " + str(num_rows)
            return data