import streamlit as st#a

st.title("ユーザー情報入力")

def session_hensu():
    if "user_name" not in st.session_state:
        st.session_state.user_name=""
    if "age" not in st.session_state:
        st.session_state.age=""
    if "gakunenn" not in st.session_state:
        st.session_state.gakunenn=""
    if "syumi" not in st.session_state:
        st.session_state.syumi=""


def detanyuryoku():
    name=st.text_input("あなたの名前を入力してください")
    if st.button("名前を保存"):
        if not name:
            st.warning("名前を入力してください")
        st.session_state.user_name=name
        st.success(f"名前を保存しました")
    st.write(f"現在保存されている名前: {st.session_state.user_name}")

    gakunenn=st.selectbox("学年を選択してください", ["小学５年生", "小学６年生", "中学１年生", "中学２年生", "中学３年生"])
    if st.button("学年を保存"):
        st.session_state.gakunenn=gakunenn
        st.success(f"学年を保存しました")
    st.write(f"現在保存されている学年: {st.session_state.gakunenn}")

    age=st.slider("年齢を選択してください", 11,15,11)
    if st.button("年齢を保存"):
        st.session_state.age=age
        st.success(f"年齢を保存しました")
    st.write(f"現在保存されている年齢: {st.session_state.age}")

    syumi=st.multiselect("趣味を入力してください", ["読書", "スポーツ", "音楽", "ゲーム", "絵画","その他"])
    if st.button("趣味を保存"):
        st.session_state.syumi=syumi
        st.success(f"趣味を保存しました")
    st.write(f"現在保存されている趣味: {st.session_state.syumi}")

session_hensu()
detanyuryoku()