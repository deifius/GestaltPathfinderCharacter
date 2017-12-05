#!/usr/bin/env python3

import json


d20classes = ['alchemist','barbarian','bard','cavalier','cleric','druid','fighter','gunslinger','inquisitor','magus','monk','oracle','paladin','ranger','rogue','shifter','sorcerer','summoner','vigilante','witch','wizard']

ClassDictJson = {}

for each in d20classes:
	ClassDictJson[each] = json.loads(open("json/" + each + ".json",'r').readline())

class GestaltD20Class:
	HitDice = []
	BaseAttackBonus = []
	Saves = {'fortitude':[],'will':[],'reflex':[]}
	SpecialAbilities = []
	SpellsPerDay = []
	SpellsKnown = []

def Gestalting(ClassOne, ClassTwo):
	GestaltD20Class.
	return GestaltD20Class
