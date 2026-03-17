import base64
import groq
import streamlit as st
from dotenv import dotenv_values



config = dotenv_values(".env")
client = groq.Groq(api_key=config["GROQ_API_KEY"])

st.set_page_config('Idea Generator')
st.title('Idea Generator')

uploader = st.file_uploader('Upload a file to generate ideas from', type=['webp', 'png', 'jpg'])

if uploader:

    st.image(uploader, caption="Uploaded Image", use_container_width=True)

    image_data = base64.b64encode(uploader.read()).decode('utf-8')

    ext = uploader.name.split(".")[-1]

    media_type = f"image/{ext}" if ext != "jpg" else "image/jpeg"

    if st.button("Generate Ideas"):
        with st.spinner("Identifying components"):
            
            vision_response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{media_type};base64,{image_data}"
                            }
                        },
                        {
                            "type": "text",
                            "text": "List every electronic component, sensor, or microcontroller you can see in this image. Be specific with names (e.g. ESP32, SG90 servo, DHT11 sensor). Return as a clean bullet list."
                        }
                    ]
                }]
            )

            components = vision_response.choices[0].message.content.strip()
            st.subheader("Identified Components")
            st.markdown(components)

        with st.spinner("Generating project ideas"):
            idea_response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Based on the following components, generate 5 unique project ideas that could be built using them. Be creative and think of interesting applications. Return as a clean bullet list.\n\nComponents:\n{components}"
                        }
                    ]
                }]
            )

            ideas = idea_response.choices[0].message.content.strip()
            st.subheader("Generated Project Ideas")
            st.markdown(ideas)

            st.markdown("**Note:** The generated ideas are based on the identified components and may require additional parts or materials to complete. Always ensure you have the necessary resources and knowledge before starting a project.")