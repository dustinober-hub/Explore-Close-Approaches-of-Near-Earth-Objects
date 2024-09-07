"""
Module for filtering close approaches based on various attributes.

This module provides a set of filters to apply on close approaches of near-Earth objects (NEOs). Each filter is represented as a class that can be invoked to determine if a given close approach matches the filter criteria. The module supports filtering by date, distance, velocity, diameter, and hazardous status of the NEO.

Typical usage involves creating a set of filters using the `create_filters` function and then applying these filters to a collection of close approaches.

Example:
    filters = create_filters(date=date(2020, 1, 1), hazardous=True)
    filtered_approaches = [approach for approach in approaches if all(f(approach) for f in filters)]
"""
import operator

class UnsupportedCriterionError(NotImplementedError):
    """Raised when a filter criterion is not supported."""

class AttributeFilter:
    """
    A superclass for filters on comparable attributes of close approaches.

    This class represents a general filter that can be applied to any attribute of a close approach.
    Subclasses should override the `get` method to fetch the specific attribute they're designed to filter.
    """

    def __init__(self, op, value):
        """
        Initialize a new AttributeFilter.

        :param op: A binary predicate comparator (e.g., operator.le).
        :param value: The reference value to compare against.
        """
        self.op = op
        self.value = value

    def __call__(self, approach):
        """
        Evaluate the filter on a given close approach.

        :param approach: A `CloseApproach` to evaluate.
        :return: True if the close approach matches the filter, False otherwise.
        """
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """
        Fetch the attribute of interest from the given close approach.

        This method should be overridden by subclasses to get the specific attribute they filter.

        :param approach: A `CloseApproach` to fetch the attribute from.
        :return: The value of the attribute of interest.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        """Return a developer-friendly string representation of the filter."""
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"

class DateFilter(AttributeFilter):
    """Filter close approaches based on the date of approach."""

    @classmethod
    def get(cls, approach):
        """Fetch the date of the close approach."""
        return approach.time.date()

class DistanceFilter(AttributeFilter):
    """Filter close approaches based on the distance of approach."""

    @classmethod
    def get(cls, approach):
        """Fetch the distance of the close approach."""
        return approach.distance

class VelocityFilter(AttributeFilter):
    """Filter close approaches based on the velocity of approach."""
    
    @classmethod
    def get(cls, approach):
        """Fetch the velocity of the close approach."""
        return approach.velocity

class DiameterFilter(AttributeFilter):
    """Filter close approaches based on the diameter of the NEO."""

    @classmethod
    def get(cls, approach):
        """Fetch the diameter of the NEO associated with the close approach."""
        return approach.neo.diameter

class HazardousFilter(AttributeFilter):
    """Filter close approaches based on the hazardous status of the NEO."""
    
    @classmethod
    def get(cls, approach):
        """Fetch the hazardous status of the NEO associated with the close approach."""
        return approach.neo.hazardous

def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    """
    Create a collection of filters based on user-specified criteria.

    :param date: Exact date of the close approach.
    :param start_date: Start date for filtering close approaches.
    :param end_date: End date for filtering close approaches.
    :param distance_min: Minimum distance for filtering close approaches.
    :param distance_max: Maximum distance for filtering close approaches.
    :param velocity_min: Minimum velocity for filtering close approaches.
    :param velocity_max: Maximum velocity for filtering close approaches.
    :param diameter_min: Minimum diameter of the NEO for filtering close approaches.
    :param diameter_max: Maximum diameter of the NEO for filtering close approaches.
    :param hazardous: Hazardous status of the NEO for filtering close approaches.
    :return: A tuple of filters for use with querying close approaches.
    """
    filters = []

    if date:
        filters.append(DateFilter(operator.eq, date))
    if start_date:
        filters.append(DateFilter(operator.ge, start_date))
    if end_date:
        filters.append(DateFilter(operator.le, end_date))
    if distance_min:
        filters.append(DistanceFilter(operator.ge, distance_min))
    if distance_max:
        filters.append(DistanceFilter(operator.le, distance_max))
    if velocity_min:
        filters.append(VelocityFilter(operator.ge, velocity_min))
    if velocity_max:
        filters.append(VelocityFilter(operator.le, velocity_max))
    if diameter_min:
        filters.append(DiameterFilter(operator.ge, diameter_min))
    if diameter_max:
        filters.append(DiameterFilter(operator.le, diameter_max))
    if hazardous is not None:
        filters.append(HazardousFilter(operator.eq, hazardous))

    return tuple(filters)

def limit(iterator, n=None):
    """
    Limit the number of items produced from an iterator.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :return: An iterator producing at most `n` values.
    """
    if n:
        return (item for _, item in zip(range(n), iterator))
    return iterator