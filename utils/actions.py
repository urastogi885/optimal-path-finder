def go_up(x, y):
    """
    Go 1 unit in positive y-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving a unit in the positive y-direction
    """
    return x, y + 1


def go_down(x, y):
    """
    Go 1 unit in negative y-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving a unit in the negative y-direction
    """
    return x, y - 1


def go_right(x, y):
    """
    Go 1 unit in positive x-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving a unit in the positive x-direction
    """
    return x + 1, y


def go_left(x, y):
    """
    Go 1 unit in negative x-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving a unit in the negative x-direction
    """
    return x - 1, y


def go_up_right(x, y):
    """
    Go 1 unit in both positive x and y directions
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving diagonally up-right
    """
    return x + 1, y + 1


def go_up_left(x, y):
    """
    Go 1 unit in positive y-direction and 1 unit in negative x-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving diagonally up-left
    """
    return x - 1, y + 1


def go_down_right(x, y):
    """
    Go 1 unit in negative y-direction and 1 unit in positive x-direction
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving diagonally down-right
    """
    return x - 1, y + 1


def go_down_left(x, y):
    """
    Go 1 unit in both negative x and y directions
    :param x: x-coordinate of the node
    :param y: y-coordinate of the node
    :return: new coordinates of the node after moving diagonally down-left
    """
    return x - 1, y - 1
