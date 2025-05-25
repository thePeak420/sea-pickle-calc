import streamlit as st

bone_count = int(st.number_input(
    "Insert the number of bones you are ordering", value=None, placeholder="Type a number..."
))
st.write("The amount of bones you ordered is ", bone_count)
