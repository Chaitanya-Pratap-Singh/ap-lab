from flask import Flask, render_template, request
import pickle
import networkx as nx

app = Flask(__name__)

# Load the trained model (Graph)
with open("bus_route_graph.pkl", "rb") as f:
    G = pickle.load(f)

# Complete list of all bus stop locations
locations = [
    "Kashmere Gate", "ISBT", "Chandni Chowk", "Red Fort", 
    "India Gate", "Rajiv Chowk", "AIIMS", "Nehru Place", 
    "Saket", "Hauz Khas", "Vasant Kunj", "Connaught Place"
]

def astar_algorithm(graph, start, goal):
    """Find the shortest path using A* algorithm."""
    return nx.astar_path(graph, start, goal, weight='weight')

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", locations=locations)

@app.route("/predict", methods=["POST"])
def predict():
    start = request.form["start"]
    end = request.form["end"]
    
    try:
        route = astar_algorithm(G, start, end)
        route_str = " → ".join(route)
    except Exception as e:
        route_str = f"Error: {str(e)}"

    return render_template("index.html", locations=locations, route=route_str)

if __name__ == "__main__":
    app.run(debug=True)
