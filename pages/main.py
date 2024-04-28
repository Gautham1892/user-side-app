import streamlit as st
import folium
from opencage.geocoder import OpenCageGeocode
from geopy.distance import great_circle
import folium.plugins as plugins
import osmnx as ox
import networkx as nx
import numpy as np

# Define locations
corporation_zones = {
    "Perambur Camp": {"location": [13.1126, 80.2329], "areas": ["Perambur", "Kolathur"]},
    "Royapuram Camp": {"location": [13.1137, 80.2953], "areas": ["Royapuram", "Tondiarpet"]},
    "Guindy Camp": {"location": [13.0080, 80.2206], "areas": ["Guindy", "Saidapet"]},
    "Porur Camp": {"location": [13.0324, 80.1689], "areas": ["Porur", "Mogappair"]},
    "Chromepet Camp": {"location": [12.9512, 80.1437], "areas": ["Chromepet", "Pallavaram"]},
    "Tambaram Camp": {"location": [12.9249, 80.1370], "areas": ["Tambaram", "Medavakkam"]},
    "Anna Nagar Camp": {"location": [13.0878, 80.2100], "areas": ["Anna Nagar", "Kilpauk"]},
    "Adyar Camp": {"location": [13.0065, 80.2572], "areas": ["Adyar", "Velachery"]},
    "Ambattur Camp": {"location": [13.0982, 80.1612], "areas": ["Ambattur", "Korattur"]},
    "Thiruvanmiyur Camp": {"location": [12.9855, 80.2677], "areas": ["Thiruvanmiyur", "Sholinganallur"]}
}

# Streamlit app
st.title("Disaster Relief Deployment App")

# Input for user's area
user_area = st.text_input("Enter your area (e.g., 'Chennai, India'):")

# Initialize OpenCage geocoder
key = "d6b091e7cc134728a37482a5877cee71"  # Replace with your OpenCage API key
geocoder = OpenCageGeocode(key)

# Default map center
map_center = [13.0827, 80.2707]  # Center of Chennai

# Display OpenStreetMap using Folium
m = folium.Map(location=map_center, zoom_start=11, control_scale=True, width='100%', height='600px')

# Add markers for Chennai Corporation Zones
for zone, data in corporation_zones.items():
    folium.Marker(data["location"], popup=f"Chennai Corporation {zone}", icon=folium.Icon(color="blue")).add_to(m)
    for area in data["areas"]:
        folium.Marker(location=[map_center[0], map_center[1]], popup=area).add_to(m)

# Add home pin and route if user_area is provided
if user_area:
    results = geocoder.geocode(user_area)
    if results:
        user_lat, user_lon = results[0]['geometry']['lat'], results[0]['geometry']['lng']
        folium.Marker([user_lat, user_lon], popup="Home", icon=folium.Icon(color="red")).add_to(m)
        
        # Find nearest Chennai Corporation Zone
        nearest_zone, nearest_zone_data = min(
            corporation_zones.items(),
            key=lambda x: great_circle(x[1]["location"], [user_lat, user_lon]).miles
        )
        
        st.write(f"Nearest Chennai Corporation Zone: {nearest_zone}")
        
        # Retrieve road network graph for the area
        G = ox.graph_from_point(nearest_zone_data["location"], network_type='drive', dist=3000)
        
        # Find the nearest node on the road network to the user's location
        nearest_node = ox.distance.nearest_nodes(G, user_lon, user_lat)
        
        # Find the nearest node on the road network to the nearest Chennai Corporation Zone
        nearest_zone_node = ox.distance.nearest_nodes(G, nearest_zone_data["location"][1], nearest_zone_data["location"][0])
        
        # Find the shortest path between the two nodes
        route = nx.shortest_path(G, nearest_node, nearest_zone_node, weight='length')
        
        # Plot the route on the map
        route_coordinates = [(G.nodes[route[i]]['y'], G.nodes[route[i]]['x']) for i in range(len(route))]
        folium.PolyLine(route_coordinates, color="green", weight=5, opacity=0.7).add_to(m)
        
        # Generate random points along the middle portion of the route
        num_random_points = 5
        middle_segment_length = len(route_coordinates) - 2  # Exclude the start and end points
        random_points_indexes = np.linspace(4, middle_segment_length-4, num_random_points-1, dtype=int)
        random_points = [route_coordinates[i] for i in random_points_indexes]
        
        # Add random points to the map
        for point in random_points:
            folium.Marker(point, popup="Water Logging", icon=folium.Icon(color="orange")).add_to(m)

# Display map using Streamlit
html = m._repr_html_()
st.components.v1.html(html, height=600)
