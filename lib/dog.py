#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        # Initialize attributes
        self.name = None
        self.breed = None

        # Validate and set name
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        elif name is not None:
            print("Name must be string between 1 and 25 characters.")

        # Validate and set breed
        if breed in APPROVED_BREEDS:
            self.breed = breed
        elif breed is not None:
            print("Breed must be in list of approved breeds.")
