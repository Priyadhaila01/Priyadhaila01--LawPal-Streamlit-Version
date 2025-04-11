import streamlit as st
import time

st.set_page_config(page_title="LawPal - Legal Chatbot", layout="centered")

st.title("⚖️ LawPal - Your Legal Assistant")
st.write("Get simplified legal advice based on Indian law, powered by AI.")

# Input box for user legal query
user_query = st.text_input("Enter your legal question:", "")

# Button to trigger the AI response
if st.button("Get Answer") and user_query:
    with st.spinner("Analyzing legal content..."):
        time.sleep(2)  # Simulate response time
        
        # Simulated AI legal response
        response = f"""
        Here’s a simplified explanation of your legal query:
        
        **Query:** {user_query}
        
        **AI Response:** According to Indian law, here's what you should know... [Detailed, simplified explanation here]
        """
        st.success("Response ready!")
        st.markdown(response)

st.markdown("---")
st.caption("LawPal uses Generative AI to enhance legal literacy and accessibility in India.")
