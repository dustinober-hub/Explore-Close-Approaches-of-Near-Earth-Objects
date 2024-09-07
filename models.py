"""
Module for representing and managing near-Earth objects (NEOs) and their close approaches to Earth.

This module provides classes to represent individual NEOs (`NearEarthObject`) and their close approaches to Earth (`CloseApproach`). Each `NearEarthObject` maintains a collection of its close approaches, and each `CloseApproach` maintains a reference to its associated NEO.

The `NearEarthObject` class encapsulates the semantic and physical parameters of the NEO, such as its designation, name, diameter, and potential hazard status. The `CloseApproach` class encapsulates the details of the approach, including the time, distance, and relative velocity.

Utility functions from the `helpers` module are used to convert between different time representations.

Typical usage:

    neo = NearEarthObject(designation="2020 AB", name="Asteroid 2020 AB", diameter=0.512, hazardous=True)
    approach = CloseApproach(designation="2020 AB", time="2020-Jan-01 00:00", distance=0.025, velocity=25.2)
    approach.neo = neo
    neo.approaches.append(approach)
"""

from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """
    Represents a near-Earth object (NEO) with its properties and close approaches.

    An NEO is an asteroid or comet with a perihelion distance less than 1.3 astronomical units from the Earth.
    This class encapsulates the semantic and physical parameters of the NEO, such as its designation, name, diameter, and potential hazard status.
    """

    def __init__(self, designation='', name=None, diameter=float('nan'), hazardous=False):
        """
        Initialize a new NearEarthObject.

        :param designation: The unique identifier for this NEO.
        :param name: The IAU name for this NEO (optional).
        :param diameter: The diameter of the NEO in kilometers (optional).
        :param hazardous: A boolean indicating if the NEO is potentially hazardous.
        """
        self.designation = designation
        self.name = name if name else None
        self.diameter = float(diameter) if diameter else float('nan')
        self.hazardous = hazardous
        self.approaches = []

    @property
    def fullname(self):
        """Return the full name of the NEO, combining its designation and name."""
        if self.name:
            return f"{self.designation} ({self.name})"
        return self.designation

    def __str__(self):
        """Return a human-readable string representation of the NEO."""
        return (f"A NearEarthObject with designation {self.designation}, name {self.name}, "
                f"diameter {self.diameter:.3f} km, and hazardous: {self.hazardous}")

    def __repr__(self):
        """Return a string representation of this object for debugging purposes."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """
    Represents a close approach of an NEO to Earth.

    This class encapsulates the details of the approach, including the time, distance, and relative velocity.
    It also maintains a reference to the associated NEO.
    """

    def __init__(self, designation='', time=None, distance=0.0, velocity=0.0):
        """
        Initialize a new CloseApproach.

        :param designation: The unique identifier of the NEO.
        :param time: The date and time, in UTC, at which the NEO approaches Earth.
        :param distance: The nominal approach distance in astronomical units.
        :param velocity: The relative approach velocity in kilometers per second.
        """
        self._designation = designation
        self.time = cd_to_datetime(time) if time else None
        self.distance = float(distance)
        self.velocity = float(velocity)
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted string representation of the approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return a human-readable string representation of the close approach."""
        return (f"A CloseApproach at {self.time_str}, distance {self.distance:.2f} AU, "
                f"velocity {self.velocity:.2f} km/s, related NEO: {self.neo.fullname}")

    def __repr__(self):
        """Return a string representation of this object for debugging purposes."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
