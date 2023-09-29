import random
import pygame

# Define the game variables
WIDTH = 500
HEIGHT = 500
SPEED = 5

# Define the game objects
class Player:
  def _init_(self, x, y):
    self.x = x
    self.y = y
    self.speed = SPEED

  def move(self):
    self.x += self.speed
    self.y += self.speed

    if self.x < 0:
      self.x = 0
    elif self.x > WIDTH - 10:
      self.x = WIDTH - 10

    if self.y < 0:
      self.y = 0
    elif self.y > HEIGHT - 10:
      self.y = HEIGHT - 10

class Obstacle:
  def _init_(self, x, y, type):
    self.x = x
    self.y = y
    self.type = type

# Create the game window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Environmental Game")

# Create the player object
player = Player(100, 100)

# Create the obstacle objects
obstacles = []
for i in range(10):
  obstacle = Obstacle(random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10), "tree")
  obstacles.append(obstacle)

# Game loop
while True:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.speed -= 1
      elif event.key == pygame.K_UP:
        player.speed -= 1
      elif event.key == pygame.K_RIGHT:
        player.speed += 1
      elif event.key == pygame.K_DOWN:
        player.speed += 1

  # Move the player
  player.move()

  # Check if the player is hitting an obstacle
  for obstacle in obstacles:
    if player.x == obstacle.x and player.y == obstacle.y:
      # If the player is hitting an obstacle, move them back to their previous position
      player.x -= player.speed
      player.y -= player.speed

  # Draw the game state
  screen.fill((255, 255, 255))

  # Draw the player
  pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, 10, 10))

  # Draw the obstacles
  for obstacle in obstacles:
    pygame.draw.rect(screen, (0, 255, 0), (obstacle.x, obstacle.y, 10, 10))

  # Update the display
  pygame.display.flip()

# Get the keyboard input
keys = pygame.key.get_pressed()

# Move the player based on the keyboard input
if keys[pygame.K_LEFT]:
  player.speed -= 1
if keys[pygame.K_UP]:
  player.speed -= 1
if keys[pygame.K_RIGHT]:
  player.speed += 1
if keys[pygame.K_DOWN]:
  player.speed += 1
