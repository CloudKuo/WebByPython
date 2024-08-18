
import streamlit as st

if __name__ == '__main__':
    # More emojis https://www.webfx.com/tools/emoji-cheat-sheet/
    # set basi page config
    st.set_page_config(page_title = "My first python web", page_icon = ":beaming_face_with_smiling_eyes:", layout= "wide", menu_items = {'Get Help': 'https://www.extremelycoolapp.com/help'} )

#     Header section
    with st.container():
        st.subheader("Hi I am Cloud :shushing_face:")
        st.title("This is the first web by streamlit Python")
        st.write("Power by python :snake: :dragon:")
        st.write("All you want is one for all")
        st.write("Learn more -> https://en.dragon-ball-official.com/")

    # My Description
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("---------")
            st.header("About Me")
        st.write("I am Cloud. I am the most handsome guy in the world :mushroom:")


