import streamlit as st
import pandas as pd
import numpy as np
st.title("ㅋㅋㄹㅃㅃ")
dataframe = pd.DataFrame({"first column": [1,2,3,4],"second column": [10,20,30,40]})
st.dataframe(dataframe,use_container_width=False)
st.table(dataframe)



st.write("Hello **world**!")
