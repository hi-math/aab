import streamlit as st
from PIL import Image


##터미널에 선 설치
# pip install gspread , pip install pygsheets, pip install streamlit gspread oauth2client, pip install tk

st.set_page_config(
      page_title="밀도 탐구",
      page_icon="images/crown.png",
      layout="wide"
)
# 1번 구역

st.title(':clipboard:데이터 수집 준비')
st.header(':white_medium_square: 실험 기구 사용법 확인', divider='rainbow')
st.subheader(':one: 질량 측정')
#contents 추가할 떄 마다 비율 나누기

image_path = 'images/electronic scale.png'

con1, con2 = st.columns([2.0, 2.2])
con1.image(image_path, caption='전자저울')
con2.subheader("전자저울 사용 시 주의사항")
with con2:
    st.markdown('1. 전자저울은 사용 전 수평조정과 영점 조정을 하여야 합니다.')
    st.markdown('2. 전자저울에 외부의 진동이 잘 전달되지 않아야 합니다.')
    if st.button('두 가지 사항을 모두 확인했습니다.'):
        st.success('모든 주의사항을 확인하셨습니다. 전자저울을 사용해주세요.')


st.subheader(':two: 부피 측정')

# 화면을 두 개의 칸으로 나눕니다.
col1, col2 = st.columns([1.0,2.0])

# 왼쪽 칸에는 문제를 출력합니다.
with col1:
    st.image('images/cylinder.png', width=200)
    answer_cylinder = st.text_input('위 그림 속 실험 기구의 이름을 입력하세요.')
    if answer_cylinder:
        if answer_cylinder == '눈금 실린더' or answer_cylinder == '매스 실린더' or answer_cylinder == '메스 실린더':
            st.write('정답입니다!')
        else:
            st.write('오답입니다. 다시 생각해보세요.')

# 오른쪽 칸에는 이미지를 출력합니다.
col2.subheader("실험 기구를 사용한 부피 측정방법")
with col2:
      st.markdown('측정하고자 하는 물체를 물에 잠기게 하여 늘어난 부피를 물체의 부피로 측정하기')
      st.image('images/volume calibration.png', width=250)
      st.image('images/cylinder2.png', width=250)

st.header(':white_medium_square: 데이터 수집 방법 확인', divider='rainbow')
st.markdown("#### **:bulb: 데이터 수집하기: 여러 금속의 부피와 질량 값을 실험기구로 측정하여 google sheet에 작성해보자 :heavy_check_mark:**")
st.image('images/googlesheet.png')
st.markdown('실험기구로 측정한 부피와 질량 데이터 값을 구글시트에 입력하세요. [구글시트에 데이터 값 입력하러 가기](https://docs.google.com/spreadsheets/d/1AfJ1XVLk75wllqbPQwZrIwnE0A9Be9p0jsxECjCyzrs/edit?usp=sharing)')
