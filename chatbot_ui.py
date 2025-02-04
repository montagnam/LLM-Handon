import streamlit as st
import openai
import os
from dotenv import load_dotenv  # Load .env file

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client using the API key from .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key is missing. Please check your .env file.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# Load system prompt from file
with open("master_prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read().strip()

# Streamlit UI
st.title("Doctor AI Chatbot")
st.write("This chatbot simulates doctor-patient interactions.")

# User input box
user_query = st.text_input("Enter your query:")

# Chatbot response
if st.button("Send"):
    if user_query.strip():
        try:
            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o",  # Use "gpt-4o" or another valid model name
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query},
                ],
                max_tokens=128
            )

            # Extract chatbot response
            chatbot_response = response.choices[0].message.content

            # Display chatbot response
            st.text_area("Chatbot Response:", value=chatbot_response, height=150)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query.")