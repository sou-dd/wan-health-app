import streamlit as st

st.tilte("ログイン")

#セッション初期化
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

username = st.text_input("ユーザー名")
password = st.text_input("パスワード", type="password")

if st.button("ログイン"):
    # 仮のユーザー認証（ID: test / PW: 1234）
    if username == "test" and password == "1234":
        st.session_state.logged_in = True
        st.session_state.user_id = username
        st.success("ログイン成功")
        st.switch_page("wan_health_app.py") # 成功したら遷移
    else:
         st.error("IDかパスワードが間違っています")





# セッション変数の初期化
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
