import os
import json
import re
from pprint import pprint
 
# number, "user_skill" : "
#  			{"prof" : {*}, "skill" : {*, "years": {*}},
#				{"prof" : {*}, "skill" : {*, "years": {*}},
#				{"prof" : {*}, "skill" : {*, "years": {*}"
 
# we want:
	
 
def main():
        # TODO catch IO errors
        raw = readfile()
        f = open('Failed.txt', 'w')
        json.dumps(raw, f)
        f.close()
        print raw;
        print "";
        
def readfile() :
        # ----------- SQL Query to list skills from each user --------------
        # SELECT `user_id`, GROUP_CONCAT(DISTINCT source_json ORDER BY source_json DESC SEPARATOR ', ')
        # FROM main_skill
        # GROUP BY `user_id`
        # ------------------------------------------------------------------
        data = []
        user = "user_id"
        skill = "user_skill"
        curr_dir = 'C:\GitHub\ExpertiseMapper'
        
        with open(curr_dir + '\Parser\main_skill50.json', 'r') as source:
                for line in source:
                        if line.find(user) != -1:
                                #get user id
                                id = line.rpartition(':')[2]
                                print id 
                        elif line.find(skill) != -1:
                                # we get line with user skills
                                # we want {'skill': 'Adobe', 'proficiency': 'beginner'}
                                parts = line.split();
                                parts = line.replace("\\", "")
                                print parts
                source.close()
        
        return data
 
        
main()