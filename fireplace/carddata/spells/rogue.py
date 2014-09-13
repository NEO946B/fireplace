from ..card import *


# Backstab
class CS2_072(Card):
	action = damageTarget(2)


# Cold Blood
class CS2_073(Card):
	action = buffTarget("CS2_073e2")
	combo = buffTarget("CS2_073e")


# Deadly Poison
class CS2_074(Card):
	def action(self):
		self.controller.hero.weapon.buff("CS2_074e")

class CS2_074e(Card):
	atk = 2


# Sinister Strike
class CS2_075(Card):
	def action(self):
		self.controller.opponent.damage(3)


# Assassinate
class CS2_076(Card):
	def action(self, target):
		target.destroy()


# Sprint
class CS2_077(Card):
	action = drawCards(4)


# Blade Flurry
class CS2_233(Card):
	def action(self):
		damage = self.controller.hero.weapon.atk
		self.controller.hero.weapon.destroy()
		for target in self.controller.opponent.field:
			target.damage(damage)


# Eviscerate
class EX1_124(Card):
	action = damageTarget(2)
	combo = damageTarget(4)


# Fan of Knives
class EX1_129(Card):
	def action(self):
		for target in self.controller.opponent.field:
			target.damage(1)
		self.controller.draw()


# Shiv
class EX1_278(Card):
	def action(self, target):
		target.damage(1)
		self.controller.draw()


# Sap
class EX1_581(Card):
	action = bounceTarget


# Vanish
class NEW1_004(Card):
	def action(self):
		for target in self.controller.getTargets(TARGET_ALL_MINIONS):
			target.bounce()
