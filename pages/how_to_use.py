import streamlit as st

st.set_page_config(
    page_title="share-page",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown("""
# share-page
Language : [English]\n
LICENSE  : Modifications copyright (C) 2023 AKAZ and LISIQI7\n
Fascinating tool to convert images into pixel art!\n
Playground  [open it](https://tensorspace.org/html/playground/lenet.html) 


# basic functions

## colorpallet
This site converts colors.  
Select the color palette to use when converting colors.  
Pyxel color  [Try it](https://sophisticated-palette.streamlit.app/).  

## ratio

This is a slider that can be adjusted in increments of 0.01. The lower the number, the larger the dot.

## Custom Pallet

You can create your own ColorPallet.  

 
# More Options
Return to akaz [📨](https://pixelart.streamlit.app/how_to_use)
 
""")
