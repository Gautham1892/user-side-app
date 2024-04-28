# key = "d6b091e7cc134728a37482a5877cee71"  # Replace with your OpenCage API key
import streamlit as st
import folium
from opencage.geocoder import OpenCageGeocode
from geopy.distance import great_circle
import folium.plugins as plugins

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
        
        # Add waypoints for routing
        waypoints = [
            [user_lat, user_lon],
            nearest_zone_data["location"]
        ]
        
        # Add routing control
        folium.plugins.AntPath(locations=waypoints, color='green', weight=5).add_to(m)

# Display map using Streamlit
html = m._repr_html_()
st.components.v1.html(html, height=600)
