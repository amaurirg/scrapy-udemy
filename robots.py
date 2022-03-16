import inspect
from sys import _getframe
from random import randint, choice


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'<Robot {str(self)}>'

    def check_moviment(self):
        method = _getframe(1).f_code.co_name
        # current = _getframe()
        # caller = current.f_back
        # line_no = caller.f_lineno
        # print('current =', current)
        # print('caller =', caller)
        # print('line_no =', line_no)
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
        # return self

    def move_down(self):
        self.check_moviment()
        # return self

    def move_left(self):
        self.check_moviment()
        # return self

    def move_right(self):
        self.check_moviment()
        # return self


class Rewards:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return f'{self.name} ({self.x}, {self.y})'

    def __str__(self):
        return f'Recompensa: {self.name}'



def check_position(obj_robot, list_reward):
    ok = False
    for reward in list_reward:
        if obj_robot.x == reward.x and obj_robot.y == reward.y:
            print(f'Você encontrou a recompensa {reward.name}')
            ok = True
    print(ok)
    print(obj_robot)

rewards_names = ['Ouro', 'Prata', 'Arma']
list_rewards = [Rewards(randint(1, 10), randint(1, 10), choice(rewards_names)) for reward in range(50)]
robot = Robot(randint(1, 10), randint(1, 10))

for chance in range(10):
    position = input('Digite up, down, left ou right para movimentar o robô: ')
    if position == 'up':
        robot.move_up()
    elif position == 'down':
        robot.move_down()
    elif position == 'left':
        robot.move_left()
    elif position == 'right':
        robot.move_right()
    else:
        print('Movimento inválido')
        continue
    check_position(robot, list_rewards)
