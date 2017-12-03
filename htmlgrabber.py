#!/usr/bin/env python3

classesd20 = ['cleric','bard','barbarian','druid','fighter',
'monk','paladin','ranger','rogue','sorcerer','wizard']

urldir = 'http://www.d20pfsrd.com/classes/core-classes/'


this = open('wgetsforsh','w')

for classd20 in classesd20:
	this.write('wget ' + urldir + classd20 +'; mv index.html classesinhtml/' + classd20 + '.html;\n')

this.close()


classesd20 = ['shifter','gunslinger','inquisitor','alchemist','cavalier',
'magus','oracle','summoner','vigilante','witch']

urldir = 'http://www.d20pfsrd.com/classes/base-classes/'


this = open('wgetsforsh','a')

for classd20 in classesd20:
	this.write('wget ' + urldir + classd20 +'; mv index.html classesinhtml/' + classd20 + '.html;\n')

this.close()