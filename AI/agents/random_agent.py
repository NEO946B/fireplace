# coding=utf-8
"""
采取随机策略的agent
"""
import random

from agent import Agent

class RandomAgent(Agent):
    def __init__(self, owner) -> None:
        super().__init__(owner)

    def Play(self):
        while True:
            hero_power = self.owner.hero.power
            if hero_power.is_usable() and random.random() < 0.1:
                if hero_power.requires_target():
                    hero_power.use(target=random.choice(hero_power.targets))
                else:
                    hero_power.use()

            # iterate over our hand and play whatever is playable
            for card in self.owner.hand:
                if card.is_playable() and random.random() < 0.5:
                    target = None
                    if card.must_choose_one:
                        card = random.choice(card.choose_cards)
                    if card.requires_target():
                        target = random.choice(card.targets)
                    print("Playing %r on %r" % (card, target))
                    card.play(target=target)

                    if self.owner.choice:
                        choice = random.choice(self.owner.choice.cards)
                        print("Choosing card %r" % (choice))
                        self.owner.choice.choose(choice)

                    continue

            # Randomly attack with whatever can attack
            for character in self.owner.characters:
                if character.can_attack():
                    character.attack(random.choice(character.targets))
                    
            break