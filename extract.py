"""
Near-Earth Object (NEO) Data Loader.

This module provides functionalities to load data about Near-Earth Objects (NEOs) and their close approaches to Earth.
The data can be sourced from CSV and JSON files. The module contains functions to parse these files, extract relevant
information, and create instances of `NearEarthObject` and `CloseApproach` classes.

Functions:
- `load_neos(neo_csv_path: str) -> List[NearEarthObject]`: Loads NEO data from a CSV file.
- `load_approaches(cad_json_path: str) -> List[CloseApproach]`: Loads close approach data from a JSON file.

Usage:
    neos = load_neos('path_to_neo_data.csv')
    approaches = load_approaches('path_to_approach_data.json')
"""

import csv
import json

from models import NearEarthObject, CloseApproach

def load_neos(neo_csv_path):
    """
    Load Near-Earth Object (NEO) data from a CSV file.

    This function reads NEO data from a CSV file, extracts relevant information,
    and creates `NearEarthObject` instances for each NEO. 

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A list of `NearEarthObject` instances.
    """
    neos = []

    with open(neo_csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            designation = row['pdes']
            name = row['name'] if row['name'] else None
            diameter = float(row['diameter']) if row['diameter'] else float('nan')
            hazardous = row['pha'] == 'Y'
            neo = NearEarthObject(designation=designation, name=name, diameter=diameter, hazardous=hazardous)
            neos.append(neo)

    return neos

def load_approaches(cad_json_path):
    """
    Load close approach data from a JSON file.

    This function reads close approach data from a JSON file, extracts relevant information,
    and creates `CloseApproach` instances for each approach. 

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A list of `CloseApproach` instances.
    """
    approaches = []

    with open(cad_json_path, 'r') as file:
        data = json.load(file)
        for approach_data in data['data']:
            approach_info = dict(zip(data['fields'], approach_data))
            
            designation = approach_info['des']
            time = approach_info['cd']
            distance = float(approach_info['dist'])
            velocity = float(approach_info['v_rel'])
            approach = CloseApproach(designation=designation, time=time, distance=distance, velocity=velocity)
            approaches.append(approach)

    return approaches
