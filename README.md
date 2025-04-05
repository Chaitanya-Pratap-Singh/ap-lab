<!-- @format -->

# Bus Route Optimizer

A web application that finds the optimal bus route between two locations in
Delhi using the A\* pathfinding algorithm.

## Overview

This application helps users find the shortest path between different bus stops
in Delhi. It uses a graph-based approach to model the bus network and implements
the A\* algorithm to find optimal routes between any two stops.

## Features

- Interactive web interface built with Flask
- Optimized route finding using the A\* algorithm
- Clean, modern UI with responsive design
- Support for all major bus stops in Delhi

## Technology Stack

- **Backend**: Python with Flask
- **Algorithm**: A\* pathfinding (NetworkX implementation)
- **Data Structure**: Graph representation of bus routes
- **Frontend**: HTML, CSS with dynamic rendering via Jinja2 templates

## How It Works

1. The application models Delhi's bus network as a weighted graph where:

   - Nodes represent bus stops
   - Edges represent direct connections between stops
   - Edge weights represent travel time/distance

2. When a user selects start and end points, the application:

   - Takes the input from the web form
   - Applies the A\* algorithm to find the shortest path
   - Returns the optimal route to the user

3. The A\* algorithm is particularly efficient for route finding because it:
   - Uses a heuristic to estimate the distance to the goal
   - Prioritizes paths that appear to lead closer to the destination
   - Generally finds optimal solutions faster than Dijkstra's algorithm

## Project Structure

```
aplab/
├── app.py                # Main Flask application
├── bus_route_graph.pkl   # Serialized graph data of bus routes
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # CSS styling
└── templates/
    ├── index.html        # Main page with form for route selection
    └── results.html      # Page displaying route results
```

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd aplab
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. On the homepage, select your starting point from the dropdown menu
2. Select your destination from the second dropdown
3. Click "Find Route"
4. The application will display the optimal route between these locations

## Future Enhancements

- Add map visualization of routes
- Include estimated travel times
- Support for real-time traffic data integration
- Mobile application version

## License

[MIT License](LICENSE)
