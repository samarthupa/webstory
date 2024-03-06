import streamlit as st
import requests
import random

# Function to generate web story using ChatGPT
def generate_web_story(url):
    # Code to extract topic from webpage URL (you may use BeautifulSoup or other libraries)
    topic = "Topic extracted from URL"

    # Call OpenAI ChatGPT API to generate content (replace this with your implementation)
    content = f"This is a sample web story about {topic}."
    
    # Call Unsplash API to fetch relevant images based on topic
    image_url = fetch_image(topic)

    return topic, content, image_url

# Function to fetch image from Unsplash API
def fetch_image(topic):
    # Replace 'YOUR_UNSPLASH_ACCESS_KEY' with your actual access key
    access_key = 'YOUR_UNSPLASH_ACCESS_KEY'
    
    # Unsplash API endpoint for searching photos
    url = f"https://api.unsplash.com/search/photos?query={topic}&client_id={access_key}&per_page=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        # Extract image URL from response
        if data.get('results'):
            image_url = data['results'][0]['urls']['regular']
            return image_url
        else:
            return None
    except Exception as e:
        print(f"Error fetching image: {e}")
        return None

# Streamlit app
st.title("Automated Web Story Generator")

# Input field for webpage URL
url = st.text_input("Enter webpage URL:")

# Button to trigger generation
if st.button("Generate Web Story"):
    if url:
        topic, content, image_url = generate_web_story(url)
        st.write(f"Topic: {topic}")
        st.write(f"Content: {content}")
        if image_url:
            st.image(image_url, caption='Image related to the topic')
        else:
            st.write("No image found for the topic.")
