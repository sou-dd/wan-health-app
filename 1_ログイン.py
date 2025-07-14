# セッション変数の初期化
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ログアウト処理
if st.session_state.logged_in:
    if st.button("ログアウト"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# ログインしていない場合はログイン画面
if not st.session_state.logged_in:
    st.title("ログイン")
    user_id = st.text_input("ユーザーID")
    password = st.text_input("パスワード" , type="password")

if st.button("ログイン"):
    # (ここではCSVから読みこむ仮処理、あとでlogin.pyを使うのも可)
    try:
        df_users = pd.read_csv("user_data/users.csv")
        user = df_users[
            (df_users["users_id"] == user_id) & (df_users["password"] == password)
        ]
        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.user_id = user_id
            st.session_state.user_mode = user.iloc[0]["mode"]
            st.experimental_rerun()
        else:
            st.error("IDかパスワードが違います")
    except FileNotFoundError:
        st.error("ユーザーが登録されていません")
