import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image
import pandas as pd
import textwrap
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
      page_title="밀도 탐구",
      page_icon="images/crown.png",
      layout="wide"
)

st.title(':exclamation:문제 해결')
st.header(':white_medium_square: 문제 상황 확인', divider='rainbow')
st.image('images/eureka.png', width=500)
st.markdown('전 시간에 했던 데이터 해석 결과를 바탕으로 문제 상황에 접목하여 내 생각을 정리하세요. [구글시트에 내 생각 입력하러 가기](https://docs.google.com/spreadsheets/d/1AfJ1XVLk75wllqbPQwZrIwnE0A9Be9p0jsxECjCyzrs/edit?usp=sharing)')
st.header(':white_medium_square: 친구들 의견 확인', divider='rainbow')

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(
    worksheet="data3",
    usecols=[0, 1],
    nrows=21,
)


# Google 시트의 공유 링크 URL
url = 'https://docs.google.com/spreadsheets/d/1AfJ1XVLk75wllqbPQwZrIwnE0A9Be9p0jsxECjCyzrs/gviz/tq?tqx=out:csv&sheet=data3'

# 첫 번째와 두 번째 열만 불러오기
df = pd.read_csv(url, usecols=[0, 1], dtype={'학번': str})

# 두 번째 열의 내용을 문자열로 변환한 후, 한 줄에 20개의 문자가 오도록 바꿈
df.iloc[:, 1] = df.iloc[:, 1].astype(str).apply(lambda x: textwrap.fill(x, 20))

# 데이터프레임의 너비를 500px, 높이를 300px로 설정하여 출력
st.dataframe(df, width=1000, height=300)

user_text = st.text_input('친구들의 의견도 참고하여 왕에게 전해야 할 얘기를 작성해주세요.')
if st.button(':man-bowing: 왕에게 내용 전달하기'):
    st.write('잘 전달되었습니다. 고생 많았어요!	:pray:')