#! python3
import pyglet
from pyglet.window import mouse
from pyglet.window import key
from pyglet.gl import *
import os
import numpy as np
from threading import Timer


def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return 0


def check_win(board):
    for i in range(3):
        if "OOO" in ''.join(np.transpose(board)[i]):
            return "Player O Won!"
        elif "XXX" in ''.join(np.transpose(board)[i]):
            return "Player X Won!"
        elif "OOO" in ''.join(board[i]):
            return "Player O Won!"
        elif "XXX" in ''.join(board[i]):
            return "Player X Won!"

    if check_diagonals(board):
        return "Player {} Won!".format(check_diagonals(board))

    if '' not in board[0] and '' not in board[1] and '' not in board[2]:
        return "The Game was a Draw!"


class TicTacToe(pyglet.window.Window):

    def __init__(self, width=320, height=320, caption="TicTacToe", resizable=False):
        super(TicTacToe, self).__init__(width, height, caption, resizable)

        self.board_values = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.x, self.y = 0, 0

        pyglet.gl.glClearColor(1, 1, 1, 1)
        script_dir = os.path.dirname(__file__)

        icon = os.path.join(script_dir, './assets/icon.png')
        self.icon = pyglet.image.load(icon)
        self.set_icon(self.icon)

        board = os.path.join(script_dir, './assets/board.png')
        self.board = pyglet.image.load(board)

        self.shape = ""
        self.shapes = ["O", "X", "O", "X", "O", "X", "O", "X", "O"]

        self.label = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.label5 = None
        self.label6 = None
        self.label7 = None
        self.label8 = None

    def on_draw(self):
        glEnable(GL_BLEND)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.clear()
        self.board.blit(0, 0)

        if self.label:
            self.label.draw()
            self.shape = ""

        if self.label1:
            self.label1.draw()
            self.shape = ""

        if self.label2:
            self.label2.draw()
            self.shape = ""

        if self.label3:
            self.label3.draw()
            self.shape = ""

        if self.label4:
            self.label4.draw()
            self.shape = ""

        if self.label5:
            self.label5.draw()
            self.shape = ""

        if self.label6:
            self.label6.draw()
            self.shape = ""

        if self.label7:
            self.label7.draw()
            self.shape = ""

        if self.label8:
            self.label8.draw()
            self.shape = ""

        if check_win(self.board_values):
            print(check_win(self.board_values))

    def on_close(self):
        pyglet.app.exit()

    def on_mouse_press(self, x, y, button, modifiers):

        if button == mouse.LEFT:

            if check_win(self.board_values):
                return pyglet.app.exit()

            if x in range(0, 100) and y in range(0, 98):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=50, y=55,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[2][0] == "":
                    self.board_values[2][0] = self.shapes[0]
                else:
                    return

            elif x in range(115, 205) and y in range(0, 98):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=160, y=55,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[2][1] == "":
                    self.board_values[2][1] = self.shapes[0]
                else:
                    return

            elif x in range(222, 320) and y in range(0, 98):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=270, y=55,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[2][2] == "":
                    self.board_values[2][2] = self.shapes[0]
                else:
                    return

            elif x in range(0, 100) and y in range(112, 204):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=50, y=165,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[1][0] == "":
                    self.board_values[1][0] = self.shapes[0]
                else:
                    return

            elif x in range(115, 205) and y in range(112, 204):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=160, y=165,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[1][1] == "":
                    self.board_values[1][1] = self.shapes[0]
                else:
                    return

            elif x in range(222, 320) and y in range(112, 204):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=270, y=165,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[1][2] == "":
                    self.board_values[1][2] = self.shapes[0]
                else:
                    return

            elif x in range(0, 100) and y in range(220, 320):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=50, y=275,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[0][0] == "":
                    self.board_values[0][0] = self.shapes[0]
                else:
                    return

            elif x in range(115, 205) and y in range(220, 320):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=160, y=275,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[0][1] == "":
                    self.board_values[0][1] = self.shapes[0]
                else:
                    return

            elif x in range(222, 320) and y in range(220, 320):
                self.shape = pyglet.text.Label(self.shapes[0],
                                               font_name='Arial',
                                               font_size=100,
                                               x=270, y=275,
                                               anchor_x='center', anchor_y='center',
                                               color=(0, 0, 0, 255))

                if self.board_values[0][2] == "":
                    self.board_values[0][2] = self.shapes[0]
                else:
                    return

            else:
                return

            if not self.label:
                self.label = self.shape

            elif not self.label1:
                self.label1 = self.shape

            elif not self.label2:
                self.label2 = self.shape

            elif not self.label3:
                self.label3 = self.shape

            elif not self.label4:
                self.label4 = self.shape

            elif not self.label5:
                self.label5 = self.shape

            elif not self.label6:
                self.label6 = self.shape

            elif not self.label7:
                self.label7 = self.shape

            elif not self.label8:
                self.label8 = self.shape

            del self.shapes[0]

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pyglet.app.exit()


def msgs():
    print()
    print("Result of Game will be Printed in Console.")
    print("To End Game, Close Window or Hit Escape.")
    print()


def setup():

    print("Launching Game...")
    main = TicTacToe()

    start = Timer(0.5, msgs)
    start.start()
    pyglet.app.run()


if __name__ == "__main__":
    setup()

''' Coordinates
# 0, 0 - 100, 98
# 115, 0 - 205, 98
# 222, 0 - 320, 98


# 0, 112 - 100, 204
# 115, 112 - 205, 204
# 222, 112 - 320, 204

# 0, 220 - 100, 320
# 115, 220 - 205, 320
# 222, 220 - 320, 320
'''
