import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

import os
import matplotlib.font_manager as fm 

def uniqueA(list):
    x = np.array(list)
    return np.unique(x)

font_dirs = [os.getcwd()+'/fonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)

fm._load_fontmanager(try_read_cache=False)

fontNames = [f.name for f in fm.fontManager.ttflist]
fontname = st.selectbox('폰트선택', uniqueA(fontNames))

plt.rc('font', family=fontname)

df = pd.DataFrame({
    '이름': ['영수','철수','민수'],
    '나이': [22,31,25],
    '몸무게': [75.5,80.2,65.1]
})

st.dataframe(df, use_container_width=True)

fig, ax = plt.subplots()
# ax.bar(df['이름'],df['나이'])
# st.pyplot(fig)
barplot = sns.barplot(x='이름',y='나이',data=df, ax=ax, palette='Set2')
fig = barplot.get_figure()
st.pyplot(fig)

# tips = sns.load_dataset("tips")
# fig, ax = plt.subplots()
# sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
# ax.set_title("한글 폰트 테스트")
# st.pyplot(fig)
# st.dataframe(tips)

# st.title('데이터 나타내기')

# df = pd.DataFrame({
#     'first' : [1,2,3,4],
#     'second' : [5,6,7,8]
# })

# # st.table(df)
# st.dataframe(df, use_container_width=True)
# # st.code(sample_code, language='python')

# button = st.button('Press button')
# if button:
#     st.write('버튼을 눌렀습니다.')

# st.download_button(label='다운로드',data=df.to_csv(),file_name='data.csv',mime='text/csv')

# agree = st.checkbox('동의하십니까?')

# if agree:
#     st.write('동의하셨습니다.')

# fruits = st.radio('좋아하는 과일은?', ('수박','사과','포도'))
# text=fruits+' 좋아'
# st.write(text)

# fruits1 = st.selectbox('좋아하는 과일은?', ('수박','사과','포도'),index=2)
# text1=fruits1+' 좋아'
# st.write(text1)

# text_input = st.text_input(label='좋아하는 과일은', placeholder='좋아하는 과일을 입력해주세요')

# st.write(f'당신이 선택한 과일: [{text_input}]')

# number_input = st.number_input(label='나이?', min_value=10,max_value=100,value=20,step=1)

# st.write(f'입력하신 나이는: [{number_input}]')

# st.title('섭씨 화씨 변환기')

# temp_type = st.radio('온도유형', ('섭씨','화씨'))
# temp_input = st.number_input(label='온도', min_value=10,max_value=100,value=20,step=1)

# button = st.button('변환하기')
# if button:
#     if temp_type=='섭씨':
#         rev_temp = (temp_input*1.8)+32
#         st.write(f'화씨:{round(rev_temp,2)}')
#     else:
#         rev_temp = (temp_input-32)/1.8
#         st.write(f'섭씨:{round(rev_temp,2)}')