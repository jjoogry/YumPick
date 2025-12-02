# 🍽️ 오늘 뭐 먹지?
날씨 API를 활용한 식사 메뉴 추천 및 맛집 검색 서비스

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 프로젝트 소개
**OpenWeatherMap API**를 통해 실시간 날씨 정보를 가져오고, 기온과 날씨 상태를 분석해 **메뉴를 추천**해주는 프로그램입니다. 사용자는 추천 받은 메뉴를 **평가**할 수 있으며, **네이버 맛집 검색**과 연동하여 식당 정보까지 한 번에 얻을 수 있도록 구현하였습니다.

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
- **원클릭 검색:** 최정 결정된 메뉴와 지역명을 조합해 **네이버 지도 맛집 검색 링크** 제공

## 설치 및 실행 방법
1. 저장소 복제
2. 필수 라이브러리 설치
3. API 키 설정
4. 실행

## 사용 기술
- **Language:** Python3
- **Framework:** Streamlit
- **API:** OpenWeatherMap API
- **Library:** Requests, Random

## 발전 가능성
- 서울, 부산, 제주처럼 넓은 지역의 경우 지역구 단위의 날씨 데이터를 통한 **정교화된 추천 알고리즘** 구현 가능
- 단순 날씨 이외에도 식사 시간대와 함께 먹는 사람 등 **여러 옵션 추가**
- 여러 스폰서드 콘텐츠나 제휴 마케팅, 배너 광고 등을 통해 **수익 창출** 가능

## 라이선스
이 프로젝트는 **MIT License**를 따르므로, 누구나 자유롭게 수정 및 배포가 가능합니다.
