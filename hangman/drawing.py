import pygame
import random
import math
import time
from hangman.constants import WHITE, BLACK, WIDTH, HEIGHT, LETTER_TEXT, WORD_FONT, RADIUS, GAP

class Drawing:
    def __init__(self):
        # game variables

        words = ["PYTHON", "RUBY", "JAVA", "JAVASCRIPT"]
        self.word = random.choice(words)
        self.guessed = []

        # buttons variables
        self.start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
        self.start_y = 400
        self.A = 65
        self.letters = []
        self.hangman_status = 0

        for i in range(26):
            self.x = self.start_x + (RADIUS * 2 + GAP) * (i % 13) + GAP * 2 
            self.y = self.start_y + (RADIUS * 2 + GAP) * (i // 13)
            self.letters.append([self.x, self.y, chr(self.A + i), True])

    def draw(self, window):
        window.fill(WHITE)
        image = pygame.image.load(f'images/hangman{self.hangman_status}.png')
        window.blit(image, (100, 100))
        
        # draw buttons
        for letter in self.letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
                text = LETTER_TEXT.render(ltr, 1, BLACK)
                window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
        # draw text
        display_word = ""
        for i in self.word:
            if i in self.guessed:
                display_word += i + " "
            if i not in self.guessed:
                display_word += "_ "

        text = WORD_FONT.render(display_word, 1, BLACK)
        window.blit(text, (400, 200))

    def collision(self):
        m_x, m_y = pygame.mouse.get_pos()
        for letter in self.letters:
            x, y, ltr, visible = letter
            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
            if visible:
                if dis < RADIUS:
                    self.guessed.append(ltr)
                    letter[3] = False
                    if ltr not in self.word:
                        self.hangman_status += 1

    def win_lose(self):
        message = ''
        count = 0
        # if you lost
        if self.hangman_status >= 6:
            message = "You lost."
            return [False, message]

        # if you won
        for i in self.word:
            if i not in self.guessed:
                break
            count += 1
            if count == len(self.word):
                message = "You won!"
                return [False, message]

        # in case you're still playing
        return [True, '']

    def display_message(self, screen, msg):
        screen.fill(WHITE)
        text = LETTER_TEXT.render(msg, True, BLACK)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.update()