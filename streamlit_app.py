import streamlit as st

bone_count = st.number_input(
    "Insert the number of bones you are ordering", min_value=None, value=0, placeholder="Type a number..."
)
st.write("The amount of bones you ordered is ", bone_count)

bone_price = st.number_input(
    "Insert the price of each bone", min_value=None, value=0.0, placeholder="Type a number..."
)
st.write("The price of each bone is ", bone_price)

money_spent_on_bones = bone_count * bone_price

st.header(f"You spent {int(money_spent_on_bones)} on the bones")
