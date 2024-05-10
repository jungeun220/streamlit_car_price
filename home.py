import streamlit as st
import webbrowser

def run_home() :
    st.subheader('자동차 데이터를 분석하고 예측합니다.')
    st.text('- 탐색적 데이터 분석과 자동차 구매 금액을 예측하는 앱 입니다. ')
    st.text('- 데이터는 캐글에 있는 Car_Purchasing_Data.csv 파일을 사용했습니다.')

    url = 'https://www.kaggle.com/datasets/dev0914sharma/car-purchasing-model'
    
    st.write('데이터출처 : ' + url)
    
    st.image('./image/car.jpg', use_column_width = True)
