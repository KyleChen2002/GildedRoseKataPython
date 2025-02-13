import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_conjured_item_degrades_by_2_before_expiration(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(
            items[0].quality, 
            8
        )

    def test_conjured_item_degrades_by_4_after_expiration(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(
            items[0].quality, 
            6
        )

    def test_conjured_item_quality_cannot_be_negative_before_expiration(self):
        items = [Item("Conjured Mana Cake", 5, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(
            items[0].quality, 
            0
        )

    def test_conjured_item_quality_cannot_be_negative_after_expiration(self):
        items = [Item("Conjured Mana Cake", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(
            items[0].quality, 
            0
        )
    
    def test_update_conjured_item_not_below_zero(self):
        item = Item("Conjured Mana Cake", 1, 1)
        gilded_rose = GildedRose([item])
        gilded_rose.update_conjured_item(item)
        self.assertEqual(item.quality, 0)
        self.assertEqual(item.sell_in, 0)




if __name__ == '__main__':
    unittest.main()
