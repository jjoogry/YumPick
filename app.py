import streamlit as st
import random
from modules import weather, menus, db 

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️")

if 'db_initialized' not in st.session_state:
    db.init_db()
    st.session_state['db_initialized'] = True

if 'weather_data' not in st.session_state:
    st.session_state['weather_data'] = None
if 'current_menu' not in st.session_state:
    st.session_state['current_menu'] = None
if 'menu_candidates' not in st.session_state:
    st.session_state['menu_candidates'] = []
if 'rejected_menus' not in st.session_state:
    st.session_state['rejected_menus'] = []
if 'menu_comment' not in st.session_state:
    st.session_state['menu_comment'] = ""
if 'notification' not in st.session_state:
    st.session_state['notification'] = None

st.markdown("<h1 style='text-align: center;'>🍽️ 오늘 뭐 먹지?</h1>", unsafe_allow_html=True)

with st.form(key='search_form'):
    col_input, col_btn = st.columns([0.8, 0.2], vertical_alignment="bottom")
    with col_input:
        user_input = st.text_input("도시 이름을 입력하세요 (예: 서울, 부산, 제주)")
    with col_btn:
        is_clicked = st.form_submit_button("메뉴 추천받기", use_container_width=True)

if is_clicked:
    clean_input = user_input.strip()
    
    if clean_input not in menus.city_map:
        st.error(f"'{clean_input}'은(는) 지원하지 않는 도시입니다.")
    else:
        city_english = menus.city_map[clean_input]
        
        data = weather.get_weather(city_english)
        
        if data:
            st.session_state['weather_data'] = data
            w_main = data['weather'][0]['main']
            tmp = data['main']['temp']
            
            candidates, comment = menus.get_menu_candidates(w_main, tmp)
            
            st.session_state['menu_candidates'] = candidates
            st.session_state['menu_comment'] = comment
            st.session_state['rejected_menus'] = []
            st.session_state['notification'] = None 
            st.session_state['menu_confirmed'] = False
            
            if candidates:
                picked = random.choice(candidates)
                st.session_state['current_menu'] = picked
                st.session_state['rejected_menus'].append(picked)
        else:
            st.error(f"잠시 후 다시 시도해주세요.")

if st.session_state['weather_data']:
    data = st.session_state['weather_data']
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    w_main = data['weather'][0]['main']
    
    st.write(f"### 📍 {user_input}의 날씨 정보")
    st.write(f"현재 날씨: **{weather_desc}** / 온도: **{temp}°C**")
    
    if st.session_state['notification']:
        st.warning(st.session_state['notification'])
        st.session_state['notification'] = None 

    st.info(f"{st.session_state['menu_comment']}")
    st.markdown(f"### 💡 추천 메뉴: **{st.session_state['current_menu']}**")

    if 'menu_confirmed' not in st.session_state:
        st.session_state['menu_confirmed'] = False

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 좋아요"):
            db.add_log(user_input, w_main, temp, st.session_state['current_menu'], 'like')
            
            st.session_state['menu_confirmed'] = True
            st.session_state['rejected_menus'] = []
            st.rerun()

    with col2:
        if st.button("👎 별로에요"):
            db.add_log(user_input, w_main, temp, st.session_state['current_menu'], 'dislike')
            
            st.session_state['menu_confirmed'] = False 
            
            remaining = list(set(st.session_state['menu_candidates']) - set(st.session_state['rejected_menus']))
            
            if remaining:
                picked = random.choice(remaining)
                st.session_state['current_menu'] = picked
                st.session_state['rejected_menus'].append(picked)
                st.rerun()
            else:
                st.session_state['notification'] = "😅 리스트를 초기화하고 다시 추천합니다."
                st.session_state['rejected_menus'] = [] 
                picked = random.choice(st.session_state['menu_candidates'])
                st.session_state['current_menu'] = picked
                st.session_state['rejected_menus'].append(picked)
                st.rerun()

    if st.session_state['menu_confirmed']:
        st.balloons()
        menu_name = st.session_state['current_menu']
        search_query = f"{user_input} {menu_name} 맛집"
        url = f"https://search.naver.com/search.naver?query={search_query}"
        
        st.markdown(f"""
            <a href="{url}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #03C75A; color: white; padding: 15px 0; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; font-size: 18px; width: 100%; display: block;">
                    🔍 네이버에서 '{search_query}' 검색하러 가기
                </button>
            </a>
        """, unsafe_allow_html=True)
