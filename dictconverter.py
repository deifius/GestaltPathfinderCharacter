#!/usr/bin/env python3

import json 
import sys
import pdb

charclass = list(zip(*json.loads(open('json/'+sys.argv[1]+'.json','r').readline())))

characterdict = {}



if len(charclass[-1][-1]) == 1: 
	characterdict['SpellsPerDay'] = []
	while len(charclass[-1][-1]) == 1: 
		characterdict['SpellsPerDay'].insert(0,charclass.pop(-1))
	characterdict["SpellsPerDay"] = list(zip(*characterdict["SpellsPerDay"]))

characterdict['SpecialAbilities'] = charclass.pop(-1)
characterdict['Will'] = charclass.pop(-1)
characterdict['Reflex'] = charclass.pop(-1)
characterdict['Fortitude'] = charclass.pop(-1)
characterdict['BaseAttackBonus'] = charclass.pop(-1)


dictatedchar = open("jsondicts/"+sys.argv[1]+".json",'w')
dictatedchar.write(json.dumps(characterdict))
dictatedchar.close()
