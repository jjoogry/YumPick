import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import db

st.set_page_config(page_title="관리자 페이지", page_icon="📊")

st.title("📊 오늘 뭐 먹지? 관리자 대시보드")

password = st.sidebar.text_input("관리자 암호", type="password")
if password != "1234":
    st.warning("관리자 암호를 입력하세요")
    st.stop()

df = db.get_all_logs()

if df.empty:
    st.info("아직 데이터가 충분하지 않습니다. 앱에서 추천을 몇 번 받아보세요!")
else:
    st.markdown("### 📈 실시간 서비스 이용 현황")
    col1, col2, col3 = st.columns(3)
    col1.metric("총 추천 횟수", f"{len(df)}회")
    
    likes = len(df[df['reaction'] == 'like'])
    dislikes = len(df[df['reaction'] == 'dislike'])
    col2.metric("좋아요(👍)", f"{likes}회")
    col3.metric("별로에요(👎)", f"{dislikes}회")

    st.divider()

    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("🏆 인기 메뉴 Top 5")
        like_df = df[df['reaction'] == 'like']
        if not like_df.empty:
            top_menus = like_df['recommended_menu'].value_counts().head(5)
            st.bar_chart(top_menus)
        else:
            st.write("아직 '좋아요' 데이터가 없습니다.")

    with col_chart2:
        st.subheader("🌤️ 날씨별 추천 비중")
        weather_counts = df['weather'].value_counts()
        st.bar_chart(weather_counts)

    st.divider()
    st.subheader("📝 사용자 상세 로그")
    st.dataframe(df.sort_values(by='id', ascending=False), use_container_width=True)