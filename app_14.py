
import streamlit as st
import plotly.express as px

tips_df = px.data.tips()
tabs_1, tabs_2 = st.tabs(["Descrptive Statstics", "Plots"])

with tabs_1:
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        dff = tips_df.describe()
        st.dataframe(dff)
        st.title("Title")
        
    with col_3:
        dff = tips_df.describe(include="O")
        st.dataframe(dff)

with tabs_2:
    fig = px.histogram(tips_df, x='tip')
    st.plotly_chart(fig)
