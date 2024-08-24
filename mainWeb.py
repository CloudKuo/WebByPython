import requests
import streamlit as st
import json

from PIL import Image
from streamlit_lottie import st_lottie

def load_lottie_file(file_path: str):
    with open(file_path, "r") as file:
        return json.load(file)

def load_lottie_url(lottie_url):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        raise Exception("This url is not valid %s", lottie_url)
    return r.json()


def use_local_css_style(css_file_name_path):
    with open(css_file_name_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == '__main__':
    # More emojis https://www.webfx.com/tools/emoji-cheat-sheet/
    # set basi page config
    st.set_page_config(page_title="My first python web", page_icon=":beaming_face_with_smiling_eyes:", layout="wide",
                       menu_items={'Get Help': 'https://www.extremelycoolapp.com/help'})

    use_local_css_style("cssStyle/style.css")
    # Image files
    deep_image = Image.open("image/uuuuuu.png")

    # Load Lottie Assets
    lottie_animation_from_url = load_lottie_url("https://lottie.host/2462c497-4d71-4c4f-a594-8ad24598d938/qd4FQ0ypj0.json")
    lottie_animation_from_file = load_lottie_file("Animation/Animation - 1724484735639.json")
    #     Header section
    with st.container():
        st.subheader("Hi I am Cloud :shushing_face:")
        st.title(":blue-background[This is the first web by streamlit Python]")
        st.write("Power by python :snake:")
        st.write(" All you want is one for all")
        st.write(":orange[Learn more] -> :material/Home: https://en.dragon-ball-official.com/")
        st.write(":red[My Youtube Channel] -> :material/Videocam: https://www.youtube.com/@Cloud-theChosenOne/")
        st.markdown("[Watch Video](https://youtu.be/MYSIcuEt2oU?si=FGup4KDLCmfLvlWj)")

    # My Description
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("---")
            st.header("About Me :smile: ")
            st.write("I am Cloud. I am the most handsome guy in the world :mushroom:")
            st.write("Pegatron Engineer now.")
            st.image(deep_image, width=300)


        with right_column:
            st_lottie(lottie_animation_from_url, height=200, key="LottieFromURL", speed=1, loop=True)
            st_lottie(lottie_animation_from_file, height=200, key="LottieFromFile", speed=2, loop=True)

    # Contact form
    # use https://formsubmit.co/
    with st.container():
        st.write("---")
        st.header("Come and in touch with me!")
        # st.write("##") ## it means new line
        contact = """
        <form action="https://formsubmit.co/theanswer0411@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact, unsafe_allow_html=True)
        with right_column:
            st.empty()

    # Guest place
    with st.container():
        st.header(":gray-background[掲示板]")
        st.text_area("Write down your suggestion :smile:", height=200, key="dashboard")


