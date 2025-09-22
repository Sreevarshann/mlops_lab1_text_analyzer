from src.converter import *

def test_to_celsius():
    assert round(to_celsius(32), 2) == 0
    assert round(to_celsius(212), 2) == 100

def test_to_fahrenheit():
    assert round(to_fahrenheit(0), 2) == 32
    assert round(to_fahrenheit(100), 2) == 212

def test_kelvin_to_celsius():
    assert round(kelvin_to_celsius(273.15), 2) == 0
    assert round(kelvin_to_celsius(373.15), 2) == 100

def test_celsius_to_kelvin():
    assert round(celsius_to_kelvin(0), 2) == 273.15
    assert round(celsius_to_kelvin(100), 2) == 373.15
