import pygame
import random

FPS = 60

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_BUFFER = 10
BALL_WIDTH = 10
BALL_HEIGHT = 10

PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def initBall():
    num = random.randint(0,9)
    paddle1YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
    paddle2YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
    ballXDirection = 1
    ballYDirection = 1
    ballXPos = WINDOW_WIDTH/2 - BALL_WIDTH/2
    if(0 < num < 3):
        ballXDirection = 1
        ballYDirection = 1
    if (3 <= num < 5):
        ballXDirection = -1
        ballYDirection = 1
    if (5 <= num < 8):
        ballXDirection = 1
        ballYDirection = -1
    if (8 <= num < 10):
        ballXDirection = -1
        ballYDirection = -1
    num = random.randint(0,9)
    ballYPos = num*(WINDOW_HEIGHT - BALL_HEIGHT)/9
    return [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]


def drawBall(screen, ballXPos, ballYPos):
    ball = pygame.Rect(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.rect(screen, WHITE, ball)

def drawPaddle1(screen, paddle1YPos):
    paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle1)

def drawPaddle2(screen, paddle2YPos):
    paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.rect(screen, WHITE, paddle2)

def updateBall(paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection):
    global score
    ballXPos = ballXPos + ballXDirection * BALL_X_SPEED
    ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED
    if (ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1YPos + PADDLE_HEIGHT):
        ballXDirection = 1
    elif (ballXPos < 0):
        [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection] = initBall()
        score = score - 1
        return [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]
    if (ballXPos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYPos + BALL_HEIGHT >= paddle2YPos and ballYPos - BALL_HEIGHT <= paddle2YPos + PADDLE_HEIGHT):
        ballXDirection = -1
    elif (ballXPos >= WINDOW_WIDTH - BALL_WIDTH):
        [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection] = initBall()
        score = score + 1
        return [paddle1YPos, paddle2YPos, allXPos, ballYPos, ballXDirection, ballYDirection]
    if(ballYPos < 0):
        ballYPos = 0;
        ballYDirection = 1;
    elif(ballYPos > WINDOW_HEIGHT - BALL_HEIGHT):
        ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1
    return [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]


def updatePaddle1(paddle1YPos):
    if(pygame.key.get_pressed()[pygame.K_UP]):
        paddle1YPos = paddle1YPos - PADDLE_SPEED
    if(pygame.key.get_pressed()[pygame.K_DOWN]):
        paddle1YPos = paddle1YPos + PADDLE_SPEED
    if(paddle1YPos < 0):
        paddle1YPos = 0
    if(paddle1YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos

def updatePaddle2(paddle2YPos, ballYPos):
    if(paddle2YPos < ballYPos):
        paddle2YPos = paddle2YPos + PADDLE_SPEED
    if(paddle2YPos > ballYPos):
        paddle2YPos = paddle2YPos - PADDLE_SPEED
    if (paddle2YPos < 0):
        paddle2YPos = 0
    if (paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle2YPos

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    done = False

    global score
    score = 0

    [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection] = initBall()

    while not done:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                done = True
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                done = True

        screen.fill(BLACK)
        paddle1YPos = updatePaddle1(paddle1YPos)
        drawPaddle1(screen, paddle1YPos)
        paddle2YPos = updatePaddle2(paddle2YPos, ballYPos)
        drawPaddle2(screen, paddle2YPos)
        [paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection] = updateBall(paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection)
        drawBall(screen, ballXPos, ballYPos)
        pygame.display.flip()
        print "Score  = " + str(score)

if __name__ == "__main__":
    main()