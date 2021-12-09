import inspect
import sys


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'<Robot {str(self)}>'

    def check_moviment(self):
        method = sys._getframe(1).f_code.co_name
        dic = {
            'move_up': self.y + 1,
            'move_down': self.y - 1,
            'move_left': self.x - 1,
            'move_right': self.x + 1
        }
        if (method == 'move_up' and self.y < 10) or (method == 'move_down' and self.y > 0):
            self.y = dic[method]
        elif (method == 'move_left' and self.x > 0) or (method == 'move_right' and self.x < 10):
            self.x = dic[method]
        else:
            print('Movimento proibido')

    def move_up(self):
        self.check_moviment()
        return self

    def move_down(self):
        self.check_moviment()
        return self

    def move_left(self):
        self.check_moviment()
        return self

    def move_right(self):
        self.check_moviment()
        return self


class Rewards:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome

    def __repr__(self):
        return f'{self.nome} ({self.x}, {self.y})'

    def __str__(self):
        return f'Recompensa: {self.nome}'


class Position:
    def check_position(self, obj_robot, obj_reward):
        if obj_robot.x == obj_reward.x and obj_robot.y == obj_reward.y:
            print(f'Você encontrou a {obj_reward}')

