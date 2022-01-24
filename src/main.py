from tkinter.tix import MAX
from unicodedata import name


class Gilded_Rose():
    
    # So items can be any type of data structure.
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    # This is just a normal item, no logic, just attributes.
    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class Interface():
    def update_quality(self):
        pass

class Normal_Item(Item, Interface):

    def __init__(self, name, sell_in, quality):
        Item.__init__(name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1
    
    def set_quality(self, value):
        MAX_QUALITY = 50

        if self.quality + value > MAX_QUALITY:
            self.quality = MAX_QUALITY
        elif self.quality + value >= 0:
            self.quality += value
        else:
            self.quality = 0

        ### ASSERT 
    
    def update_quality(self):
        if self.sell_in > 0:
            
    
