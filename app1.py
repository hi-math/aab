import streamlit as st
from st_pages import Page, show_pages, add_page_title
from PIL import Image

st.set_page_config(
      page_title="밀도 탐구",
      page_icon="images/crown.png",
      layout="wide"
)
st.subheader("")
st.title(":magic_wand: 내가 아르키메데스였다면?")
st.header(':white_medium_square: 문제 상황', divider='rainbow')

# 영상 링크 : https://www.youtube.com/watch?v=StynfAWBxuU
video_file = open('images/video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


st.subheader(':white_medium_square: 왕에게 어떤 결론을 전달해야할까요?', divider='rainbow')
st.image('images/question.png')
st.subheader(":heavy_check_mark: 데이터로 문제상황 해결하기: 직접 수집한 데이터로 설명해보자!")

show_pages(
    [
        Page("app1.py", "1. 문제 상황 확인", ":magic_wand:"),
        Page("app2.py", "2. 데이터 수집", ":clipboard:"),
        Page("app3.py", "3. 데이터 해석", ":old_key:"),
        Page("app4.py", "4. 문제 해결", ":exclamation:"),
    ]
)

