
import pygame
import sys
import random

# -------------------- INITIALIZATION --------------------

pygame.init()

WIDTH = 1000
HEIGHT = 850

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe - Ultimate Edition")

clock = pygame.time.Clock()

# -------------------- COLORS --------------------

BG = (13, 17, 32)
PANEL = (24, 31, 52)
PANEL_LIGHT = (34, 43, 68)
WHITE = (245, 247, 255)
GRAY = (145, 155, 180)
CYAN = (40, 220, 230)
PURPLE = (145, 100, 255)
ORANGE = (255, 160, 75)
GREEN = (70, 220, 150)
RED = (255, 90, 110)

# -------------------- FONTS --------------------

title_font = pygame.font.SysFont("tahoma", 58, bold=True)
large_font = pygame.font.SysFont("tahoma", 48, bold=True)
font = pygame.font.SysFont("tahoma", 29, bold=True)
medium_font = pygame.font.SysFont("tahoma", 23)
small_font = pygame.font.SysFont("tahoma", 18)

# -------------------- LANGUAGES --------------------

languages = {
    "EN": {
        "name": "English",
        "title": "TIC TAC TOE",
        "subtitle": "Choose your game mode",
        "two": "Two Players",
        "computer": "Play vs Computer",
        "language": "Language",
        "your_turn": "Your Turn (X)",
        "computer_turn": "Computer's Turn",
        "player_x": "Player X's Turn",
        "player_o": "Player O's Turn",
        "x_wins": "Player X Wins!",
        "o_wins": "Player O Wins!",
        "you_win": "You Win!",
        "computer_wins": "Computer Wins!",
        "draw": "It's a Draw!",
        "restart": "Restart",
        "menu": "Main Menu",
        "score": "SCORE",
        "choose": "Choose a mode",
        "playing": "Playing",
        "made": "Made with Python & Pygame"
    },

    "FA": {
        "name": "فارسی",
        "title": "دوز",
        "subtitle": "حالت بازی را انتخاب کن",
        "two": "دو نفره",
        "computer": "بازی با کامپیوتر",
        "language": "زبان",
        "your_turn": "نوبت شما (X)",
        "computer_turn": "نوبت کامپیوتر",
        "player_x": "نوبت بازیکن X",
        "player_o": "نوبت بازیکن O",
        "x_wins": "بازیکن X برنده شد!",
        "o_wins": "بازیکن O برنده شد!",
        "you_win": "شما برنده شدید!",
        "computer_wins": "کامپیوتر برنده شد!",
        "draw": "بازی مساوی شد!",
        "restart": "شروع مجدد",
        "menu": "منوی اصلی",
        "score": "امتیاز",
        "choose": "یک حالت را انتخاب کن",
        "playing": "در حال بازی",
        "made": "ساخته شده با پایتون و Pygame"
    },

    "DE": {
        "name": "Deutsch",
        "title": "TIC TAC TOE",
        "subtitle": "Wähle deinen Spielmodus",
        "two": "Zwei Spieler",
        "computer": "Gegen Computer",
        "language": "Sprache",
        "your_turn": "Du bist dran (X)",
        "computer_turn": "Computer ist dran",
        "player_x": "Spieler X ist dran",
        "player_o": "Spieler O ist dran",
        "x_wins": "Spieler X gewinnt!",
        "o_wins": "Spieler O gewinnt!",
        "you_win": "Du gewinnst!",
        "computer_wins": "Computer gewinnt!",
        "draw": "Unentschieden!",
        "restart": "Neustart",
        "menu": "Hauptmenü",
        "score": "PUNKTE",
        "choose": "Modus auswählen",
        "playing": "Spiel läuft",
        "made": "Erstellt mit Python & Pygame"
    },

    "FR": {
        "name": "Français",
        "title": "MORPION",
        "subtitle": "Choisissez votre mode",
        "two": "Deux joueurs",
        "computer": "Contre ordinateur",
        "language": "Langue",
        "your_turn": "À vous (X)",
        "computer_turn": "Tour de l'ordinateur",
        "player_x": "Tour du joueur X",
        "player_o": "Tour du joueur O",
        "x_wins": "Le joueur X gagne !",
        "o_wins": "Le joueur O gagne !",
        "you_win": "Vous avez gagné !",
        "computer_wins": "L'ordinateur gagne !",
        "draw": "Match nul !",
        "restart": "Recommencer",
        "menu": "Menu principal",
        "score": "SCORE",
        "choose": "Choisissez un mode",
        "playing": "En cours",
        "made": "Créé avec Python & Pygame"
    },

    "ES": {
        "name": "Español",
        "title": "TRES EN RAYA",
        "subtitle": "Elige el modo de juego",
        "two": "Dos jugadores",
        "computer": "Contra ordenador",
        "language": "Idioma",
        "your_turn": "Tu turno (X)",
        "computer_turn": "Turno del ordenador",
        "player_x": "Turno del jugador X",
        "player_o": "Turno del jugador O",
        "x_wins": "¡Gana el jugador X!",
        "o_wins": "¡Gana el jugador O!",
        "you_win": "¡Has ganado!",
        "computer_wins": "¡Gana el ordenador!",
        "draw": "¡Empate!",
        "restart": "Reiniciar",
        "menu": "Menú principal",
        "score": "PUNTOS",
        "choose": "Elige un modo",
        "playing": "Jugando",
        "made": "Hecho con Python y Pygame"
    }
}

