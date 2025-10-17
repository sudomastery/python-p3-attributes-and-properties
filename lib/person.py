#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # Initialize attributes
        self.name = None
        self.job = None

        # Validate and set name (title-cased on save)
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name.title()
        elif name is not None:
            print("Name must be string between 1 and 25 characters.")

        # Validate and set job
        if job in APPROVED_JOBS:
            self.job = job
        elif job is not None:
            print("Job must be in list of approved jobs.")
