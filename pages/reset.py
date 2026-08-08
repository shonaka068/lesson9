import streamlit as st

st.title("ユーザー情報リセット")

if st.button("情報をリセット"):
    if st.button("確認: 本当にリセットしますか？"):
        st.session_state.user_name = ""
        st.session_state.age = ""
        st.session_state.gakunenn = ""
        st.session_state.syumi = ""
        st.success("ユーザー情報がリセットされました")
