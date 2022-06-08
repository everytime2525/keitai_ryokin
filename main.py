import streamlit as st

st.title("携帯料金 計算")

# st.write("現在")

genzai = st.number_input("現在の料金を入力して", min_value=0, value=0, step=1)

# st.write("乗り換え後")

norikaego = st.number_input("乗り換え後の料金を入力して", min_value=0, value=0, step=1)

st.write("現在 - 乗り換え後は↓")

sagaku = genzai - norikaego

st.write(sagaku)
