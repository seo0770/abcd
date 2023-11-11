import streamlit as st
import pandas as pd
import numpy as np
st.title("ㅋㅋㄹㅃㅃ")
dataframe = pd.DataFrame({"first column": [1,2,3,4],"second column": [10,20,30,40]})
st.dataframe(dataframe,use_container_width=True) #아래와 다르게 기능 존재 , 인수use...는 크기를 가로에 맞춤?
st.table(dataframe) #그냥 출력.



st.write("Hello **world**!")
