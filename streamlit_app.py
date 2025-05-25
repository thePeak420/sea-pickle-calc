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

shulkers_of_pickles_produced = st.number_input(
    "Insert how many shulkers of sea pickles the farm produced", min_value=None, value=0, placeholder="Type a number..."
)
pickles_produced = shulkers_of_pickles_produced * 27 * 64
st.write("The farm produced ", pickles_produced, " sea pickles")

pickle_price = st.number_input(
    "Insert the money gained per pickle", min_value=None, value=0.0, placeholder="Type a number..."
)
money_made = pickles_produced * pickle_price
st.write("You made ", money_made, "$")
