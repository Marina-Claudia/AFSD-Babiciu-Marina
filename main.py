import pygame
import random
import sys

# main.py
# Simple Tetris implementation using pygame
# Requirements: pygame (pip install pygame)


WIDTH, HEIGHT = 10, 20
CELL = 30
SIDE = 6 * CELL
SCREEN_W = WIDTH * CELL + SIDE
SCREEN_H = HEIGHT * CELL
FPS = 60

# Tetromino definitions (rotations)
TETROMINOES = {
    'I': [
        [[1, 1, 1, 1]],
        [[1], [1], [1], [1]],
    ],
    'O': [
        [[1, 1],
         [1, 1]],
    ],
    'T': [
        [[0, 1, 0],
         [1, 1, 1]],
        [[1, 0],
         [1, 1],
         [1, 0]],
        [[1, 1, 1],
         [0, 1, 0]],
        [[0, 1],
         [1, 1],
         [0, 1]],
    ],
    'S': [
        [[0, 1, 1],
         [1, 1, 0]],
        [[1, 0],
         [1, 1],
         [0, 1]],
    ],
    'Z': [
        [[1, 1, 0],
         [0, 1, 1]],
        [[0, 1],
         [1, 1],
         [1, 0]],
    ],
    'J': [
        [[1, 0, 0],
         [1, 1, 1]],
        [[1, 1],
         [1, 0],
         [1, 0]],
        [[1, 1, 1],
         [0, 0, 1]],
        [[0, 1],
         [0, 1],
         [1, 1]],
    ],
    'L': [
        [[0, 0, 1],
         [1, 1, 1]],
        [[1, 0],
         [1, 0],
         [1, 1]],
        [[1, 1, 1],
         [1, 0, 0]],
        [[1, 1],
         [0, 1],
         [0, 1]],
    ],
}

COLORS = {
    'I': (80, 220, 255),
    'O': (255, 210, 50),
    'T': (180, 80, 250),
    'S': (100, 255, 100),
    'Z': (255, 80, 80),
    'J': (80, 120, 255),
    'L': (255, 160, 80),
    None: (30, 30, 30),
}

class Piece:
    def __init__(self, kind):
        self.kind = kind
        self.rot = 0
        self.shapes = TETROMINOES[kind]
        self.shape = self.shapes[self.rot]
        self.x = WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self, board):
        old_rot = self.rot
        self.rot = (self.rot + 1) % len(self.shapes)
        self.shape = self.shapes[self.rot]
        if collision(self, board):
            # try simple wall kicks: left or right
            for dx in (-1, 1, -2, 2):
                self.x += dx
                if not collision(self, board):
                    return
                self.x -= dx
            # revert
            self.rot = old_rot
            self.shape = self.shapes[self.rot]

def create_board():
    return [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

def collision(piece, board, dx=0, dy=0):
    for r, row in enumerate(piece.shape):
        for c, cell in enumerate(row):
            if not cell:
                continue
            x = piece.x + c + dx
            y = piece.y + r + dy
            if x < 0 or x >= WIDTH or y >= HEIGHT:
                return True
            if y >= 0 and board[y][x] is not None:
                return True
    return False

def lock_piece(piece, board):
    for r, row in enumerate(piece.shape):
        for c, cell in enumerate(row):
            if not cell:
                continue
            x = piece.x + c
            y = piece.y + r
            if 0 <= y < HEIGHT:
                board[y][x] = piece.kind

def clear_lines(board):
    new_board = [row for row in board if any(cell is None for cell in row)]
    lines_cleared = HEIGHT - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [None for _ in range(WIDTH)])
    return new_board, lines_cleared

def next_piece_generator():
    bag = []
    while True:
        if not bag:
            bag = list(TETROMINOES.keys())
            random.shuffle(bag)
        yield bag.pop()

def draw_board(screen, board, offset_x=0, offset_y=0):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            kind = board[y][x]
            color = COLORS[kind]
            rect = pygame.Rect(offset_x + x*CELL, offset_y + y*CELL, CELL, CELL)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (10,10,10), rect, 1)

def draw_piece(screen, piece, offset_x=0, offset_y=0):
    for r, row in enumerate(piece.shape):
        for c, cell in enumerate(row):
            if not cell:
                continue
            x = piece.x + c
            y = piece.y + r
            if y >= 0:
                rect = pygame.Rect(offset_x + x*CELL, offset_y + y*CELL, CELL, CELL)
                pygame.draw.rect(screen, COLORS[piece.kind], rect)
                pygame.draw.rect(screen, (10,10,10), rect, 1)

