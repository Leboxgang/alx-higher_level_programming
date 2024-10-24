#!/usr/bin/python3
"""Contains the class "Student"."""

class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance
        with specified attributes."""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            if a in self.__dict__:
                new_dict[a] = self.__dict__[a]
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
