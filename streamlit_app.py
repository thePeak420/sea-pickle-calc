import streamlit as st

bone_count = st.number_input(
    "Insert the number of bones you are ordering", min_value=None, value=0, placeholder="Type a number..."
)
st.write("The amount of bones you ordered is ", bone_count)
