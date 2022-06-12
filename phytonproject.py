# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:01:35 2022

@author: kdeep
"""

import streamlit as st
import pandas as pd
from PIL import Image

img=Image.open(r"E:\pictures.webp")
st.image(img,use_column_width=True)
st.title("Dungeons & Dragons Currency Deductor")
st.subheader('please give the number of coins you have for each coin type')

copper=1/100
silver=1/10
electrum=1/2
gold=1
platinum=10


placeholder_si=st.empty()
placeholder_pl=st.empty()
placeholder_gd=st.empty()
placeholder_cp=st.empty()
placeholder_el=st.empty()

No_of_silver=placeholder_si.number_input('Enter number of Silver:',min_value=0)
No_of_platinum=placeholder_pl.number_input('Enter number of Platinum:',min_value=0)
No_of_gold=placeholder_gd.number_input('Enter number of Gold:',min_value=0)
No_of_copper=placeholder_cp.number_input('Enter number of Copper:',min_value=0)
No_of_electrum=placeholder_el.number_input('Enter number of Electrum:',min_value=0)



total_value=(No_of_silver*silver)+(No_of_platinum*platinum)+(No_of_gold*gold)
+(No_of_copper*copper)+(No_of_electrum*electrum)
total_value=round(total_value)

st.subheader(f'The  Total No of currency that you have:{total_value:,d}')

coins=[
       {"value":silver,"count":No_of_silver},
       {"value":platinum,"count":No_of_platinum},
       {"value":gold,"count":No_of_gold},
       {"value":copper,"count":No_of_copper},
       {"value":electrum,"count":No_of_electrum},
      ]

dp=pd.DataFrame(coins)
st.dataframe(data=dp)

st.bar_chart(data=dp)
st.area_chart(data=dp)
st.line_chart(data=dp)

