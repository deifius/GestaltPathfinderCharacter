#!/usr/bin/env python3

class CharacterClass():
	def __init__(self, name, hitDice, skillPoints, classSkill, baseAttackBonus, fortitude, reflex, will, spellsPerDay, spellsKnown, specialAbilities, ):
		self.name = name
		self.hitDice = hitDice
		self.skillPoints = skillPoints
		self.classSkill = classSkill
		self.baseAttackBonus = baseAttackBonus
		self.fortitude = fortitude
		self.reflex = reflex
		self.will = will
		self.spellsPerDay = spellsPerDay
		self.spellsKnown = spellsKnown
		self.specialAbilities = specialAbilities
		
class GestaltCharacter(CharacterClass):
	def __init__(self, characterClassOne, characterClassOther):
		self.characterClassOne = characterClassOne
		self.characterClassOther = characterClassOther
		self.gestaltName = characterClassOne.name + characterClassOther.name
		self.gestaltHitDice = max(characterClassOne.hitDice, characterClassOther.hitDice)
		self.gestaltSkillPoints = max(characterClassOne.skillPoints, characterClassOther.skillPoints)
		self.gestaltClassSkill = list(set(characterClassOne.classSkill + characterClassOther.classSkill))
		self.gestaltBaseAttackBonus = max(characterClassOne.baseAttackBonus, characterClassOther.baseAttackBonus)
		self.gestaltFortitude = max(characterClassOne.fortitude, characterClassOther.fortitude)
		self.gestaltWill = max(characterClassOne.will, characterClassOther.will)
		self.gestaltSpellsPerDay = # a dict keeping the spell lists seperate
		self.gestaltSpellKnown = # a dict keeping the spell lists seperate
		self.gestaltSpecialAbilities = # colated 
		
		
