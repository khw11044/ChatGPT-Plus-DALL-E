import streamlit as st 
import openai 

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Make Prompt (ex: cute cat)")
    user_input2 = st.text_input("Enter required words (ex: 3D animation style or masterpiece, best quality, photorealistic, dramatic lighting, raw photo, ultra realistic details)")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appeareance of the input. Response it shortly around 30 words."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input + user_input2
    })
    

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt 
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALL-E..."):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )
    

    st.image(dalle_response["data"][0]["url"])
