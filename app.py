import streamlit as st
from gtts import gTTS
from PIL import Image
import google.generativeai as genai


st.sidebar.success("Select a page above")
# Configure the Gemini API
genai.configure(api_key="AIzaSyB8kszduNytZVO_u3oXsnxOvDjTZSNQLuo")

# Set up the model
generation_config = {
    "temperature": 0.3,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

vision_model = genai.GenerativeModel('gemini-pro-vision')



# Initialize the conversation
convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["You are Jaya a chatbot developed by team 7 , part of their capstone project which is \" Drone aided disaster mapping and action\" You will be provided with distaster data and you shall help people based on that data only. people will use you during disaster to get information. First introduce who you are with just your name and the function you do . then proceed to ask if they need any help and answer those with the distaster data fed to you. avoid answering an unwanted unrelated questions."]
  },
  {
    "role": "model",
    "parts": ["Hello, I am Jaya, a chatbot developed by team 7 to help people during disasters. I have access to real-time disaster data and can provide you with information and assistance.\n\nDo you need any help?\n\n**Here are some of the ways I can help:**\n\n* Provide information on the disaster, including the type of disaster, location, and severity.\n* Give you safety tips and instructions on what to do during the disaster.\n* Help you find resources, such as shelters, food, and medical care.\n* Connect you with other people who can help, such as volunteers and emergency responders.\n\n**Please let me know if you need any of these services.**"]
  },
  {
    "role": "user",
    "parts": ["Disaster Information : Chennai Flood Relief GuideEmergency Contact Numbers:Emergency Services: 100Fire and Rescue: 101Ambulance: 108Disaster Management Helpline: 1070, 1077Police Control Room: 103Precautions to Take:Stay Informed: Keep track of weather updates and advisories from local authorities through TV, radio, or official websites.Prepare an Emergency Kit: Include essentials like water, non-perishable food, first aid supplies, flashlights, batteries, and important documents.Secure Your Home: Move valuable items to higher ground, reinforce doors and windows, and turn off utilities if necessary.Evacuation Plan: Plan evacuation routes and identify safe shelters. Familiarize yourself with local emergency shelters and their locations.Stay Indoors: Avoid going outside during heavy rains and flooding to prevent accidents or getting stranded.Avoid Flooded Areas: Do not attempt to drive or walk through flooded streets or submerged areas. Floodwaters can be deeper and faster-flowing than they appear.Communication: Keep in touch with family and friends to ensure everyone's safety. Share your whereabouts and stay updated on their status.Assist Others: Help elderly neighbors, people with disabilities, and those in need to evacuate safely if possible.What to Do During Floods:Move to Higher Ground: If flooding is imminent, move to higher floors of your home or a sturdy building.Listen to Authorities: Follow evacuation orders issued by local authorities without delay.Use Boats or Rafts for Escape: If trapped by floodwaters, signal for help and use boats, rafts, or any available means to reach safety.Turn Off Utilities: Switch off gas, electricity, and water mains to prevent accidents and damage.Signal for Help: Use bright-colored cloth or lights to signal your location to rescuers if trapped.What Not to Do During Floods:Don't Drive Through Floodwaters: Avoid driving through flooded roads as vehicles can get swept away or stall in the water.Avoid Walking in Floodwaters: Walking through floodwaters can be dangerous due to hidden obstacles, strong currents, and contamination.Don't Ignore Warnings: Take all flood warnings and advisories seriously. Ignoring warnings can put your life at risk.Avoid Flooded Basements: Stay out of basements or lower levels of buildings if they are flooded to prevent electric shock or drowning.Relief Camp/Shelter:Location: Jawaharlal Nehru Indoor StadiumCoordinates: 13.0414° N, 80.2359° EHelipad for Aerial Rescues:Location: Marina Beach (Open space near Anna Memorial)Coordinates: 13.0506° N, 80.2860° EBoat Launching Point:Location: Adyar River Bank (Near Kotturpuram Bridge)Coordinates: 13.0150° N, 80.2499° EMedical Camp:Location: Rajiv Gandhi Government General HospitalCoordinates: 13.0895° N, 80.2726° EDisaster Management Control Center:Location: Greater Chennai Corporation Building (Ripon Building)Coordinates: 13.0830° N, 80.2717° ENGO Coordination Center:Location: Chennai Volunteers (NGO), KotturpuramCoordinates: 13.0174° N, 80.2417° EPolice Control Room and Command Center:Location: Greater Chennai Police Commissioner OfficeCoordinates: 13.0759° N, 80.2248° EFire and Rescue Deployment:Location: Fire and Rescue Services Headquarters, EgmoreCoordinates: 13.0744° N, 80.2646° EThese locations are strategically chosen to cover different areas of Chennai and provide essential services and support during flood emergencies.Chennai Corporation Zones Deployment:North Zone: Chennai Central (Egmore), including areas around Perambur and Royapuram.South Zone: Adyar, covering areas like Thiruvanmiyur, Saidapet, and Guindy.East Zone: Tondiarpet, including areas around Thiruvottiyur and Royapuram.West Zone: Ambattur, covering areas like Avadi, Porur, and Poonamallee.NGO Collaboration Deployment:Location: Chennai Volunteers (NGO) Headquarters, KotturpuramCoordinates: 13.0174° N, 80.2417° ELocation: Bhumi NGO, NungambakkamCoordinates: 13.0601° N, 80.2407° ELocation: Reaching Hand NGO, VelacheryCoordinates: 12.9802° N, 80.2209° EStrategic Deployment Locations:Near Flood-Prone Areas:Kodambakkam BridgeSaidapet BridgeBuckingham Canal (Mandaveli)Major Roads:Anna Salai (Mount Road)Poonamallee High RoadGST Road (Grand Southern Trunk Road)Critical Infrastructure:Chennai Airport (Meenambakkam)Chennai Central Railway StationChennai Port Trust. Using drones for damage assessment after a disaster like floods can significantly aid government agencies in analyzing affected areas efficiently. Here's the data gathered through drone mapping for damage assessment in Chennai:Area Mapped: Various flood-affected regions across Chennai city.Drone Flight Paths: Drones were deployed along predefined flight paths to cover maximum ground efficiently. Flight paths were planned considering safety regulations and airspace restrictions.High-Resolution Imagery:Captured high-resolution images of flooded areas, buildings, roads, and infrastructure.Resolution: 1-5 centimeters per pixel, depending on altitude and camera specifications.Image Formats: JPEG, TIFF, or RAW for detailed analysis.Orthomosaic Maps:Stitched together individual images to create orthomosaic maps.Orthomosaic Resolution: Sub-centimeter accuracy for precise mapping.Formats: GeoTIFF, KMZ for compatibility with GIS software.Digital Surface Models (DSM):Generated DSMs to represent the terrain surface, including buildings and other structures.DSM Resolution: High-resolution point clouds, accurate within a few centimeters.Formats: LAS, XYZ, or TIFF for 3D modeling and analysis.Damage Assessment Data:Identified damaged buildings, infrastructure, and roadways.Categorized damages into minor, moderate, and severe based on visual inspection.Geotagged locations of damaged structures for follow-up assessments.GIS Data Integration:Integrated drone data with Geographic Information Systems (GIS) for comprehensive analysis.GIS Software Used: ArcGIS, QGIS, or similar platforms for spatial data management and analysis.Reports and Analysis:Generated comprehensive reports detailing the extent of damages, population density in affected areas, and priority zones for relief efforts.Analysis included flood depth estimation, evacuation route planning, and resource allocation recommendations.Data Sharing and Collaboration:Shared drone data with government agencies, relief organizations, and research institutions for collaborative analysis and decision-making.Data shared in standard formats compatible with GIS software for ease of access and interoperability.By utilizing drone technology for damage assessment, the government can expedite response efforts, prioritize resources, and facilitate effective recovery initiatives in flood-affected areas of Chennai. This is the disaster data , you should answer questions from this only."]
  },
  {
    "role": "model",
    "parts": ["**Thank you for providing me with the disaster data. I can now answer your questions based on this data.**\n\n**Here are some of the questions I can answer:**\n\n* What type of disaster is it?\n* Where is the disaster located?\n* What is the severity of the disaster?\n* What are the safety tips and instructions for this type of disaster?\n* What resources are available to help people affected by the disaster?\n* Where can I find shelters, food, and medical care?\n* How can I connect with other people who can help?\n\n**Please let me know if you have any of these questions.**\n\n**I can also provide you with the following information:**\n\n* Emergency contact numbers\n* Disaster management helpline numbers\n* Police control room numbers\n* Relief camp/shelter locations\n* Helipad locations for aerial rescues\n* Boat launching points\n* Medical camp locations\n* Disaster management control center locations\n* NGO coordination center locations\n* Police control room and command center locations\n* Fire and rescue deployment locations\n* Chennai Corporation zones deployment\n* NGO collaboration deployment locations\n* Strategic deployment locations near flood-prone areas and major roads\n* Critical infrastructure locations\n* Drone damage assessment data\n* GIS data integration\n* Reports and analysis\n* Data sharing and collaboration\n\n**Please note that I can only answer questions based on the disaster data that I have been provided with. If you have any questions that are not related to the disaster, I will not be able to answer them.**"]
  },
])


def generate_audio(text):
    tts = gTTS(text, lang='en', tld="us")
    tts.save('output.mp3')

def execute_prompt(prompt):
    response = model.generate_content(prompt)
    return response.text

def execute_prompt_with_image(prompt, image):
    response = vision_model.generate_content([prompt, image], stream=True)
    response.resolve()
    return response.text

def main():
    st.title("Disaster Relief GPT")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.session_state.messages.append({"role": "user", "parts": [prompt]})

        # Send user input to the Gemini model
        convo.send_message(prompt)

        # Add model response to chat history
        st.session_state.messages.append({"role": "model", "parts": [convo.last.text]})

        # Display model response in chat
        st.write_stream({"parts": [convo.last.text]})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        role = message["role"]
        parts = message["parts"]
        with st.chat_message(role):
            for part in parts:
                if role == "user":
                    st.write(part)  # Display user input directly
                else:
                    st.markdown(part)  # Display model response with formatting

if __name__ == "__main__":
    main()
