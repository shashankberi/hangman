
class Board:
    '''
    creates a board object that will be used for the game
    '''
    def __init__(self):
        '''
        constructor
        '''
        

empty_board = """
-------|
 |     |
 |
 |
 |
 |
 |
-------
"""
# print(empty_board)

head = """
-------|
 |     |
 |     O
 |
 |
 |
 |
-------
"""
# print(head)

torso = """
-------|
 |     |
 |     O
 |     |
 |     |
 |
 |
-------
"""
# print(torso)

right_arm = """
-------|
 |     |
 |     O
 |     |/
 |     |
 |
 |
-------
"""
# print(right_arm)

left_arm = """
-------|
 |     |
 |     O
 |    \|/
 |     |
 |
 |
-------
"""
# print(left_arm)

right_leg = """
-------|
 |     |
 |     O
 |    \|/
 |     |
 |      \\
 |
-------
"""
# print(right_leg)

left_leg = """
-------|
 |     |
 |     O
 |    \|/
 |     |
 |    / \\
 |
-------
"""
# print(left_leg)