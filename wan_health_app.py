import streamlit as st
import pandas as pd
from datetime import date

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

      if st.button("ログイン")
　　　　　　　# (ここではCSVから読みこむ仮処理、あとでlogin.pyを使うのも可)
　　　　　　  try:
                  df_users = pd.read_csv("user_data/users.csv")
                  user = df_users[(df_users["users_id"] == user_id) & (df_users["password"] == password)]
                  if not user.empty:
                      st.session_state.logged_in = True
                      st.session_state.user_id = user_id
                      st.session_state.user_mode = user.iloc[0]["mode"]
                      st.experimental_rerun()
                  else:
                      st.error("IDかパスワードが違います")
        except FileNotFoundError:
            st.error("ユーザーが登録されていません")
else:
    # ログイン後の本体コード（ここに今までの記録・グラフなどを入れる）
    st.title("ワンちゃん健康管理アプリ")

try:
    df = pd.read_csv("wan_health")
except FileNotFoundError:
     df = pd.DataFrame(columns=["日付", "体重", "体調"])

# 入力フォーム
st.subheader("📋 今日の記録を入力")
today = date.today()
weight = st.number_input("体重 (kg)", min_value=0.0, step=0.1)
condition = st.selectbox("体調", ["元気", "普通", "少し元気ない", "病院に行った"])

if st.button("記録する"):
    new_data = pd.DataFrame([[today, weight, condition]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("wan_health.csv", index=False)
    st.success("✅ 記録しました！")

# 表とグラフ
st.subheader("📊 記録一覧")
st.dataframe(df)
import plotly.express as px

st.subheader("📈 体重の推移")
if not df.empty:
    df["日付"] = pd.to_datetime(df["日付"])
    fig = px.line(df, x="日付", y="体重", markers=True, title="わんちゃんの体重推移")
    fig.update_layout(xaxis_title="日付", yaxis_title="体重 (kg)", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
