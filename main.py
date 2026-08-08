import streamlit as st
print("hell world")

st.title ("名前記憶アプリ")

name=st.text_input("あなたの名前を入力してください")
if st.button("名前を記録")：

st.write(f"記憶している名前")