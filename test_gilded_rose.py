# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

# Items
ITEM = "foo"

class GildedRoseTest(unittest.TestCase):
  def test_update_quality_lowers_item_values(self):
    """Test for 'Requirement: At the end of each day our system lowers both values for every item'"""
    starting_sell_in = 1
    starting_quality = GildedRose.DEFAULT_MAX_QUALITY
    item = Item(ITEM, starting_sell_in, starting_quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(ITEM, item.name)
    # Check that both item's sell_in and quality values have been decremented by defaults
    self.assertEqual(item.sell_in, starting_sell_in - GildedRose.DEFAULT_DEGRADE_SELL_IN)
    self.assertEqual(item.quality, starting_quality - GildedRose.DEFAULT_DEGRADE_QUALITY)

  def test_update_quality_sell_by_date_passed(self):
    """Test for 'Requirement: Once the sell by date has passed, `Quality` degrades twice as fast'"""
    starting_sell_in = GildedRose.SELL_IN_ZERO
    starting_quality = GildedRose.DEFAULT_DEGRADE_QUALITY * 2
    item = Item(ITEM, starting_sell_in, starting_quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(ITEM, item.name)
    # Check that item's sell_in value has been decremented by default value
    self.assertEqual(item.sell_in, starting_sell_in - GildedRose.DEFAULT_DEGRADE_SELL_IN)
    # Check that item's quality value has been decremented by double default value
    self.assertEqual(item.quality, starting_quality - GildedRose.DEFAULT_DEGRADE_QUALITY * 2)
  
  def test_update_quality_is_never_negative(self):
    """Test for 'Requirement: The Quality of an item is never negative'"""
    starting_sell_in = GildedRose.SELL_IN_ZERO
    starting_quality = GildedRose.DEFAULT_MIN_QUALITY
    item = Item(ITEM, starting_sell_in, starting_quality)
    # Ensure that item's quality value started at default min
    self.assertEqual(item.quality, GildedRose.DEFAULT_MIN_QUALITY)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(ITEM, item.name)
    # Check that item's sell_in value has been decremented by default
    self.assertEqual(item.sell_in, starting_sell_in - GildedRose.DEFAULT_DEGRADE_SELL_IN)
    # Check that item's quality value has stayed at default min
    self.assertEqual(item.quality, GildedRose.DEFAULT_MIN_QUALITY)

  def test_update_quality_aged_brie_increases_quality(self):
    """Test for 'Requirement: "Aged Brie" actually increases in Quality the older it gets'
    - Once the sell by date has passed, `Quality` degrades twice as fast
    """
    for days_left in [1, 0]:
      with self.subTest(days_left=days_left):
        starting_quality = GildedRose.DEFAULT_MIN_QUALITY
        item = Item(GildedRose.AGED_BRIE, days_left, starting_quality)
        gilded_rose = GildedRose((item,))
        gilded_rose.update_quality()
        if days_left == 1:
          # Check item has the expected state
          self.assertEqual(GildedRose.AGED_BRIE, item.name)
          # Check that item's sell_in value has been decremented by default
          self.assertEqual(item.sell_in, days_left - GildedRose.DEFAULT_DEGRADE_SELL_IN)
          # Check that item's quality value has also increased by default
          self.assertEqual(item.quality, starting_quality + GildedRose.DEFAULT_DEGRADE_QUALITY)
        elif days_left == 0:
          # Check item has the expected state
          self.assertEqual(GildedRose.AGED_BRIE, item.name)
          # Check that item's sell_in value has been decremented by default
          self.assertEqual(item.sell_in, days_left - GildedRose.DEFAULT_DEGRADE_SELL_IN)
          # Check that item's quality value has also increased by double the default
          self.assertEqual(item.quality, starting_quality + GildedRose.DEFAULT_DEGRADE_QUALITY * 2)
  
  def test_update_quality_max_quality(self):
    """Test for 'Requirement: The Quality of an item is never more than 50'"""
    starting_sell_in = GildedRose.SELL_IN_ZERO
    starting_quality = GildedRose.DEFAULT_MAX_QUALITY
    item = Item(GildedRose.AGED_BRIE, starting_sell_in, starting_quality)
    # Ensure starting_quality is at default max value
    self.assertEqual(item.quality, GildedRose.DEFAULT_MAX_QUALITY)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(GildedRose.AGED_BRIE, item.name)
    # Check that item's sell_in value has been decremented by default
    self.assertEqual(item.sell_in, starting_sell_in - GildedRose.DEFAULT_DEGRADE_SELL_IN)
    # Check that item's quality value has stayed at default max
    self.assertEqual(item.quality, GildedRose.DEFAULT_MAX_QUALITY)

  def test_update_quality_sulfuras(self):
    """Test for 'Requirement: "Sulfuras", being a legendary item, never has to be sold or decreases in Quality, its Quality is 80 and it never alters.'"""
    starting_sell_in = GildedRose.SELL_IN_ZERO
    starting_quality = GildedRose.SULFURAS_QUALITY
    item = Item(GildedRose.SULFURAS, starting_sell_in, starting_quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(GildedRose.SULFURAS, item.name)
    # Check that item's sell_in and quality values have not changed
    self.assertEqual(item.sell_in, starting_sell_in)
    self.assertEqual(item.quality, GildedRose.SULFURAS_QUALITY)

  def test_update_quality_backstage_passes_quality(self):
    """Test for 'Requirement: Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;'
    - Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    - Quality drops to 0 after the concert
    """
    starting_sell_in = GildedRose.SELL_IN_ZERO
    for days_left in list(reversed(range(starting_sell_in, GildedRose.BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY_SELL_IN + 1))):
      with self.subTest(days_left=days_left):
        starting_quality = 1
        item = Item(GildedRose.BACKSTAGE_PASSES, days_left, starting_quality)
        gilded_rose = GildedRose((item,))
        gilded_rose.update_quality()
        if GildedRose.BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY_SELL_IN < days_left <= GildedRose.BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY_SELL_IN:
          # - Quality increases by 2 when there are 10 days or less
          # Check item has the expected state
          self.assertEqual(GildedRose.BACKSTAGE_PASSES, item.name)
          # Check that item's sell_in value has been decremented by default value
          self.assertEqual(item.sell_in, days_left - GildedRose.DEFAULT_DEGRADE_SELL_IN)
          # Check that item's quality value has been incremented by default value
          self.assertEqual(item.quality, starting_quality + GildedRose.BACKSTAGE_PASSES_LOW_DEGRADE_QUALITY)
        elif 0 < days_left <= GildedRose.BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY_SELL_IN:
          # - Quality increases by 3 when there are 5 days or less
          # Check item has the expected state
          self.assertEqual(GildedRose.BACKSTAGE_PASSES, item.name)
          # Check that item's sell_in value has been decremented by default value
          self.assertEqual(item.sell_in, days_left - GildedRose.DEFAULT_DEGRADE_SELL_IN)
          # Check that item's quality value has been incremented by default value
          self.assertEqual(item.quality, starting_quality + GildedRose.BACKSTAGE_PASSES_HIGH_DEGRADE_QUALITY)
        else:
          # - Quality drops to 0 after the concert
          # Check item has the expected state
          self.assertEqual(GildedRose.BACKSTAGE_PASSES, item.name)
          # Check that item's sell_in value has been decremented by default value
          self.assertEqual(item.sell_in, days_left - GildedRose.DEFAULT_DEGRADE_SELL_IN)
          # Check that item's sell_in value has decremented under starting_sell_in value of 0
          self.assertLess(item.sell_in, starting_sell_in)
          # Check that item's quality value has dropped to default min
          self.assertEqual(item.quality, GildedRose.DEFAULT_MIN_QUALITY)

  def test_update_quality_conjured(self):
    """Test for 'New Requirement: "Conjured" items degrade in Quality twice as fast as normal items'"""
    starting_sell_in = 1
    starting_quality = GildedRose.DEFAULT_MAX_QUALITY
    item = Item(GildedRose.CONJURED, starting_sell_in, starting_quality)
    gilded_rose = GildedRose((item,))
    gilded_rose.update_quality()
    # Check item has the expected state
    self.assertEqual(GildedRose.CONJURED, item.name)
    # Check that the item's sell_in value has been decremented by defaults
    self.assertEqual(item.sell_in, starting_sell_in - GildedRose.DEFAULT_DEGRADE_SELL_IN)
    # Check that the item's quality value has been decremented twice as fast as default
    self.assertEqual(item.quality, starting_quality - GildedRose.DEFAULT_DEGRADE_QUALITY * 2)

class ItemTest(unittest.TestCase):
  def test_repr(self):
    starting_sell_in = GildedRose.SELL_IN_ZERO
    starting_quality = GildedRose.DEFAULT_MIN_QUALITY
    item = Item(ITEM, starting_sell_in, starting_quality)
    self.assertEqual(repr(item), "%s, %s, %s" % (ITEM, starting_sell_in, starting_quality))

if __name__ == '__main__':
    unittest.main()
