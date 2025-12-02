import streamlit as st
import requests
import random

API_KEY = "키_입력"

city_map = {
    # 주요 광역시 및 특별시
    "서울": "Seoul",
    "부산": "Busan",
    "대구": "Daegu",
    "인천": "Incheon",
    "광주": "Gwangju",
    "대전": "Daejeon",
    "울산": "Ulsan",
    "세종": "Sejong",
    "제주": "Jeju",
    "서귀포": "Seogwipo",

    # 경기도
    "수원": "Suwon",
    "용인": "Yongin",
    "화성": "Hwaseong",
    "성남": "Seongnam",
    "부천": "Bucheon",
    "안산": "Ansan",
    "평택": "Pyeongtaek",
    "안양": "Anyang",
    "시흥": "Siheung",
    "김포": "Gimpo",
    "하남": "Hanam",
    "광명": "Gwangmyeong",
    "군포": "Gunpo",
    "오산": "Osan",
    "이천": "Icheon",
    "안성": "Anseong",
    "의왕": "Uiwang",
    "양평": "Yangpyeong",
    "여주": "Yeoju",
    "과천": "Gwacheon",
    "고양": "Goyang",
    "남양주": "Namyangju",
    "파주": "Paju",
    "의정부": "Uijeongbu",
    "양주": "Yangju",
    "구리": "Guri",
    "포천": "Pocheon",
    "동두천": "Dongducheon",
    "가평": "Gapyeong",
    "연천": "Yeoncheon",

    # 강원도
    "춘천": "Chuncheon",
    "강릉": "Gangneung",
    "동해": "Donghae",
    "속초": "Sokcho",
    "삼척": "Samcheok",
    "태백": "Taebaek",
    "홍천": "Hongcheon",
    "횡성": "Hoengseong",
    "철원": "Cheorwon",
    "평창": "Pyeongchang",
    "영월": "Yeongwol",
    "정선": "Jeongseon",
    "인제": "Inje",
    "양양": "Yangyang",
    "화천": "Hwacheon",
    "양구": "Yanggu",

    # 충청북도
    "청주": "Cheongju",
    "충주": "Chungju",
    "제천": "Jecheon",
    "보은": "Boeun",
    "옥천": "Okcheon",
    "영동": "Yeongdong",
    "진천": "Jincheon",
    "음성": "Eumseong",
    "괴산": "Goesan",
    "단양": "Danyang",
    "증평": "Jeungpyeong",

    # 충청남도
    "천안": "Cheonan",
    "아산": "Asan",
    "서산": "Seosan",
    "당진": "Dangjin",
    "공주": "Gongju",
    "보령": "Boryeong",
    "논산": "Nonsan",
    "계룡": "Gyeryong",
    "홍성": "Hongseong",
    "예산": "Yesan",
    "부여": "Buyeo",
    "서천": "Seocheon",
    "청양": "Cheongyang",
    "태안": "Taean",
    "금산": "Geumsan",

    # 전라북도
    "전주": "Jeonju",
    "군산": "Gunsan",
    "익산": "Iksan",
    "정읍": "Jeongeup",
    "남원": "Namwon",
    "김제": "Gimje",
    "완주": "Wanju",
    "진안": "Jinan",
    "무주": "Muju",
    "장수": "Jangsu",
    "임실": "Imsil",
    "순창": "Sunchang",
    "고창": "Gochang",
    "부안": "Buan",

    # 전라남도
    "목포": "Mokpo",
    "여수": "Yeosu",
    "순천": "Suncheon",
    "나주": "Naju",
    "광양": "Gwangyang",
    "담양": "Damyang",
    "곡성": "Gokseong",
    "구례": "Gurye",
    "고흥": "Goheung",
    "보성": "Boseong",
    "화순": "Hwasun",
    "장흥": "Jangheung",
    "강진": "Gangjin",
    "해남": "Haenam",
    "영암": "Yeongam",
    "무안": "Muan",
    "함평": "Hampyeong",
    "영광": "Yeonggwang",
    "장성": "Jangseong",
    "완도": "Wando",
    "진도": "Jindo",
    "신안": "Sinan",

    # 경상북도
    "포항": "Pohang",
    "경주": "Gyeongju",
    "김천": "Gimcheon",
    "안동": "Andong",
    "구미": "Gumi",
    "영주": "Yeongju",
    "영천": "Yeongcheon",
    "상주": "Sangju",
    "문경": "Mungyeong",
    "경산": "Gyeongsan",
    "의성": "Uiseong",
    "청송": "Cheongsong",
    "영양": "Yeongyang",
    "영덕": "Yeongdeok",
    "청도": "Cheongdo",
    "고령": "Goryeong",
    "성주": "Seongju",
    "칠곡": "Chilgok",
    "예천": "Yecheon",
    "봉화": "Bonghwa",
    "울진": "Uljin",
    "울릉": "Ulleung",

    # 경상남도
    "창원": "Changwon",
    "진주": "Jinju",
    "김해": "Gimhae",
    "양산": "Yangsan",
    "거제": "Geoje",
    "통영": "Tongyeong",
    "사천": "Sacheon",
    "밀양": "Miryang",
    "의령": "Uiryeong",
    "함안": "Haman",
    "창녕": "Changnyeong",
    "고성": "Goseong",
    "남해": "Namhae",
    "하동": "Hadong",
    "산청": "Sancheong",
    "함양": "Hamyang",
    "거창": "Geochang",
    "합천": "Hapcheon"
}

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_menu_candidates(weather_main, temp):
    menus = []
    comment = ""
    
    if "Rain" in weather_main or "Drizzle" in weather_main:
        menus = ["해물파전", "바지락 칼국수", "짬뽕", "우동", "김치전", "수제비", "짜장면"]
        comment = "☔ 비랑 어울리는 메뉴는 어때요?"
    elif "Snow" in weather_main:
        menus = ["군고구마", "어묵탕", "만두전골", "설렁탕", "호빵", "우동", "새알팥죽", "칼국수"]
        comment = "☃️ 겨울하면 생각나는 음식들 어때요?"
    else:
        if temp <= 0:
            menus = ["순대국", "김치찌개", "부대찌개", "뼈해장국", "갈비탕", "청국장", "떡만두국", "알탕", "매운탕", "어묵탕"]
            comment = "🥶 추운 날에는 뜨끈한 국물 어때요?"
        elif 0 < temp <= 10:
            menus = ["온메밀", "잔치국수", "일본 라멘", "베트남 쌀국수", "샤브샤브", "수제비", "츠케멘", "떡라면", "카레", "스키야키"]
            comment = "🌬️ 쌀쌀한 날씨엔 따뜻한 요리 어때요?"
        elif 10 < temp <= 22:
            menus = ["한강 라면", "샌드위치", "수제버거", "떡볶이", "김밥", "토스트", "도시락", "샐러드", "오코노미야끼"]
            comment = "✨ 날씨도 좋은데 피크닉 어때요?"
        elif 22 < temp < 30:
            menus = ["초밥", "치킨", "피자", "연어덮밥", "파스타", "타코", "비빔면", "돈까스", "화덕피자", "가츠동"]
            comment = "☀️ 활동하기 좋은 날 사람들과 함께 어때요?"
        else:
            menus = ["평양냉면", "함흥냉면", "콩국수", "물회", "냉모밀", "메밀소바", "오이냉국", "물냉면", "비빔냉면"]
            comment = "🔥 이렇게 더운 날에는 시원한 메뉴 어때요?"

    return menus, comment

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

