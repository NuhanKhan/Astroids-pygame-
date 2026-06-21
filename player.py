from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0  # in degrees
        self.shot_cooldown_timer = 0.0  # seconds

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), LINE_WIDTH)

    def rotate(self, direction: int, dt: float) -> None:
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        # in the Player class
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        # create a new shot and shoot it
        if self.shot_cooldown_timer > 0:
            return  # still in cooldown, cannot shoot yet
        else:
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS  # reset cooldown timer
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1, dt)
        if keys[pygame.K_d]:
            self.rotate(1, dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # create a new shot and shoot it
            self.shoot()

        self.shot_cooldown_timer -= dt  # decrease cooldown timer by dt