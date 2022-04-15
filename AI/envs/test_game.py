# coding=utf-8

import sys

from fireplace import cards
import env


def main():
    cards.db.initialize()
    episode_num = 1
    if len(sys.argv) > 1:
        episode_num = int(sys.argv[1])
    for i in range(int(episode_num)):
        env.Play()


if __name__ == "__main__":
    main()
