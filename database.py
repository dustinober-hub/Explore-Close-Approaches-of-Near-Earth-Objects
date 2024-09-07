"""
Near-Earth Object (NEO) Database Management.

This module provides a class, `NEODatabase`, to manage and query a collection of Near-Earth Objects (NEOs) and their close approaches to Earth.
The database maintains indices for quick look-up based on primary designation and name. It also provides functionalities to query close approaches
based on a set of filters and to retrieve NEOs by their designation or name.

The `NEODatabase` class is designed to:
- Store a collection of NEOs and their close approaches.
- Provide quick look-up capabilities for NEOs based on their primary designation or name.
- Allow querying of close approaches based on a set of filters.

Usage:
    db = NEODatabase(neos, approaches)
    neo_by_name = db.get_neo_by_name("Eros")
    neo_by_designation = db.get_neo_by_designation("433")
    hazardous_approaches = db.query(filters=[HazardousFilter(operator.eq, True)])
"""

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`."""
        self._neos = neos
        self._approaches = approaches

        # Auxiliary data structures for quick look-up
        self._designation_index = {neo.designation: neo for neo in neos}
        self._name_index = {neo.name: neo for neo in neos if neo.name}

        # Link NEOs and their close approaches
        for approach in approaches:
            neo = self._designation_index.get(approach._designation)
            if neo:
                approach.neo = neo
                neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation."""
        return self._designation_index.get(designation)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name."""
        return self._name_index.get(name)

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters."""
        for approach in self._approaches:
            if all(f(approach) for f in filters):
                yield approach
