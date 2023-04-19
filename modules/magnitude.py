from math import pi

def surface(r):
    return r**2

def volume(r):
    return r**3

def sphere_surface_area(r):
    return 4*pi*r**2

def sphere_volume(r):
    return (4/3)*pi*r**3

def volume_to_surface(r):
    return (1/3)*r