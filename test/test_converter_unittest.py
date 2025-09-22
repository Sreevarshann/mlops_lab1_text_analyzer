import unittest
from src.converter import *

class TestConverter(unittest.TestCase):
    def test_to_celsius(self):
        self.assertEqual(round(to_celsius(32), 2), 0)
        self.assertEqual(round(to_celsius(212), 2), 100)

    def test_to_fahrenheit(self):
        self.assertEqual(round(to_fahrenheit(0), 2), 32)
        self.assertEqual(round(to_fahrenheit(100), 2), 212)

    def test_kelvin_to_celsius(self):
        self.assertEqual(round(kelvin_to_celsius(273.15), 2), 0)
        self.assertEqual(round(kelvin_to_celsius(373.15), 2), 100)

    def test_celsius_to_kelvin(self):
        self.assertEqual(round(celsius_to_kelvin(0), 2), 273.15)
        self.assertEqual(round(celsius_to_kelvin(100), 2), 373.15)

if __name__ == "__main__":
    unittest.main()
