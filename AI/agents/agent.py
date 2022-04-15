# coding=utf-8
"""
所有机器人的基类
"""

class Agent:
    def __init__(self, owner) -> None:
        self.owner = owner
        owner.agent = self

    def Play(self):
        """
        执行当前轮次的操作
        """
        raise NotImplementedError