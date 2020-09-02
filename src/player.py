# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap

class Player:
    def __init__(self, location):
        self.location = location
    
    def __str__(self):
        return f'You are currently at {self.location.name}\n\n{textwrap.fill(self.location.description, width=40)}\n'