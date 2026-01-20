import streamlit as st
import pandas as pd
import seaborn as sns
st.markdown("# Main Page")

data = st.file_uploader("Choose a CSV file", type=["csv", "txt", "xlsx","xls","json","tsv"])

if data is not None:
    data2 = pd.read_csv(data)
    st.dataframe(data2)


st.checkbox("Show summary statistics",key="Show summary statistics")
if st.session_state.get("Show summary statistics"):
    st.write(data2.describe())


st.checkbox("Plot it",key="a")
if st.session_state.get("a"):
    st.pyplot(sns.pairplot(data2))


st.text_input("data columns", key="name")
if st.session_state.get("name"):
    st.write(data2[st.session_state.get("name")])

st.markdown("Conditional based querying") 
st.text_input("Column name", key="col")
st.text_input("Value", key="val")
if st.session_state.get("col") and st.session_state.get("val"):
    st.write(data2[data2[st.session_state.get("col")] == st.session_state.get("val")])