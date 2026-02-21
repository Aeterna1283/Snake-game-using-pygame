import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        #Body of the snake, using 3 2d vectors
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        #for importing the snake head pngs
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
        #for importing the snake tail pngs
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        
        #vertical and horizontal pngs
        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        
        #curved body pngs
        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
    
    #function to draw the snake on the board    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            #1. rect for position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            #2.what position is the face heading
            if index == 0:
                screen.blit(self.head, block_rect)
           
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
                
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block 
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
                        
                    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
            
            
        
        
        # for block in self.body:
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
        #     #creates a rect
        #     block_rect = pygame.Rect(x_pos, y_pos , cell_size, cell_size)
        #     pygame.draw.rect(screen, (100, 100, 243), block_rect)
        #     #draw the rect
            
            
    def move_snake(self):
        if self.new_block == True:
            #copy the snake with last index
            body_copy = self.body[:]
            #insert the direction into the first index of the snake
            body_copy.insert(0, body_copy[0] + self.direction)
            # The body is set equal to the entire copy with inserted index
            self.body = body_copy[:]
            self.new_block = False
            
        else:  
            #copy the snake - the last index
            body_copy = self.body[:-1]
            #insert the direction into the first index of the snake
            body_copy.insert(0, body_copy[0] + self.direction)
             # The body is set equal to the entire copy with inserted index
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
        
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        
               
class FRUIT:
    def __init__(self):
        #create an x and y position
        self.randomize()
        
        #draw a square
    def draw_fruit(self):
        #create a rectangle in the right position
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen, (226, 130, 114), fruit_rect)
        #draw the rect
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
        
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
          self.snake.move_snake()
          self.check_collision()
          self.check_fail()
    
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #reposition the apple
            self.fruit.randomize()
            #add another vector to the snake
            self.snake.add_block()
            
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()
    
    def check_fail(self):
        #check if the snail is outside the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        #check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
            
        
    def game_over(self):
        self.snake.reset()
        
            
    def draw_grass(self):
        grass_color = (70, 127, 75)
        
        for row in range(cell_number):
            if row %2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,56, True, (240, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 7, apple_rect.height)
        
        pygame.draw.rect(screen, (0, 0, 0), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen, (100, 0, 0), bg_rect, 2)
        
              
pygame.init()
cell_size = 40
cell_number = 20
#display surface/ main game window with resolution (width, height)
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
#clock object for consistant game speed across instances and multiple devices
clock = pygame.time.Clock()

#imports an apple png from the project directory
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

game_font = pygame.font.Font(None,35)

# test_surface = pygame.Surface((100,200))
# test_surface.fill(pygame.Color(0, 0, 255))

#rectangle needs a (x, y, width, and height)

#center = (x, y)
# test_rect = test_surface.get_rect(center = (200, 250))


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

#never stops unless stopped from inside
while True:
    # event loop that looks for a quit event
    for event in pygame.event.get():
        #if the type of event is clicking the x to close window
        if event.type == pygame.QUIT:
            #opposite of pygame init to quit the code
            pygame.quit()
            #sometimes .quit() is not enough as parts of code can keep running
            #so use a system module to exit the code
            sys.exit()
        
        if event.type == SCREEN_UPDATE:
           main_game.update()
            
        if event.type == pygame.KEYDOWN:
            #move up
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: 
                 main_game.snake.direction = Vector2(0, -1)
            #move down
            if event.key == pygame.K_DOWN:
                 if main_game.snake.direction.y != -1: 
                     main_game.snake.direction = Vector2(0, +1)
            #move right
            if event.key == pygame.K_LEFT:
                 if main_game.snake.direction.x != 1: 
                    main_game.snake.direction = Vector2(-1, 0)
            
            if event.key == pygame.K_RIGHT:
                 if main_game.snake.direction.x != -1: 
                    main_game.snake.direction = Vector2(+1, 0)
    
    #fills screen with color (dark green)
    screen.fill((0, 50, 0))
    main_game.draw_element()
    
    #draw needs (surface, color, rectangle)
    #pygame.draw.ellipse(screen, pygame.Color('red'), test_rect)
    
    # test_rect.right += 1
    # screen.blit(test_surface, test_rect)
    
    
    #draw all game elements 
    pygame.display.update()
    #(Framerate) how fast game runs
    #while loop will never run faster than 60 fps
    clock.tick(60)