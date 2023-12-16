
#pip install gspread oauth2client pandas streamlit, pip install koreanize-matplotlib
#pip install gspread

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_gsheets import GSheetsConnection
import koreanize_matplotlib


st.set_page_config(
      page_title="밀도 탐구",
      page_icon="images/crown.png",
      layout="wide"
)

# Google Sheets API에 연결
#scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('5a2786e4bf2e30bfc502f11e84a401d7d9d74c4b', scope)
#client = gspread.authorize(creds)

# Google Sheets 문서 열기
#sheet = client.open('streamlit-gsheets-demo').sheet1

# 데이터를 pandas DataFrame으로 변환
#data = sheet.get_all_records()
#df = pd.DataFrame(data)

st.title(':clipboard:데이터 해석')
st.header(':white_medium_square: 데이터 값 확인 및 그래프 변환', divider='rainbow')
st.subheader(':one: 금속A')

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(
    worksheet="data1",
    usecols=[1, 2],
    nrows=6,
)


conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(
    worksheet="data1",
    ttl="10m",
    usecols=[0, 1, 2],
    nrows=6,
)

# 화면 분할 설정
col1, col2 = st.columns([1.0,3.0])

# 왼쪽 열에 데이터프레임 표시
df = df.reset_index(drop=True)

with col1:
    st.write(df)


# 데이터프레임에서 필요한 데이터 추출
x = df['volume']
y = df['mass']

# 그래프 그리기
plt.figure(figsize=(5, 3)) # 그래프 크기 설정
plt.plot(x, y, color='blue') # 선 그래프 그리기
plt.title('금속 A Volume vs Mass') # 그래프 제목 설정
plt.xlabel('Volume') # x축 라벨 설정
plt.ylabel('Mass') # y축 라벨 설정

# 그래프를 보여줄 것인지에 대한 버튼 추가
if st.button('그래프로 변환하기', key='unique_key1'):
    # 오른쪽 열에 그래프 표시
    with col2:
        st.pyplot(plt)

#############
st.subheader(':two: 금속 B')

conn = st.connection("gsheets", type=GSheetsConnection)
df1 = conn.read(
    worksheet="data2",
    usecols=[0, 1, 2],
    nrows=6,
)

# 화면 분할 설정
con1, con2 = st.columns([1.0,3.0])

with con1:
    st.write(df1)


# 데이터프레임에서 필요한 데이터 추출
x = df1['volume']
y = df1['mass']

# 그래프 그리기
plt.figure(figsize=(5, 3)) # 그래프 크기 설정
plt.plot(x, y, color='red') # 선 그래프 그리기
plt.title('금속 B Volume vs Mass') # 그래프 제목 설정
plt.xlabel('Volume') # x축 라벨 설정
plt.ylabel('Mass') # y축 라벨 설정

# 그래프를 보여줄 것인지에 대한 버튼 추가
if st.button('그래프로 변환하기', key='unique_key2'):
    # 오른쪽 열에 그래프 표시
    with con2:
        st.pyplot(plt)


# 데이터프레임에서 필요한 데이터 추출
x1 = df['volume']
y1 = df['mass']

x2 = df1['volume']
y2 = df1['mass']


# 그래프 그리기
plt.figure(figsize=(10,5)) # 그래프 크기 설정

plt.plot(x1, y1, color='blue', label='금속 A')
plt.plot(x2, y2, color='red', label='금속 B')

plt.title('금속 A vs 금속 B Volume vs Mass') # 그래프 제목 설정
plt.xlabel('Volume') # x축 라벨 설정
plt.ylabel('Mass') # y축 라벨 설정
plt.legend() # 범례 표시

st.subheader(':three: 금속 A와 B')


# 오른쪽 열에 그래프 표시
st.pyplot(plt)

# 텍스트 입력을 받는 코드
user_text = st.text_input('위 그래프에 대한 해석 내용을 부피와 질량을 이용하여 작성하세요.')

# 버튼을 누르면 입력값을 출력하는 코드
if st.button('의견 제줄하기'):
    if user_text == "":
        st.write("제출한 의견이 없습니다. 작성해 주세요.")
    elif '밀도' in user_text:
        st.write("밀도로 설명을 했네요. 훌륭해요.")
    else:
        st.write("밀도를 이용한 해석을 다시 해볼까요?")