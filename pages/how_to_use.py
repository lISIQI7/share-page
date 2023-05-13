import streamlit as st

st.set_page_config(
    page_title="share-page",
    page_icon="🎶",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown("""
# share-page
Language : [English]

LICENSE: : Modifications copyright (C) 2023 AKAZ and LISIQI7
Fascinating tool to convert images into pixel art!\n
Playground : [open it](https://tensorspace.org/html/playground/lenet.html).  


# Basic functions
## colorpallet
This site converts colors.  
Select the color palette to use when converting colors.  
Pyxel color  [Try it](https://sophisticated-palette.streamlit.app/).  


## ratio
This is a slider that can be adjusted in increments of 0.01. The lower the number, the larger the dot.


## Custom Pallet
You can create your own ColorPallet.  
Enter the colors you want to add to the palette in the table using color codes.  
The colors entered in the table will be displayed on the right side.  
It is easier to select a color from the color picker above the table, copy the color code, and enter it.  
Color picker is not supported.

 

# More Options
## Anime Filter
Add edges.  


## No Color Convert
Disables the color palette.  


## decrease Color
Decrease color.  
Basically used with ``No Color Convert``.

## threhsold
Value of AnimeFilter (edge processing).  
The smaller the value, the more edges are processed.  
### threhsold 1
Specifies the amount of edges.
### threhsold 2
Specifies the length of edges.

# Experimental Features
This is not an official feature yet, so there may be bugs or errors.  
## Pixel Edge
Generate edges with dots.

# Color Sample
Displays the colors in the default color palette  
""")
