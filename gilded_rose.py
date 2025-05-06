# -*- coding: utf-8 -*-

class GildedRose(object):

    # Items
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

    # Sell in levels
    SELL_IN_ZERO = 0
    DEFAULT_DEGRADE_SELL_IN = 1

    # Quality levels
    DEFAULT_DEGRADE_QUALITY = 1
    DOUBLE_DEFAULT_DEGRADE_QUALITY = DEFAULT_DEGRADE_QUALITY * 2
    DEFAULT_MIN_QUALITY = 0
    DEFAULT_MAX_QUALITY = 50
    SULFURAS_QUALITY = 80
    BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY = 2
    BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY = 3
    BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY_SELL_IN = 10
    BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY_SELL_IN = 5

    def __init__(self, items):
        self.items = items

    def _update_quality_aged_brie_and_backstage_passes(self, item):
      if item.quality < self.DEFAULT_MAX_QUALITY:
        item.quality = item.quality + self.DEFAULT_DEGRADE_QUALITY
        if item.name == self.BACKSTAGE_PASSES:
          if item.sell_in <= self.BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY_SELL_IN:
            if item.quality < self.DEFAULT_MAX_QUALITY:
              item.quality = item.quality + self.DEFAULT_DEGRADE_QUALITY
            if item.sell_in <= self.BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY_SELL_IN:
              if item.quality < self.DEFAULT_MAX_QUALITY:
                item.quality = item.quality + self.DEFAULT_DEGRADE_QUALITY
    
    def _update_quality_all(self, item):
      if item.quality > self.DEFAULT_MIN_QUALITY:
        if item.name != self.SULFURAS:
          item.quality = item.quality - self.DEFAULT_DEGRADE_QUALITY
    
    def _update_quality_nagative_sell_in(self, item):
      if item.quality > self.DEFAULT_MIN_QUALITY:
        item.quality = item.quality - self.DEFAULT_DEGRADE_QUALITY
    
    def _update_sulfuras_item(self, item):
      self._update_quality_all(item)
    
    def _degrade_sell_in(self, item):
      item.sell_in = item.sell_in - self.DEFAULT_DEGRADE_SELL_IN
    
    def _update_age_brie_item(self, item):
      self._update_quality_aged_brie_and_backstage_passes(item)
      self._degrade_sell_in(item)
      if item.sell_in < self.SELL_IN_ZERO:
        if item.quality < self.DEFAULT_MAX_QUALITY:
          item.quality = item.quality + self.DEFAULT_DEGRADE_QUALITY
    
    def _update_backstage_passes_item(self, item):
      self._update_quality_aged_brie_and_backstage_passes(item)
      self._degrade_sell_in(item)
      if item.sell_in < self.SELL_IN_ZERO:
        item.quality = self.DEFAULT_MIN_QUALITY
    
    def _update_item_quality(self, item):
      if item.name == self.SULFURAS:
        self._update_sulfuras_item(item)
        return
      
      if item.name == self.AGED_BRIE:
        self._update_age_brie_item(item)
        return
      
      if item.name == self.BACKSTAGE_PASSES:
        self._update_backstage_passes_item(item)
        return
        
      self._update_quality_all(item)
      self._degrade_sell_in(item)
      if item.sell_in < self.SELL_IN_ZERO:
        self._update_quality_nagative_sell_in(item)

    def update_quality(self):
      for item in self.items:
        self._update_item_quality(item)


                


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
