#!/usr/bin/env python3

import json
import sys
import pdb



def Gestalting(ClassOne, ClassTwo):
	GestaltD20Class = {
		'Name' : '',
		'HitDice' : [],
		'SkillPointsPerDay' : 0,
		'BaseAttackBonus' : [],
		'Fortitude' : [],
		'Will' : [],
		'Reflex' : [],
		'SpecialAbilities' : [],
		'SpellsPerDay' : {},
		'SpellsKnown' : []
	}
	GestaltD20Class['Name'] = ClassOne['Name'] + '+' + ClassTwo['Name']
	if int(ClassOne['BaseAttackBonus'][4]) > int(ClassTwo['BaseAttackBonus'][4]): GestaltD20Class['BaseAttackBonus']= ClassOne['BaseAttackBonus'] 
	else:  GestaltD20Class['BaseAttackBonus']= ClassTwo['BaseAttackBonus']

	if int(ClassOne['Fortitude'][4]) > int(ClassTwo['Fortitude'][4]): GestaltD20Class['Fortitude']= ClassOne['Fortitude'] 
	else:  GestaltD20Class['Fortitude']= ClassTwo['Fortitude']

	if int(ClassOne['Reflex'][4]) > int(ClassTwo['Reflex'][4]): GestaltD20Class['Reflex']= ClassOne['Reflex'] 
	else:  GestaltD20Class['Reflex']= ClassTwo['Reflex']

	if int(ClassOne['Will'][4]) > int(ClassTwo['Will'][4]): GestaltD20Class['Will']= ClassOne['Will'] 
	else:  GestaltD20Class['Will']= ClassTwo['Will']

	if 'SpellsPerDay' in ClassOne.keys(): GestaltD20Class['SpellsPerDay'][ClassOne['Name']] =  ClassOne['SpellsPerDay']
	if 'SpellsPerDay' in ClassTwo.keys(): GestaltD20Class['SpellsPerDay'][ClassTwo['Name']] =  ClassTwo['SpellsPerDay']

	for level in range(20):
		GestaltD20Class['SpecialAbilities'].append(ClassOne['SpecialAbilities'][level] + ' + ' + ClassTwo['SpecialAbilities'][level])

	newclass = open('GestaltDicts/' + GestaltD20Class['Name'] + '.json','w')
	newclass.write(json.dumps(GestaltD20Class))
	newclass.close()

allclasses = ['alchemist','barbarian','bard','cavalier','cleric','druid','fighter','gunslinger','inquisitor','magus','monk','oracle','paladin','ranger','rogue','shifter','sorcerer','summoner','vigilante','witch','wizard']



ClassCombos = json.loads(open('gestaltcombos.json','r').read())

for combo in ClassCombos:
	#why don't I have druids, gunslingers or inquisitors in my DB?
	if "druid" in combo or "gunslinger" in combo or "inquisitor" in combo or "monk" in combo or "wizard" in combo: continue
	print(combo)
	ClassOne = json.loads(open('jsondicts/' + combo[0] + '.json','r').read())
	ClassTwo = json.loads(open('jsondicts/' + combo[1] + '.json','r').read())
	ClassOne['Name'] = combo[0]
	ClassTwo['Name'] = combo[1]

	#pdb.set_trace()

	Gestalting(ClassOne, ClassTwo)
