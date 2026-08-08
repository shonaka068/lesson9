import streamlit as st

st.title("ユーザー情報リセット")

st.write("保存されているユーザー情報をリセットします")
# 現在の情報を表示
if st.session_state.get('user_name') or st.session_state.get('gakunenn') or st.session_state.get('age') or st.session_state.get('syumi'):
    st.info("現在保存されている情報:")
    st.columns(f"名前: {st.session_state.get('user_name', '未設定')}")
    st.columns(f"学年: {st.session_state.get('gakunenn', '未設定')}")
    st.columns(f"年齢: {st.session_state.get('age', '未設定')}")
    st.columns(f"趣味: {', '.join(st.session_state.get('syumi', []))}")
    if st.button("すべての情報をリセット", type="primary"):
        st.session_state.user_name = ""
        st.session_state.gakunenn = ""
        st.session_state.syumi = []
        st.success("すべての情報がリセットされました")
        st.rerun()  # ページを再読み込み

else: st.warning("リセットする情報がありません")

