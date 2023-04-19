import unittest
from math import pi
from modules.magnitude import surface, volume, sphere_surface_area, sphere_volume, volume_to_surface

class TestFunctions(unittest.TestCase):
    def test_surface(self):
        self.assertEqual(surface(2), 4)
        self.assertEqual(surface(3), 9)
        self.assertEqual(surface(4.5), 20.25)
        
    def test_volume(self):
        self.assertEqual(volume(2), 8)
        self.assertEqual(volume(3), 27)
        self.assertEqual(volume(4.5), 91.125)
        
    def test_sphere_surface_area(self):
        self.assertAlmostEqual(sphere_surface_area(2), 4*pi*2**2, places=5)
        self.assertAlmostEqual(sphere_surface_area(3), 4*pi*3**2, places=5)
        self.assertAlmostEqual(sphere_surface_area(4.5), 4*pi*4.5**2, places=5)
        
    def test_sphere_volume(self):
        self.assertAlmostEqual(sphere_volume(2), (4/3)*pi*2**3, places=5)
        self.assertAlmostEqual(sphere_volume(3), (4/3)*pi*3**3, places=5)
        self.assertAlmostEqual(sphere_volume(4.5), (4/3)*pi*4.5**3, places=5)
        
    def test_volume_to_surface(self):
        self.assertAlmostEqual(volume_to_surface(2), (1/3)*2, places=5)
        self.assertAlmostEqual(volume_to_surface(3), (1/3)*3, places=5)
        self.assertAlmostEqual(volume_to_surface(4.5), (1/3)*4.5, places=5)
        
if __name__ == '__main__':
    unittest.main()