language_codes = list(languages.keys())
language_index = 0
language = language_codes[language_index]


def tr(key):
    return languages[language][key]


def prepare_text(text):
    if language == "FA":
        try:
            import arabic_reshaper
            from bidi.algorithm import get_display

            text = arabic_reshaper.reshape(text)
            text = get_display(text)
        except ImportError:
            pass

    return text


def draw_text(text, selected_font, color, center):
    text = prepare_text(str(text))
    image = selected_font.render(text, True, color)
    rect = image.get_rect(center=center)
    screen.blit(image, rect)


# -------------------- BUTTONS --------------------

def draw_button(rect, text, color, mouse_pos):
    hovered = rect.collidepoint(mouse_pos)

    shadow = pygame.Rect(rect.x, rect.y + 6, rect.width, rect.height)
    pygame.draw.rect(screen, (7, 10, 22), shadow, border_radius=18)

    button_color = tuple(min(c + 20, 255) for c in color) if hovered else color

    pygame.draw.rect(screen, button_color, rect, border_radius=18)
    pygame.draw.rect(screen, (90, 105, 145), rect, 2, border_radius=18)

    draw_text(text, font, WHITE, rect.center)


# -------------------- GAME DATA --------------------

board = [""] * 9

current_player = "X"
game_mode = ""
game_state = "menu"

game_over = False
winner = None
winning_line = None

scores = {
    "X": 0,
    "O": 0,
    "Draw": 0
}

# -------------------- GAME LOGIC --------------------

def check_winner(b):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for line in lines:
        a, b1, c = line

        if b[a] == b[b1] == b[c] and b[a] != "":
            return b[a], line

    if "" not in b:
        return "Draw", None

    return None, None


def minimax(b, maximizing):
    result, line = check_winner(b)

    if result == "O":
        return 10

    if result == "X":
        return -10

    if result == "Draw":
        return 0

    if maximizing:
        best_score = -100

        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = ""
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = ""
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -100
    best_moves = []

    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""

            if score > best_score:
                best_score = score
                best_moves = [i]
            elif score == best_score:
                best_moves.append(i)

    if best_moves:
        board[random.choice(best_moves)] = "O"


def finish_game():
    global game_over, winner, winning_line

    result, line = check_winner(board)

    if result is not None:
        game_over = True
        winner = result
        winning_line = line
        scores[result] += 1


def reset_game():
    global board, current_player
    global game_over, winner, winning_line

    board = [""] * 9
    current_player = "X"
    game_over = False
    winner = None
    winning_line = None


def start_game(mode):
    global game_mode, game_state

    game_mode = mode
    reset_game()
    game_state = "game"


# -------------------- DRAW BACKGROUND --------------------

def draw_background():
    screen.fill(BG)

    pygame.draw.circle(screen, (25, 35, 65), (30, 40), 170)
    pygame.draw.circle(screen, (35, 25, 65), (970, 800), 220)

    pygame.draw.circle(screen, (25, 65, 80), (950, 70), 100)


# -------------------- MENU SCREEN --------------------

def draw_menu(mouse_pos):
    draw_background()

    draw_text(tr("title"), title_font, CYAN, (500, 180))
    draw_text(tr("subtitle"), medium_font, GRAY, (500, 255))

    two_button = pygame.Rect(280, 350, 440, 85)
    computer_button = pygame.Rect(280, 465, 440, 85)
    language_button = pygame.Rect(340, 600, 320, 65)

    draw_button(two_button, tr("two"), PURPLE, mouse_pos)
    draw_button(computer_button, tr("computer"), (15, 135, 160), mouse_pos)

    draw_button(
        language_button,
        tr("language") + ": " + languages[language]["name"],
        PANEL_LIGHT,
        mouse_pos
    )

    draw_text(tr("made"), small_font, GRAY, (500, 780))


# -------------------- GAME SCREEN --------------------

