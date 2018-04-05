import unittest
import toyRobot

class TestRobot(unittest.TestCase):

    def test_toy(self):
        self.assertEqual(toyRobot.toy("PLACE 0,0,NORTH MOVE REPORT"), True)
        self.assertEqual(toyRobot.toy("PLACE 0,0,NORTH LEFT REPORT"), True)
        self.assertEqual(toyRobot.toy("PLACE 1,2,EAST MOVE LEFT MOVE REPORT"), True)
        self.assertEqual(toyRobot.toy("PLACE 5,0,NORTH MOVE REPORT"), False)
        self.assertEqual(toyRobot.toy("PLACE 0,6,NORTH RIGHT REPORT"), False)
        self.assertEqual(toyRobot.toy("PLACE 5,5,EAST MOVE MOVE LEFT MOVE REPORT"), False)

    def test_move(self):
        self.assertRaises(TypeError, toyRobot.move, '3', 2, 1)
        self.assertRaises(TypeError, toyRobot.move, '3', '2', 1)

if(__name__ == '__main__'):
    unittest.main()
