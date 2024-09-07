# Explore Close Approaches of Near Earth Objects

This project provides tools and scripts to explore and analyze close approaches of Near-Earth Objects (NEOs). It allows users to filter, query, and visualize data related to NEOs based on various parameters.

## Features

- **Data Extraction**: Extracts NEO data from various sources.
- **Database Management**: Stores and manages NEO data in a structured format.
- **Filtering and Querying**: Apply various filters to query NEO data.
- **Visualization**: Visualize NEO data using different charts and graphs.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/dustinober-hub/Explore-Close-Approaches-of-Near-Earth-Objects.git
```

### Navigate to the project directory:

```bash
cd Explore-Close-Approaches-of-Near-Earth-Objects
```

### Install the necessary dependencies (assuming you are using pip):

```bash
pip install -r requirements.txt
```
Usage
To use the project, run the main.py script with the desired parameters. For example:

```bash
python main.py --filter date=2024-09-06 --sort distance
```

You can use different options to filter, sort, and analyze the data. Refer to the code comments in main.py for more details on usage.

## Project Structure

- `main.py`: The main script to run the project.
- `database.py`: Handles database connections and queries.
- `extract.py`: Contains functions to extract NEO data from external sources.
- `filters.py`: Provides various filtering options for querying NEO data.
- `helpers.py`: Contains utility functions used throughout the project.
- `models.py`: Defines the data models used in the project.
- `write.py`: Handles writing processed data to files or databases.
- `res/`: Contains any resources or data files used in the project.
- `tests/`: Contains unit tests for the project's functionality.

## Contributing

We welcome contributions! To contribute, please fork the repository and submit a pull request with your changes. Ensure that your code follows the existing style and passes all tests.

1. **Fork the Project**
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