def draw_preview(screen, kind, pos, title="Next"):
    font = pygame.font.SysFont("arial", 18)
    surf = font.render(title, True, (220,220,220))
    screen.blit(surf, pos)
    off_x = pos[0]
    off_y = pos[1] + 24
    shape = TETROMINOES[kind][0]
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                rect = pygame.Rect(off_x + c*CELL, off_y + r*CELL, CELL, CELL)
                pygame.draw.rect(screen, COLORS[kind], rect)
                pygame.draw.rect(screen, (10,10,10), rect, 1)

def game_over(board):
    return any(board[0][x] is not None for x in range(WIDTH))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Tetris - simple")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)

    board = create_board()
    gen = next_piece_generator()
    current = Piece(next(gen))
    nxt = next(gen)
    hold = None
    hold_used = False

    drop_counter = 0
    drop_speed = 30  # frames between automatic drops; lower = faster
    score = 0
    level = 1
    lines_total = 0
    running = True
    paused = False

    while running:
        dt = clock.tick(FPS)
        if not paused:
            drop_counter += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_p:
                    paused = not paused
                if paused:
                    continue
                if event.key == pygame.K_LEFT:
                    if not collision(current, board, dx=-1):
                        current.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not collision(current, board, dx=1):
                        current.x += 1
                elif event.key == pygame.K_DOWN:
                    if not collision(current, board, dy=1):
                        current.y += 1
                elif event.key == pygame.K_UP:
                    current.rotate(board)
                elif event.key == pygame.K_SPACE:
                    # hard drop
                    while not collision(current, board, dy=1):
                        current.y += 1
                    lock_piece(current, board)
                    board, cleared = clear_lines(board)
                    if cleared:
                        score += (cleared ** 2) * 100
                        lines_total += cleared
                        level = 1 + lines_total // 10
                        drop_speed = max(5, 30 - (level-1)*2)
                    current = Piece(nxt)
                    nxt = next(gen)
                    hold_used = False
                elif event.key == pygame.K_c:
                    if not hold_used:
                        if hold is None:
                            hold = current.kind
                            current = Piece(nxt)
                            nxt = next(gen)
                        else:
                            current_kind = current.kind
                            current = Piece(hold)
                            hold = current_kind
                        hold_used = True

        if not paused:
            if drop_counter >= drop_speed:
                drop_counter = 0
                if not collision(current, board, dy=1):
                    current.y += 1
                else:
                    lock_piece(current, board)
                    board, cleared = clear_lines(board)
                    if cleared:
                        score += (cleared ** 2) * 100
                        lines_total += cleared
                        level = 1 + lines_total // 10
                        drop_speed = max(5, 30 - (level-1)*2)
                    current = Piece(nxt)
                    nxt = next(gen)
                    hold_used = False
                    if collision(current, board):
                        # Game over
                        running = False

        # Draw
        screen.fill((18, 18, 18))
        # board area
        draw_board(screen, board, 0, 0)
        draw_piece(screen, current, 0, 0)

        # Sidebar
        side_x = WIDTH * CELL + 10
        # next
        draw_preview(screen, nxt, (side_x, 10), "Next")
        # hold
        font_small = pygame.font.SysFont("consolas", 18)
        screen.blit(font_small.render("Hold", True, (220,220,220)), (side_x, 140))
        if hold:
            draw_preview(screen, hold, (side_x, 170), "")
        # stats
        stats_y = 320
        screen.blit(font.render(f"Score: {score}", True, (220,220,220)), (side_x, stats_y))
        screen.blit(font.render(f"Level: {level}", True, (220,220,220)), (side_x, stats_y + 30))
        screen.blit(font.render(f"Lines: {lines_total}", True, (220,220,220)), (side_x, stats_y + 60))
        if paused:
            big = pygame.font.SysFont("consolas", 48).render("PAUSED", True, (255, 255, 255))
            screen.blit(big, (WIDTH*CELL//2 - big.get_width()//2, SCREEN_H//2 - big.get_height()//2))

        pygame.display.flip()

    # Game over screen
    over_font = pygame.font.SysFont("consolas", 48)
    small = pygame.font.SysFont("consolas", 24)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        screen.fill((5,5,5))
        screen.blit(over_font.render("GAME OVER", True, (200,50,50)), (50, 100))
        screen.blit(small.render(f"Score: {score}", True, (220,220,220)), (50, 180))
        screen.blit(small.render("Press any key to quit", True, (180,180,180)), (50, 220))
        pygame.display.flip()
        clock.tick(15)

if __name__ == "__main__":
    main()