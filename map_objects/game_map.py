import tcod as libtcod
from random import randint

from components.ai import BasicMonster
from components.fighter import Fighter
from components.item import Item

from entity import Entity

from game_messages import Message

from item_functions import cast_confuse, cast_fireball, cast_lightning, heal

from map_objects.rectangle import Rect
from map_objects.tile import Tile

from render_functions import RenderOrder


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        for i in range(0, 5):
            self.tiles = self.initialize_tiles()
        
    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_circle(self, y=3):
 
        #painfully draw a circle
        for x in range(17, 23):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
            
        for x in range(14, 26):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(11, 29):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(10, 30):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(9, 31):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(8, 32):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(7, 33):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(6, 34):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(3, 37):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1

        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(4, 36):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(5, 35):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(6, 34):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(7, 33):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(8, 32):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(9, 31):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(10, 30):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(11, 29):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(14, 26):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1
        
        for x in range(17, 23):
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].blocked = False
        y += 1

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities,
                 max_monsters_per_room, max_items_per_room):
       
        self.make_circle(y=3)
                    
        self.place_entities(0, entities, max_monsters_per_room, max_items_per_room)
       
        player.x = 21
        player.y = 21
        
    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities, max_monsters_per_room, max_items_per_room):
        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)

        # Get a random number of items
        number_of_items = randint(0, max_items_per_room)

        for i in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(8,32)
            y = randint(7,31)

            # Check if an entity is already in that location
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                if randint(0, 100) < 80:
                    fighter_component = Fighter(hp=10, defense=0, power=3)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 4, 'o', libtcod.yellow, 'Orc', blocks=True,
                                     render_order=RenderOrder.ACTOR, strength=4, fighter=fighter_component, ai=ai_component)
                else:
                    fighter_component = Fighter(hp=16, defense=1, power=4)
                    ai_component = BasicMonster()

                    monster = Entity(x, y, 4, 'T', libtcod.cyan, 'Troll', blocks=True, fighter=fighter_component,
                                     render_order=RenderOrder.ACTOR, strength=10, ai=ai_component)

                entities.append(monster)

        '''
        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_chance = randint(0, 100)

                if item_chance < 70:
                    item_component = Item(use_function=heal, amount=4)
                    item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
                                  item=item_component)
                elif item_chance < 80:
                    item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message(
                        'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan),
                                          damage=12, radius=3)
                    item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
                                  item=item_component)
                elif item_chance < 90:
                    item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message(
                        'Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
                    item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM,
                                  item=item_component)
                else:
                    item_component = Item(use_function=cast_lightning, damage=20, maximum_range=5)
                    item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM,
                                  item=item_component)

                entities.append(item)
        ''' 
        
    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
