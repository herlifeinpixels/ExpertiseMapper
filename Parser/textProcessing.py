import os, json, re

from collections import defaultdict
#curr_dir = 'C:\Users\Hannah\Documents\GitHub\ExpertiseMapper'
#curr_dir = 'C:\GitHub\ExpertiseMapper'

class Parser:

    def __init__(self, dir, raw)  :

        self.dir = dir
        self.raw = raw
        self.raw = self.readfile(self.dir, self.raw)
        
        # Users and skills
        self.userSkills, self.skillsList = self.getAllSkills(self.raw)

    # Sort into dictionary of skills        
    def getAllSkills(self, rdata) :
        skills = defaultdict(list)
        skillsList = []
        num_parsed = 0

        #print json.loads(rdata[0][0])["user_skill"][0]["skill"]["name"]
        for row in rdata :
            try :
                #print json.loads(raw[row][0])["user_skill"]
                for s in json.loads(rdata[row][0])["user_skill"]:
                    if "skill" in s :
                    
                        skillName = s["skill"]["name"]
                        # Add to dictionary
                        skills[json.loads(rdata[row][0])["user_id"]].append(skillName)
                        
                        # Add to list
                        skillsList.append(skillName)
                        num_parsed += 1
                    else :
                        pass
            except :
                pass
        print "total skills: " + str(num_parsed)
        return skills, skillsList
        
    # Extract duplicates
    def getDuplicates(self) :
        copy = self.skillsList[:]
        for value in set(copy):
            copy.remove(value)
        return copy

    # Parse JSON file
    def readfile(self, dir, raw) :
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
            with open(dir + '\\' + raw, 'r') as source:
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
                        data[num_rows].append(parts)
                        num_rows += 1
                source.close()
            print "total valid entries: " + str(num_rows)
            return data