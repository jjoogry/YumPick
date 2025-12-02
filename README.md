# 🍽️ 오늘 뭐 먹지?
날씨 API를 활용한 식사 메뉴 추천 및 맛집 검색 서비스 

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 프로젝트 소개
**OpenWeatherMap API**를 통해 실시간 날씨 정보를 가져오고, 기온과 날씨 상태를 분석해 **메뉴를 추천**해주는 프로그램입니다. 사용자는 추천 받은 메뉴를 **평가**할 수 있으며, **네이버 맛집 검색**과 연동하여 식당 정보까지 한 번에 얻을 수 있도록 구현하였습니다. [(웹사이트 실행)](https://yumpick-hu3xzwekjvyewtffh7z4uq.streamlit.app/)

## 실행 화면
1. 초기 화면
<img width="1608" height="967" alt="초기화면" src="https://github.com/user-attachments/assets/72f2f7b9-0ef9-42ae-a033-87786436e5d2" />
2. '좋아요' 선택
<img width="1608" height="967" alt="좋아요" src="https://github.com/user-attachments/assets/78ca976f-2ea7-4d84-9f93-7b07655d73db" />
3. '별로에요' 선택
<img width="1608" height="967" alt="별로에요" src="https://github.com/user-attachments/assets/1957e73c-44d0-4e98-b7e0-3bb8871cedb6" />

## 주요 기능
- **실시간 날씨 조회:** OpenWeatherMap API를 연동하여 전 세계 도시의 날씨 확인
- **대한민국 도시명 한글 지원:** 서울, 부산, 제주 등 한국어 지명 입력 시 자동 영문 변환
- **메뉴 추천:** 기온과 날씨에 따른 메뉴 추천 알고리즘
- **사용자 피드백:** 추천 메뉴가 마음에 들지 않을 경우 '별로에요' 기능 제공
- **원클릭 검색:** 최종 결정된 메뉴와 지역명을 조합해 **네이버 지도 맛집 검색 링크** 제공

## 개발 과정에서의 고민
- **API 안정성 확보:** 사용자가 입력하는 한국어 도시명을 OpenWeatherMap API가 인식하지 못하는 문제를 해결하기 위해 국내 도시 데이터를 직접 딕셔너리 형태로 매핑하여 즉시 변환되도록 구현했습니다.
- **Streamlit의 세션 상태 관리:** Streamlit은 버튼을 클릭할 때마다 코드가 다시 실행되기 때문에 '별로에요' 버튼을 누르면 기존 날씨 데이터까지 휘발되는 문제가 발생했습니다. 이를 해결하기 위해 'st.session_state'를 도입하였고 날씨 정보와 추천된 메뉴 리스트를 메모리에 캐싱했습니다.
- **사용자 행동 유도:** 단순히 메뉴를 추천하고 끝내는 것보다 사용자가 정말 추천받은 메뉴를 식사하기까지의 행동을 유도하기 위해 추천 결과와 사용자가 입력한 위치를 결합해 '네이버 지도 맛집 검색 링크'를 생성했습니다.
- **직관적인 UI 구성:** Streamlit의 기본 레이아웃을 사용하면 텍스트 입력창과 실행 버튼의 배치가 부자연스러워 'st.columns'를 활용해 화면 비율을 분할하고 'vertical_alignment="bottom"' 속성을 적용하여 버튼의 하단 라인을 일치시켰습니다. 또한, '네이버 지도 맛집 검색 링크'는 전체 너비를 사용하고 네이버의 상징색인 초록색을 적용하여 사용자의 시선이 자연스럽게 이어지도록 설정했습니다.

## 설치 및 실행 방법
1. 저장소 복제
```bash
git clone https://github.com/jjoogry/YumPick.git
```
2. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```
3. API 키 설정 확인 (만료 시 app.py 코드에 입력)
```python
API_KEY = "키_입력"
```
4. 실행
```bash
streamlit run app.py
```

## 사용 기술
- **Language:** Python3
- **Framework:** Streamlit
- **API:** OpenWeatherMap API
- **Library:** Requests, Random

## 발전 가능성
- 서울, 부산, 제주처럼 넓은 지역의 경우 지역구 단위의 날씨 데이터를 통한 **정교화된 추천 알고리즘** 구현 가능
- 단순 날씨 이외에도 식사 시간대와 함께 먹는 사람 등 **여러 옵션 추가**
- 여러 스폰서드 콘텐츠나 제휴 마케팅, 배너 광고 등을 통해 **수익 창출** 가능
- **사용자 위치 기반** 자동 도시 인식 기능을 도입해 지역 입력 없이 수행 가능

## 참고 자료
- [Streamlit Official Documentation](https://docs.streamlit.io)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)

## 라이선스
이 프로젝트는 **MIT License**를 따르므로, 누구나 자유롭게 수정 및 배포가 가능합니다.
