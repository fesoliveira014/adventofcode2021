from enum import Enum
from typing import Match

class Direction(Enum):
    FORWARD = 1
    UP = 2
    DOWN = 3

    @staticmethod
    def from_str(direction: str):
        direction = direction.upper()
        return Direction[direction]

class Command:
    def __init__(self, direction, value):
        self.direction = Direction.from_str(direction)
        self.value = int(value)

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.commands = []

    def parse_commands(self, commands):
        for line in commands:
            tokens = line.split(' ')
            command = Command(tokens[0], tokens[1])
            self.commands.append(command)
    
    def calculate_final_position(self):
        for command in self.commands:
            if command.direction == Direction.FORWARD:
                self.x += command.value
            elif command.direction == Direction.UP:
                self.y -= command.value
            elif command.direction == Direction.DOWN:
                self.y += command.value
    
if __name__ == "__main__":
    commands = []
    with open("input/01.txt", 'r') as f:
        for line in f:
            commands.append(line.strip('\n'))
    ship = Ship()
    ship.parse_commands(commands)
    ship.calculate_final_position()
    print("{}".format(ship.x * ship.y))