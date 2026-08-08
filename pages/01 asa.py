import streamlit as st
st.title("ユーザー情報表示ページ")
# session_stateからデータを取得
if 'user_name' in st.session_state and st.session_state.user_name:
    st.success(f"こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")
# 追加の表示
else:
    st.error("ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください")

if 'gakunenn' in st.session_state and st.session_state.gakunenn:
    st.write(f"{st.session_state.user_name}さんの学年は: {st.session_state.gakunenn}です。")
    st.write("メインページで入力された学年が正しく表示されています。")
else:
    st.error("学年が設定されていません")
    st.write("メインページで学年を選択してください")

if 'age' in st.session_state and st.session_state.age:
    st.write(f"{st.session_state.user_name}さんの年齢は: {st.session_state.age}歳です。")
    st.write("メインページで入力された年齢が正しく表示されています。")
else:
    st.error("年齢が設定されていません")
    st.write("メインページで年齢を選択してください")

if 'syumi' in st.session_state and st.session_state.syumi:
    st.write(f"{st.session_state.user_name}さんの趣味は: {', '.join(st.session_state.syumi)}です。")
    st.write("メインページで入力された趣味が正しく表示されています。")
else:
    st.error("趣味が設定されていません")
    st.write("メインページで趣味を選択してください")

if 'syumi' in st.session_state and "ゲーム" in st.session_state.syumi:
    st.write("ゲーム作りにも挑戦しよう！")
    st.balloons()  # 祝福のアニメーション
    