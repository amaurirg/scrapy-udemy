"""
Um robô que percorre as posições a busca de uma recompensa
"""

from random import randint


class Point:
    """ Classe abstrata Mãe que possui as posições do robô e das recompensas """

    def __init__(self, x, y):
        """
        :param x: posição do robô e das recompensas no eixo x
        :param y: posição do robô e das recompensas no eixo y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Método para retorno do formato do objeto
        :return:
        """
        return f"<Point - pos: ({self.x}, {self.y})>"

    def __repr__(self):
        """
        Chama o método __str__
        :return: representação do objeto em formato str conforme o método __str__
        """
        return str(self)


class Reward(Point):
    """ Recompensa que herda de Point e possui o atributo self.name """

    def __init__(self, x, y, name):
        """
        Herda x e y de Point
        :param x: posição das recompensas no eixo x
        :param y: posição das recompensas no eixo y
        :param name: nome da recompensa
        """
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        """
        Método para retorno do formato do objeto
        :return: formato do objeto
        """
        return f"<Reward {self.name} - pos: ({self.x}, {self.y})>"

    def __repr__(self):
        """
        Chama o método __str__
        :return: representação do objeto em formato str conforme o método __str__
        """
        return str(self)


class Robot(Point):
    """ Move a posição do robô em uma matriz 10x10 """

    def check_moviment(self, pos):
        """
        Checa se a posição será menor que 0 ou maior que 10 pois não é possível ultrapassar a matriz 10x10
        :param pos: posição a ser checada
        :return: True caso seja um movimento válido ou False caso seja menor que 0 ou maior 10
        """
        if not 0 <= pos <= 10:
            print("Movimento proibido")
            return False
        return True

    def move_up(self):
        """
        Move uma posição para cima no eixo y
        :return: acrescenta uma posição no eixo y caso o valor seja válido
        """
        if self.check_moviment(self.y + 1):
            self.y += 1

    def move_down(self):
        """
        Move uma posição para baixo no eixo y
        :return: diminui uma posição no eixo y caso o valor seja válido
        """
        if self.check_moviment(self.y - 1):
            self.y -= 1

    def move_left(self):
        """
        Move uma posição para a esquerda no eixo x
        :return: diminui uma posição no eixo x caso o valor seja válido
        """
        if self.check_moviment(self.x - 1):
            self.x -= 1

    def move_right(self):
        """
        Move uma posição para a direita no eixo x
        :return: acrescenta uma posição no eixo x caso o valor seja válido
        """
        if self.check_moviment(self.x + 1):
            self.x += 1

    def __str__(self):
        """
        Método para retorno do formato do objeto
        :return: formato do objeto
        """
        return f"<Robot - pos: ({self.x}, {self.y})>"

    def __repr__(self):
        """
        Chama o método __str__
        :return: representação do objeto em formato str conforme o método __str__
        """
        return str(self)


def check_reward(robot, rewards):
    """
    Checa se o robô está na mesma posição da recompensa
    :param robot: objeto robô com suas posições
    :param rewards: lista de recompensas
    :return: True caso o robê esteja na mesma posição da recompensa ou False caso não esteja
    """
    for reward in rewards:
        if robot.x == reward.x and robot.y == reward.y:
            print(f"O robô encontrou a recompensa: {reward.name}")
            return True
    return False


rewards = [Reward(randint(0, 10), randint(0, 10), reward_name) for i in range(3) for reward_name in
           ["moeda", "energia", "arma"]]

robot = Robot(randint(0, 10), randint(0, 10))


def attempts(robot):
    """
    Pede ao usuário que mova as posições do robô para encontrar as recompensas
    Chama o método de acordo com o movimento solicitado pelo usuário
    Mostra a posição atual do robô
    Chama a função check_reward(robot, rewards)
    :param robot: objeto Robot(x, y)
    :return:
    """
    movements = {
        "up": robot.move_up,
        "down": robot.move_down,
        "left": robot.move_left,
        "right": robot.move_right
    }
    for i in range(10):
        movement = input("Digite up, down, left ou right para o movimento: ")
        try:
            movements[movement]()
        except:
            print("Movimento inválido!")
        # if movement == "up":
        #     robot.move_up()
        # elif movement == "down":
        #     robot.move_down()
        # elif movement == "left":
        #     robot.move_left()
        # elif movement == "right":
        #     robot.move_right()
        # else:
        #     print("Movimento inválido!")
        print(robot)
        check_reward(robot, rewards)


if __name__ == "__main__":
    attempts(robot)