def draw_game(mouse_pos):
    draw_background()

    draw_text(tr("title"), title_font, CYAN, (500, 65))

    if game_over:
        if winner == "Draw":
            status = tr("draw")
            status_color = WHITE

        elif game_mode == "computer" and winner == "X":
            status = tr("you_win")
            status_color = GREEN

        elif game_mode == "computer" and winner == "O":
            status = tr("computer_wins")
            status_color = ORANGE

        elif winner == "X":
            status = tr("x_wins")
            status_color = CYAN

        else:
            status = tr("o_wins")
            status_color = ORANGE

    else:
        if game_mode == "computer":
            status = tr("your_turn") if current_player == "X" else tr("computer_turn")
        else:
            status = tr("player_x") if current_player == "X" else tr("player_o")

        status_color = CYAN if current_player == "X" else ORANGE

    draw_text(status, font, status_color, (500, 140))

    # Score panel
    score_panel = pygame.Rect(300, 170, 400, 70)
    pygame.draw.rect(screen, PANEL, score_panel, border_radius=15)

    draw_text(tr("score"), small_font, GRAY, (365, 205))
    draw_text("X: " + str(scores["X"]), font, CYAN, (500, 205))
    draw_text("O: " + str(scores["O"]), font, ORANGE, (600, 205))

    # Board
    board_x = 250
    board_y = 280
    cell_size = 166

    board_rect = pygame.Rect(board_x, board_y, 500, 500)
    pygame.draw.rect(screen, PANEL, board_rect, border_radius=25)

    for i in range(1, 3):
        pygame.draw.line(
            screen, PANEL_LIGHT,
            (board_x + i * cell_size, board_y + 15),
            (board_x + i * cell_size, board_y + 485),
            7
        )

        pygame.draw.line(
            screen, PANEL_LIGHT,
            (board_x + 15, board_y + i * cell_size),
            (board_x + 485, board_y + i * cell_size),
            7
        )

    for i in range(9):
        row = i // 3
        col = i % 3

        x = board_x + col * cell_size
        y = board_y + row * cell_size

        cell_rect = pygame.Rect(x + 7, y + 7, cell_size - 14, cell_size - 14)

        if cell_rect.collidepoint(mouse_pos) and board[i] == "" and not game_over:
            pygame.draw.rect(screen, PANEL_LIGHT, cell_rect, border_radius=15)

        center = (x + cell_size // 2, y + cell_size // 2)

        if board[i] == "X":
            draw_text("X", large_font, CYAN, center)

        elif board[i] == "O":
            draw_text("O", large_font, ORANGE, center)

    # Winning line
    if winning_line:
        first = winning_line[0]
        last = winning_line[2]

        x1 = board_x + (first % 3) * cell_size + cell_size // 2
        y1 = board_y + (first // 3) * cell_size + cell_size // 2

        x2 = board_x + (last % 3) * cell_size + cell_size // 2
        y2 = board_y + (last // 3) * cell_size + cell_size // 2

        pygame.draw.line(screen, GREEN, (x1, y1), (x2, y2), 7)

    restart_button = pygame.Rect(250, 790, 230, 48)
    menu_button = pygame.Rect(520, 790, 230, 48)

    draw_button(restart_button, tr("restart"), PURPLE, mouse_pos)
    draw_button(menu_button, tr("menu"), (15, 135, 160), mouse_pos)


# -------------------- INPUT HANDLING --------------------

def handle_board_click(pos):
    global current_player

    if game_over:
        return

    x, y = pos

    board_x = 250
    board_y = 280
    cell_size = 166

    if not (board_x <= x < board_x + 500 and
            board_y <= y < board_y + 500):
        return

    col = (x - board_x) // cell_size
    row = (y - board_y) // cell_size

    index = int(row * 3 + col)

    if board[index] != "":
        return

    board[index] = current_player

    finish_game()

    if game_over:
        return

    if game_mode == "computer":
        current_player = "O"
        computer_move()
        finish_game()

        if not game_over:
            current_player = "X"

    else:
        current_player = "O" if current_player == "X" else "X"


# -------------------- MAIN LOOP --------------------

running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            x, y = event.pos

            if game_state == "menu":

                if 280 <= x <= 720 and 350 <= y <= 435:
                    start_game("two")

                elif 280 <= x <= 720 and 465 <= y <= 550:
                    start_game("computer")

                elif 340 <= x <= 660 and 600 <= y <= 665:
                    language_index += 1
                    language_index %= len(language_codes)
                    language = language_codes[language_index]

            elif game_state == "game":

                if 250 <= x <= 480 and 790 <= y <= 838:
                    reset_game()

                elif 520 <= x <= 750 and 790 <= y <= 838:
                    reset_game()
                    scores = {"X": 0, "O": 0, "Draw": 0}
                    game_state = "menu"

                else:
                    handle_board_click(event.pos)

    if game_state == "menu":
        draw_menu(mouse_pos)

    else:
        draw_game(mouse_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
