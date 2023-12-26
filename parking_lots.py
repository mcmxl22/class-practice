#!/usr/bin/env python3
"""
parking_lots.py Version 1
Author: M McConnaughey
10/21/2023
Python 3.7
"""

class Parking_lot:
    """Define a parking lot class"""
    def __init__(self):
        self.is_active = True

    def set_status(self, state):
        self.is_active = state
    
    def get_status(self):
        return self.is_active


class Vehicle:
    """Define a vehicle class"""
    def __init__(self):
        self.is_type = 'car'

    def set_type(self, vehicle_type):
        predefined_types = ['car', 'truck']

        try:
            self.is_type = vehicle_type
        except ValueError:
            print(f'This lot only accepts {predefined_types}.')

    def get_type(self):
        return self.vehicle_type

    def set_status(self):
        pass

    def get_status(self):
        pass


class Parking_Space:
    """Define a parking space class"""
    def __init__(self, vehicle):
        self.vehicle = None

    def park_vehicle(self):
        self.vehicle = vehicle
