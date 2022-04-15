# coding=utf-8
import random
from fireplace.utils import random_draft, CardClass
from fireplace.exceptions import GameOver
from AI.agents.random_agent import RandomAgent

def CreateGame():
    from fireplace.game import Game
    from fireplace.player import Player

    deck1 = random_draft(CardClass.MAGE)
    deck2 = random_draft(CardClass.WARRIOR)
    # TODO: 给player增加agent or brain
    player1 = Player("Player1", deck1, CardClass.MAGE.default_hero)
    agent1 = RandomAgent(player1)
    player2 = Player("Player2", deck2, CardClass.WARRIOR.default_hero)
    agent2 = RandomAgent(player2)

    game = Game(players=(player1, player2))
    game.start()

    return game


def Play():
    try:
        game = CreateGame()

        for player in game.players:
            print("Can mulligan %r" % (player.choice.cards))
            mull_count = random.randint(0, len(player.choice.cards))
            cards_to_mulligan = random.sample(player.choice.cards, mull_count)
            player.choice.choose(*cards_to_mulligan)

        while True:
            # PlayTurn(game)
            PlayOneTurn(game)


    except GameOver:
        print("Game completed normally.")


def PlayOneTurn(game):
    player = game.current_player
    player.agent.Play()
    game.end_turn()


def PlayTurn(game):
    player = game.current_player

    while True:
        hero_power = player.hero.power
        if hero_power.is_usable() and random.random() < 0.1:
            if hero_power.requires_target():
                hero_power.use(target=random.choice(hero_power.targets))
            else:
                hero_power.use()
            continue

        # iterate over our hand and play whatever is playable
        for card in player.hand:
            if card.is_playable() and random.random() < 0.5:
                target = None
                if card.must_choose_one:
                    card = random.choice(card.choose_cards)
                if card.requires_target():
                    target = random.choice(card.targets)
                print("Playing %r on %r" % (card, target))
                card.play(target=target)

                if player.choice:
                    choice = random.choice(player.choice.cards)
                    print("Choosing card %r" % (choice))
                    player.choice.choose(choice)

                continue

        # Randomly attack with whatever can attack
        for character in player.characters:
            if character.can_attack():
                character.attack(random.choice(character.targets))

        break

    game.end_turn()
    return game
