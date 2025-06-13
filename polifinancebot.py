import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # <- Replace this with your real key

st.title("PoliFinanceBot")
st.write("Ask about a political event and how it might affect the financial market.")

user_input = st.text_input("Enter a political event or decision:")

if st.button("Analyze"):
    prompt = f"You are a political economy and market strategy expert. Analyze how this political event may impact global financial markets in a detailed, sector-specific way: {user_input}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response.choices[0].message.content)
