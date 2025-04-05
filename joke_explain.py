import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Title of the app
st.title("Joke Explainer")

# Text box for user to enter a joke
joke = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke:
        # Call OpenAI API to get the explanation
    
        response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"explain this joke: {joke}",
        }
    ],
    model="gpt-4o-mini"
)

        # Extract the explanation from the response
        explanation = response.choices[0].message.content
        
        # Display the explanation
        st.subheader("Explanation")
        st.write(explanation)
    else:
        st.warning("Please enter a joke before submitting.")