from constants import LINE_WIDTH, PLAYER_RADIUS
import pygame
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0  # in degrees
        self.width = LINE_WIDTH

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), self.width)
    
        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]