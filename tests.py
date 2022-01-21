#!/usr/bin/env python3
from unittest import TestCase
from script import move

# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_raises_warning_gamestate(self):
        # Wrong Type state
        with self.assertRaises(Exception): move(["###"," o "], "right")
        with self.assertRaises(Exception): move("###", "right")
        with self.assertRaises(Exception): move(420.0, "right")
        # Wrong Type line
        with self.assertRaises(Exception): move(("##o ",[" ", "#", " ", "#"]), "right")
        with self.assertRaises(Exception): move(("##o ",(" ", "#", " ", "#")), "right")
        with self.assertRaises(Exception): move(("##o ",4578), "right")
        # Empty state/line
        with self.assertRaises(Exception): move((), "right")
        with self.assertRaises(Exception): move(("",), "right")
        with self.assertRaises(Exception): move(("  o ",""), "right")
        # Same Line length
        with self.assertRaises(Exception): move(("##o ","###"), "right")
        with self.assertRaises(Exception): move((" #o","###", "## #"), "right")
        with self.assertRaises(Exception): move(("##o ","## ", " # #"), "right")
        # Invalid Chars
        with self.assertRaises(Exception): move(("a#o ","## #"), "right")
        with self.assertRaises(Exception): move(("##o ","#0 #"), "right")
        with self.assertRaises(Exception): move(("##o ","#[ #"), "right")
        # Player count
        with self.assertRaises(Exception): move((" #o ","#o #"), "right")
        with self.assertRaises(Exception): move((" #  ","## #"), "right")
        with self.assertRaises(Exception): move((" #oo","## #"), "right")
        # No Possible Movements
        with self.assertRaises(Exception): move((" ###","##o#"), "right")
        with self.assertRaises(Exception): move(("o###","##  "), "right")
        with self.assertRaises(Exception): move((" #  ","#o# ", " #  "), "right")
    
    def test_raises_warning_direction(self):
        # Wrong Type direction
        with self.assertRaises(Exception): move(("o ##"," # #"), ["right"])
        with self.assertRaises(Exception): move(("o ##"," # #"), ("right",))
        with self.assertRaises(Exception): move(("o ##"," # #"), 234)
        # Invalid direction
        with self.assertRaises(Exception): move(("o ##"," # #"), "Right")
        with self.assertRaises(Exception): move(("o ##"," # #"), " ")
        with self.assertRaises(Exception): move(("o ##"," # #"), "")
        # Obstructed direction
        with self.assertRaises(Exception): move((" #  "," #o "), "left")
        with self.assertRaises(Exception): move((" #  "," o #"), "up")
        with self.assertRaises(Exception): move((" # o","# # "), "right")
        with self.assertRaises(Exception): move(("# # "," o #"), "down")
        with self.assertRaises(Exception): move((" ## ","o  #"), "left")
        with self.assertRaises(Exception): move(("# o ","#  #"), "up")
    
    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)
        self.assertEqual((
            (
                "#####   ",
                "###  # #",
                "#    o #",
                "   ## ##"
            ),
            ("down", "left", "right")), 
            move((
            "#####   ",
            "###  # #",
            "#   o  #",
            "   ## ##"), 
            "right"))

    def test_move_up(self):
        # this test case WAS buggy
        state = (
            "####    ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "####    ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right", "up")
        )
        self.assertEqual(expected, actual)
        self.assertEqual((
            (
                "#####   ",
                "####o###",
                "#     ##",
                "   #####"
            ),
            ("down",)), 
            move((
                "#####   ",
                "#### ###",
                "#   o ##",
                "   #####"
            ), 
            "up"))

    def test_move_down(self):
        self.assertEqual((
            (
                "#####   ",
                "#### ###",
                "#     ##",
                "   #o###"
            ),
            ("up",)), 
            move((
                "#####   ",
                "#### ###",
                "#   o ##",
                "   # ###"
            ), 
            "down"))
        self.assertEqual((
            (
                "#####   ",
                "###  ###",
                "#  o  ##",
                "     ###"
            ),
            ("down","left", "right", "up")), 
            move((
                "#####   ",
                "###o ###",
                "#     ##",
                "     ###"
            ), 
            "down"))
    
    def test_move_left(self):
        self.assertEqual((
            (
                "#####   ",
                "########",
                "###o ###",
                "  ######"
            ),
            ("right",)), 
            move((
                "#####   ",
                "########",
                "### o###",
                "  ######"
            ), 
            "left"))
        self.assertEqual((
            (
                "#####   ",
                "##   ###",
                "#  o  ##",
                "     ###"
            ),
            ("down", "left", "right", "up")), 
            move((
                "#####   ",
                "##   ###",
                "#   o ##",
                "     ###"
            ), 
            "left"))