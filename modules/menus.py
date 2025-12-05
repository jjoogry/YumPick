import random
import sqlite3
import pandas as pd

city_map = {
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

# 각 메뉴의 상세 설명은 ChatGPT로 작성
MENU_DB = {
    # 비/흐림
    "해물파전": {
        "category": "한식",
        "desc": "비 오는 날 빗소리와 함께 즐기는 바삭한 파전",
        "tags": ["#비오는날", "#막걸리", "#바삭바삭"]
    },
    "바지락 칼국수": {
        "category": "한식",
        "desc": "시원한 조개 국물이 일품인 뜨끈한 국수",
        "tags": ["#국물요리", "#시원함", "#해장"]
    },
    "짬뽕": {
        "category": "중식",
        "desc": "얼큰한 국물과 해산물의 조화",
        "tags": ["#매운맛", "#해장", "#스트레스해소"]
    },
    "우동": {
        "category": "일식",
        "desc": "오통통한 면발과 따뜻한 국물의 정석",
        "tags": ["#따뜻함", "#면요리", "#휴게소"]
    },
    "김치전": {
        "category": "한식",
        "desc": "매콤새콤한 김치로 부쳐낸 한국인의 소울푸드",
        "tags": ["#비오는날", "#매콤", "#간식"]
    },
    "수제비": {
        "category": "한식",
        "desc": "쫀득한 반죽과 감칠맛 나는 국물",
        "tags": ["#손맛", "#비오는날", "#따뜻함"]
    },
    "짜장면": {
        "category": "중식",
        "desc": "달콤짭짤한 춘장 소스에 비벼먹는 국민 면요리",
        "tags": ["#국민음식", "#단짠", "#배달"]
    },

    # 눈/겨울
    "군고구마": {
        "category": "간식",
        "desc": "호호 불어가며 먹는 겨울철 최고의 별미",
        "tags": ["#겨울간식", "#달콤", "#추억"]
    },
    "어묵탕": {
        "category": "한식",
        "desc": "추운 몸을 녹여주는 따끈한 국물과 쫄깃한 어묵",
        "tags": ["#겨울", "#길거리음식", "#소주안주"]
    },
    "만두전골": {
        "category": "한식",
        "desc": "속이 꽉 찬 만두와 야채를 끓여먹는 전골",
        "tags": ["#푸짐함", "#따뜻함", "#가족외식"]
    },
    "설렁탕": {
        "category": "한식",
        "desc": "오래 끓여 진하고 뽀얀 사골 국물",
        "tags": ["#보양식", "#든든함", "#국밥"]
    },
    "호빵": {
        "category": "간식",
        "desc": "찬 바람 불 때 생각나는 따끈한 찐빵",
        "tags": ["#겨울간식", "#편의점", "#단팥"]
    },
    "새알팥죽": {
        "category": "한식",
        "desc": "달콤하고 부드러운 팥죽에 쫀득한 새알심",
        "tags": ["#동지", "#달콤", "#건강식"]
    },

    # 추위/영하
    "순대국": {
        "category": "한식",
        "desc": "들깨가루 팍팍 넣은 든든한 국밥 한 그릇",
        "tags": ["#국밥", "#해장", "#든든함"]
    },
    "김치찌개": {
        "category": "한식",
        "desc": "돼지고기와 김치의 환상적인 조화",
        "tags": ["#집밥", "#매콤", "#한국인의맛"]
    },
    "부대찌개": {
        "category": "한식",
        "desc": "햄과 소시지, 라면사리의 푸짐한 만남",
        "tags": ["#햄", "#라면", "#점심추천"]
    },
    "뼈해장국": {
        "category": "한식",
        "desc": "푸짐한 고기와 얼큰한 국물",
        "tags": ["#해장", "#고기", "#얼큰함"]
    },
    "갈비탕": {
        "category": "한식",
        "desc": "맑고 깊은 국물에 부드러운 갈비",
        "tags": ["#보양식", "#고급", "#맑은국물"]
    },
    "청국장": {
        "category": "한식",
        "desc": "구수하고 진한 콩의 맛이 살아있는 찌개",
        "tags": ["#구수함", "#건강", "#집밥"]
    },
    "알탕": {
        "category": "한식",
        "desc": "톡톡 터지는 알과 얼큰한 국물",
        "tags": ["#술안주", "#얼큰", "#해물"]
    },

    # 쌀쌀함/초겨울
    "온메밀": {
        "category": "일식",
        "desc": "따뜻한 쯔유 국물에 부드러운 메밀면",
        "tags": ["#담백", "#소화잘됨", "#따뜻"]
    },
    "잔치국수": {
        "category": "한식",
        "desc": "멸치 육수에 소면을 말아낸 깔끔한 맛",
        "tags": ["#가벼움", "#점심", "#깔끔"]
    },
    "일본 라멘": {
        "category": "일식",
        "desc": "진한 돈코츠 육수와 차슈의 조화",
        "tags": ["#진한맛", "#일본식", "#차슈"]
    },
    "베트남 쌀국수": {
        "category": "아시안",
        "desc": "깊은 고기 육수와 아삭한 숙주",
        "tags": ["#해장", "#가벼움", "#이국적"]
    },
    "샤브샤브": {
        "category": "퓨전",
        "desc": "끓는 육수에 살짝 익혀 먹는 고기와 야채",
        "tags": ["#건강식", "#다이어트", "#가족모임"]
    },
    "카레": {
        "category": "퓨전",
        "desc": "향신료의 향이 입맛을 돋우는 요리",
        "tags": ["#향신료", "#밥도둑", "#간편식"]
    },
    "스키야키": {
        "category": "일식",
        "desc": "달콤 짭짤한 소스에 졸여 날계란에 찍어먹는 요리",
        "tags": ["#단짠", "#고기", "#일본가정식"]
    },

    # 맑음
    "한강 라면": {
        "category": "간식",
        "desc": "야외에서 끓여 먹는 라면의 맛",
        "tags": ["#한강", "#피크닉", "#감성"]
    },
    "샌드위치": {
        "category": "양식",
        "desc": "신선한 야채와 햄, 치즈의 조화",
        "tags": ["#브런치", "#가벼움", "#피크닉"]
    },
    "수제버거": {
        "category": "양식",
        "desc": "육즙 가득한 패티와 풍성한 토핑",
        "tags": ["#미국맛", "#푸짐", "#육즙"]
    },
    "떡볶이": {
        "category": "분식",
        "desc": "매콤달콤 쫄깃한 국민 간식",
        "tags": ["#국민간식", "#매운맛", "#친구랑"]
    },
    "김밥": {
        "category": "분식",
        "desc": "다양한 재료를 한입에 즐기는 맛",
        "tags": ["#소풍", "#간편", "#든든"]
    },
    "토스트": {
        "category": "양식",
        "desc": "바삭하게 구운 식빵과 달콤한 소스",
        "tags": ["#간식", "#달달", "#아침"]
    },
    "도시락": {
        "category": "한식",
        "desc": "다양한 반찬을 골라 먹는 재미",
        "tags": ["#편의점", "#가성비", "#다양함"]
    },
    "샐러드": {
        "category": "양식",
        "desc": "신선한 채소로 즐기는 건강한 한 끼",
        "tags": ["#다이어트", "#건강", "#신선"]
    },
    "오코노미야끼": {
        "category": "일식",
        "desc": "양배추와 해물을 철판에 구워낸 일본식 전",
        "tags": ["#맥주안주", "#철판요리", "#일본식"]
    },

    # 활동적/따뜻함
    "초밥": {
        "category": "일식",
        "desc": "신선한 생선과 밥의 조화",
        "tags": ["#깔끔", "#고급", "#데이트"]
    },
    "치킨": {
        "category": "한식/퓨전",
        "desc": "바삭한 튀김 옷과 부드러운 속살",
        "tags": ["#치맥", "#야식", "#파티"]
    },
    "피자": {
        "category": "양식",
        "desc": "쭉 늘어나는 치즈와 다양한 토핑",
        "tags": ["#파티", "#배달", "#치즈"]
    },
    "연어덮밥": {
        "category": "일식",
        "desc": "부드러운 연어와 간장, 와사비의 조화",
        "tags": ["#덮밥", "#부드러움", "#건강"]
    },
    "파스타": {
        "category": "양식",
        "desc": "다양한 소스로 즐기는 이탈리아 면요리",
        "tags": ["#데이트", "#분위기", "#양식"]
    },
    "타코": {
        "category": "멕시칸",
        "desc": "또띠아에 싸먹는 이색적인 맛",
        "tags": ["#이국적", "#멕시칸", "#핑거푸드"]
    },
    "비빔면": {
        "category": "한식",
        "desc": "새콤달콤한 소스에 비벼먹는 차가운 면",
        "tags": ["#여름", "#입맛돋움", "#매콤달콤"]
    },
    "돈까스": {
        "category": "일식/경양식",
        "desc": "바삭하게 튀겨낸 돼지고기 요리",
        "tags": ["#점심", "#바삭", "#고기"]
    },
    "화덕피자": {
        "category": "양식",
        "desc": "화덕에서 구워내 도우가 쫄깃한 피자",
        "tags": ["#담백", "#이탈리안", "#데이트"]
    },
    "가츠동": {
        "category": "일식",
        "desc": "돈까스를 계란과 함께 졸여 밥 위에 얹은 덮밥",
        "tags": ["#든든", "#단짠", "#한그릇"]
    },

    # 더위
    "평양냉면": {
        "category": "한식",
        "desc": "슴슴하면서도 깊은 메밀 향과 육수",
        "tags": ["#매니아", "#시원", "#담백"]
    },
    "함흥냉면": {
        "category": "한식",
        "desc": "쫄깃한 면발과 매콤한 양념",
        "tags": ["#매콤", "#쫄깃", "#여름"]
    },
    "콩국수": {
        "category": "한식",
        "desc": "진하고 고소한 콩 국물",
        "tags": ["#고소함", "#여름별미", "#건강"]
    },
    "물회": {
        "category": "한식",
        "desc": "새콤달콤한 육수에 신선한 회",
        "tags": ["#바다", "#시원", "#새콤달콤"]
    },
    "냉모밀": {
        "category": "일식",
        "desc": "살얼음 동동 띄운 쯔유 국물",
        "tags": ["#깔끔", "#시원", "#여름"]
    },
    "오이냉국": {
        "category": "한식",
        "desc": "식초의 상큼함과 오이의 아삭함",
        "tags": ["#상큼", "#가벼움", "#입맛"]
    },
    "물냉면": {
        "category": "한식",
        "desc": "살얼음 육수가 뼛속까지 시원한 냉면",
        "tags": ["#국민여름음식", "#시원", "#갈비랑"]
    },
    "비빔냉면": {
        "category": "한식",
        "desc": "매콤한 양념장으로 입맛 살리는 냉면",
        "tags": ["#매콤", "#스트레스", "#고기랑"]
    }
}

def get_menu_candidates(weather_main, temp):
    """
    날씨 기반 추천에 '사용자 피드백 학습(Learning)'을 적용한 함수
    DB에서 좋아요/싫어요 기록을 가져와 메뉴별 가중치를 계산합니다.
    """
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

    try:
        conn = sqlite3.connect("yumpick_log.db")
        query = f"SELECT recommended_menu, reaction FROM user_logs"
        df = pd.read_sql(query, conn)
        conn.close()

        weights = []
        for menu in menus:
            score = 10
            
            if not df.empty:
                menu_logs = df[df['recommended_menu'] == menu]
                likes = len(menu_logs[menu_logs['reaction'] == 'like'])
                dislikes = len(menu_logs[menu_logs['reaction'] == 'dislike'])
                
                score = score + (likes * 5) - (dislikes * 5)
                
                if score <= 0:
                    score = 1
            
            weights.append(score)
        
        weighted_menus = []
        for menu, weight in zip(menus, weights):
            weighted_menus.extend([menu] * weight)
            
        return weighted_menus, comment

    except Exception as e:
        return menus, comment
