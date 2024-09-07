"""
This module provides utilities for writing data about close approaches of near-Earth objects (NEOs) to CSV and JSON files.

The primary functions in this module are `write_to_csv` and `write_to_json`. The former writes a collection of `CloseApproach` objects to a CSV file, while the latter writes them to a JSON file. Both functions structure the output according to the attributes of the `CloseApproach` objects and their associated NEOs.
"""

import csv
import json

def write_to_csv(results, filename):
    """
    Write an iterable of `CloseApproach` objects to a CSV file.

    Each row in the resulting file corresponds to a single close approach, with columns for the approach's attributes and the associated NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: The desired location and name of the output file.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for approach in results:
            writer.writerow({
                'datetime_utc': approach.time_str,
                'distance_au': approach.distance,
                'velocity_km_s': approach.velocity,
                'designation': approach.neo.designation,
                'name': approach.neo.name,
                'diameter_km': approach.neo.diameter,
                'potentially_hazardous': approach.neo.hazardous
            })

def write_to_json(results, filename):
    """
    Write an iterable of `CloseApproach` objects to a JSON file.

    The resulting file contains a list of dictionaries, with each dictionary corresponding to a single close approach. The dictionary keys are the attributes of the approach and its associated NEO.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: The desired location and name of the output file.
    """
    output = []
    for approach in results:
        output.append({
            'datetime_utc': approach.time_str,
            'distance_au': approach.distance,
            'velocity_km_s': approach.velocity,
            'neo': {
                'designation': approach.neo.designation,
                'name': approach.neo.name,
                'diameter_km': approach.neo.diameter,
                'potentially_hazardous': approach.neo.hazardous
            }
        })

    with open(filename, 'w') as file:
        json.dump(output, file, indent=2)