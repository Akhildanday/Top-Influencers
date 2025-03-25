import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("engagement_model.pkl")

# Dictionary for country encoding (update if needed)
country_mapping = {
    "United States": 24, "India": 8, "Spain": 18, "Unknown": 15, "Brazil": 4,
    "Netherlands": 6, "United Kingdom": 7, "Uruguay": 9, "Turkey": 10, "Indonesia": 11,
    "Colombia": 12, "France": 13, "Australia": 14, "Italy": 16, "United Arab Emirates": 17,
    "Puerto Rico": 19, "Côte d'Ivoire": 20, "Anguilla": 21, "Switzerland": 22,
    "Sweden": 23, "British Virgin Islands": 25, "Czech Republic": 26, "Mexico": 27,
    "Germany": 28, "Russia": 29
}

# Streamlit App UI
st.title("Instagram Engagement Rate Predictor 📊")
st.write("Enter the influencer details to predict engagement rate.")

# Input fields
followers = st.number_input("Followers", min_value=0, step=1000)
avg_likes = st.number_input("Average Likes", min_value=0, step=100)
new_post_avg_like = st.number_input("New Post Average Likes", min_value=0, step=100)
total_likes = st.number_input("Total Likes", min_value=0, step=1000)
posts = st.number_input("Number of Posts", min_value=0, step=1)
influence_score = st.slider("Influence Score", min_value=0, max_value=100, step=1)

# Country Dropdown
selected_country = st.selectbox("Select Country", list(country_mapping.keys()))
country_encoded = country_mapping[selected_country]  # Convert to encoded value

# Predict button
if st.button("Predict Engagement Rate"):
    # Prepare input features
    input_data = np.array([[influence_score, posts, followers, avg_likes, new_post_avg_like, total_likes, country_encoded]])
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    # Display Result
    st.success(f"Predicted Engagement Rate: {prediction:.4f}")
