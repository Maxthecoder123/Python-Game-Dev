import pgzrun
import random

TITLE = "Item drop"
WIDTH = 800
HEIGHT = 600

# Global Variables
items = ["battery","bottle","chips","plastic_bag"]
levels = 6
current_level = 1
speed = 10
game_over = False
game_complete = False
Final_Items = []
Animations = []

def draw():
    screen.blit("background",(0,0))
    if game_over:
        custom_message("Game Over","Try again!")
    elif game_complete:
        custom_message("You win!","Well done")
    else:
        for item in Final_Items:
            item.draw()

# Create a custom function to display the main heading and the sub heading
def custom_message(mainheading,subheading):
    screen.draw.text(mainheading,fontsize = 50, center = (400,300),color = "black")
    screen.draw.text(subheading,fontsize = 35, center = (400,350),color = "black")

# Create extra items based on the current level
def item_maker():
    global current_level, items
    Item_Maker_List = ["paper_bag"]
    for i in range(0,current_level):
        random_item = random.choice(items)
        Item_Maker_List.append(random_item)
    return Item_Maker_List # Contains a list of item names for each level

# Convert items into actors
def item_converter(Item_Maker_List):
    item_converter_list = []
    for item in Item_Maker_List:
        item_actor = Actor(item)
        item_converter_list.append(item_actor)
    return item_converter_list # Contain a list of actors

# Arrange the actors on screen
def arrange_actors(item_converter_list):
    gap_number = len(item_converter_list)+1
    gap_size = WIDTH/gap_number
    random.shuffle(item_converter_list)
    for i,objects in enumerate(item_converter_list):
        x = (i+1)*gap_size
        objects.x = x



# Animate the actors to move down
def animation(item_converter_list):
    global speed,current_level,HEIGHT,Animations
    for item in item_converter_list:
        duration = speed - current_level
        item.anchor = ("center","bottom")
        item_animaton = animate(item, duration = duration, on_finished=handle_game_over, y=HEIGHT)
        Animations.append(item_animaton)

# Changes the game state to game over or game complete
def handle_game_over():
    global game_over
    game_over = True

    

def handle_game_complete():
    global game_complete,Final_Items,Animations,levels,current_level
    stop_animation(Animations)
    if current_level == levels:
        game_complete = True
    else:
        current_level +=1
        Final_Items = []
        Animations = []

    
# Display the actors on the screen
def display_actors():
    Item_Maker_List = item_maker()
    item_converter_list = item_converter(Item_Maker_List)
    arrange_actors(item_converter_list)
    animation(item_converter_list)
    return item_converter_list

# Predefined function that updates the games every frame
def update():
    global Final_Items
    if len(Final_Items) == 0:
        Final_Items = display_actors()

# Predefined function that checks if you have clicked something
def on_mouse_down(pos):
    global Final_Items
    for item in Final_Items:
        if item.collidepoint(pos):
            if "paper_bag" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def stop_animation(Animations):
    for animation in Animations:
        if animation.running:
            animation.stop()

pgzrun.go()