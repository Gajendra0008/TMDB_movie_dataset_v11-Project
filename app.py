# import streamlit as st
# import pandas as pd
# import seaborn as sns
# data = pd.read_csv("mobile_sales.csv")

# data

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)



# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name


# st.pyplot(sns.pairplot(data))

# st.dataframe(data)

# st.write(data.columns)

# st.write(data.describe())

# st.write(data.size)
# st.write(data.shape)


# st.sidebar.markdown("# Main page 🎈")

import streamlit as st

st.markdown("# Main page ")
st.sidebar.markdown("# Sidebar ")