col_input, col_btn = st.columns([0.8, 0.2], vertical_alignment="bottom")

with col_input:
    user_input = st.text_input("도시 이름을 입력하세요 (예: 서울, 부산, 제주)")

with col_btn:
    is_clicked = st.button("메뉴 추천받기", use_container_width=True)

if is_clicked:
    city_english = city_map.get(user_input, user_input)
    data = get_weather(city_english)
    
    if data:
        st.session_state['weather_data'] = data
        w_main = data['weather'][0]['main']
        tmp = data['main']['temp']
        
        candidates, comment = get_menu_candidates(w_main, tmp)
        
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
        st.error(f"'{user_input}'을(를) 찾을 수 없습니다.")

if st.session_state['weather_data']:
    data = st.session_state['weather_data']
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    
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
            st.session_state['menu_confirmed'] = True
            st.session_state['rejected_menus'] = []
            st.rerun()

    with col2:
        if st.button("👎 별로에요"):
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
                <button style="
                    background-color: #03C75A; 
                    color: white; 
                    padding: 15px 0; 
                    border: none; 
                    border-radius: 10px; 
                    cursor: pointer;
                    font-weight: bold;
                    font-size: 18px;
                    width: 100%; 
                    display: block;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    🔍 네이버에서 '{search_query}' 검색하러 가기
                </button>
            </a>
        """, unsafe_allow_html=True)
