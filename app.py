import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

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

data = pd.read_csv('vegetable.csv', encoding='cp949')
dhead = data.iloc[:,0]

def extractYear(year):
    cols = data.columns[data.columns.str.contains(year)]
    ndata = pd.concat([dhead, data[cols]], axis=1, ignore_index=True)
    ndata.columns = ndata.iloc[0]
    return ndata[2:].reset_index(drop=True)

def extractData(d1, selected):
    s1 = '|'.join(selected)
    dh = d1.iloc[:,0]
    cols = d1.columns[d1.columns.str.contains(s1)]
    return pd.concat([dh, d1[cols]], axis=1, ignore_index=False)

year = st.selectbox('생산년도', range(2023,2014, -1))
dd = extractYear(str(year))

options = ['배추','시금치','상추','양배추']
selected = st.multiselect("채소를 선택하세요", options)
colors = ["#FF0000", "#3600F8", "#02FA4D", "#FDEC00"]

if selected:
   d2 = extractData(d1=dd, selected=selected)
   fig, ax = plt.subplots(layout='constrained')
   y_labels = d2['시도별']
   y_pos = np.arange(len(y_labels))
   bar_height = 0.8/len(selected)

   for i, sel in enumerate(selected):
       col = d2.columns[d2.columns.str.contains(sel)&d2.columns.str.contains('kg')]
       if not col.empty:
           offset = (i-len(selected)/2) * bar_height+bar_height/2
           ax.barh(y_pos+offset, [int(x) for x in d2[col[0]]], height=bar_height, 
                   color=colors[i%len(colors)], label=sel)
       ax.set_yticks(y_pos)
       ax.set_yticklabels(y_labels)
       ax.tick_params(axis='x', labelrotation=90)       
       ax.legend(title='채소종류')
       ax.set_xlabel('생산량(kg)')
       
   plt.title('채소생산량(엽채류)')
   st.pyplot(fig)
