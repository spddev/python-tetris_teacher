import pygame
import random

# создание структуры данных для игровых фигур
# установка глобальных переменных
# функции
# - построение "сетки"
# - отрисовка "сетки"
# - отрисовка окна
# - реализация поворота фигур в главной функции main
# - код главной функции main

"""
квадратная сетка для фигур игры размером 10 x 20, таких как:
S, Z, I, O, J, L, T,
представленных в порядке от 0 до 6 
"""

# инициализация шрифтов в библиотеке pygame
pygame.font.init()

# Глобальные переменные
S_WIDTH = 800
S_HEIGHT = 700
PLAY_WIDTH = 300  # означает: 300 // 10 = 30 - ширина на блок
PLAY_HEIGHT = 600  # означает: 600 // 20 = 30 - высота на блок
BLOCK_SIZE = 30  # размер блока

# x-координата левого верхнего угла
TOP_LEFT_X = (S_WIDTH - PLAY_WIDTH) // 2
# y-координата левого верхнего угла
TOP_LEFT_Y = S_HEIGHT - PLAY_HEIGHT

# Форматы фигур
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# список основных фигур игры
shapes = [S, Z, I, O, J, L, T]
# список цветов основных фигур
# индекс 0 - 6 представляет конкретную фигуру
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


# класс параметров конкретной фигуры
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


# функция создание сетки для размещения фигур игры
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


# функция преобразования формата фигуры
def convert_shape_format(shape):
    pass


# функция проверки правильного размещения фигуры на сетке игрового поля
def valid_space(shape, grid):
    pass


# функция проверки уровня исчезающих "линий"
def check_lost(positions):
    pass


# функция получения фигуры
def get_shape():
    # возвращаем случайную фигуру из списка возможных фигур
    return Piece(5, 0, random.choice(shapes))


# функция отрисовки текста посередине
def draw_text_middle(text, size, color, surface):
    pass


# функция отрисовки сетки игрового поля
def draw_grid(surface, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw_rect(surface, grid[i][j], (TOP_LEFT_X + j * BLOCK_SIZE,
                                                   TOP_LEFT_Y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(surface, (255, 0, 0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)


# Функция "очистки" строк
def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface, grid):
    # заполняем экран игры чёрным цветом
    surface.fill(0, 0, 0)

    # инициализация шрифтов в pygame
    pygame.font.init()
    # устанавливаем шрифт
    font = pygame.font.SysFont('comicsans', 60)
    # отображаем название игры на экране белым цветом
    label = font.render('ТЕТРИС', 1, (255, 255, 255))
    # отображаем название игры в центре экрана
    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH / 2 - (label.get_width() / 2), 30))
    draw_grid(surface, grid)
    pygame.display.update()


# основная функции игры
def main(win):
    # словарь заблокированных позиций сетки
    locked_positions = {}
    # создание сетки из словаря заблокированных позиций
    grid = create_grid(locked_positions)

    # изменение фигуры
    change_piece = False
    # состояние запуска игры
    run = True
    # текущая фигура
    current_piece = get_shape()
    # следующая фигура
    next_piece = get_shape()
    # внутриигровое время
    clock = pygame.time.Clock()
    # время падения фигуры
    fall_time = 0

    # основной игровой цикл
    while run:
        # анализ игровых событий
        for event in pygame.event.get():
            # если получено событие выхода из игры
            if event.type == pygame.QUIT:
                run = False
            # если зарегистрировано событие нажатия клавиш
            if event.type == pygame.KEYDOWN:
                # если нажата клавиша "стрелка влево"
                if event.key == pygame.K_LEFT:
                    # уменьшаем на 1 текущую координату x фигуры
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece += 1
                # если нажата клавиша "стрелка вправо"
                if event.key == pygame.K_RIGHT:
                    # увеличиваем на 1 текущую координату x фигуры
                    current_piece.x += 1
                    # если пространство не позволяет, то меняем фигуру
                    if not (valid_space(current_piece, grid)):
                        current_piece -= 1
                # если нажата клавиша "стрелка вниз"
                if event.key == pygame.K_DOWN:
                    # увеличиваем на 1 текущую координату y фигуры
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                # если нажата клавиша "стрелка вверх"
                if event.key == pygame.K_UP:
                    # вращаем фигуру
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece -= 1

        draw_window(win, grid)


# функция отображения главного меню игры
def main_menu(win):
    main(win)


# задаём размеры окна нашей игры
win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
# указываем название игры в заголовке окна
pygame.display.set_caption('Тетрис')
main_menu(win)
