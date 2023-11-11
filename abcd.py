import streamlit as st
import pandas as pd
import numpy as np
st.title("ㅋㅋㄹㅃㅃ")
dataframe = pd.DataFrame({"first column": [1,2,3,4],"second column": [10,20,30,40]})
st.dataframe(dataframe,use_container_width=False) #아래와 다르게 기능 존재 , 인수use...는 크기를 가로에 맞춤?
st.table(dataframe) #그냥 출력.



st.write("Hello **world**!")
st.metric(label="온도",value="10℃",delta="1.2℃") #label은 위에 글씨 , value = 중심에 글자,delta = 아래에 숫자(양수,음수는 서로 화살표 방향이 다름.)
st.metric(label="삼성전자",value="61,000 원",delta="-1200 원")

col1,col2,col3 = st.columns(3) #가로줄을 세개로 나눔
col1.metric(label="달러USB",value="1,228 원",delta="-32.00 원") #같은곳에 매트릭을 쓰면 그아래에 만들어짐.단 같은 내용일 경우 이미있는 위치에 써짐.
col1.metric(label="달러USB",value="1,11128 원",delta="-32.00 원")
col2.metric(label="일본JPY(100엔)",value="958.63 원",delta="-7.44 원")
col3.metric(label="유럽연합EUR",value="1,335.82 원",delta="11.44 원")
