import unittest

import circle
import square

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_fractional(self):
        res = circle.area(2.5)
        self.assertAlmostEqual(res, 19.634954084936208)

    def test_area_large(self):
        res = circle.area(1000)
        self.assertAlmostEqual(res, 3141592.653589793)

    def test_perimeter(self):
        res = circle.perimeter(2)
        self.assertAlmostEqual(res, 12.566370614359172)

    def test_perimenter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_fractional(self):
        res = circle.perimeter(2.5)
        self.assertAlmostEqual(res, 15.707963267948966)

    def test_perimeter_large(self):
        res = circle.perimeter(1000)
        self.assertAlmostEqual(res, 6283.185307179586)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_fractional(self):
        res = square.area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_large(self):
        res = square.area(1000)
        self.assertEqual(res, 1000000)

    def test_perimeter(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_fractional(self):
        res = square.perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_large(self):
        res = square.perimeter(1000)
        self.assertEqual(res, 4000)