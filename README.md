# 🍽️ 오늘 뭐 먹지?
날씨 API와 사용자 피드백 루프를 결합한 식사 메뉴 추천 및 맛집 검색 서비스 

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Data_Persistence-003B57?style=flat&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 프로젝트 소개
 **OpenWeatherMap API**를 통해 실시간 날씨 정보를 가져오고, 기온과 날씨 상태를 분석해 **메뉴를 추천**해주는 프로그램입니다. 단순한 규칙 기반 추천을 넘어 사용자의 선택 데이터를 학습하여 추천 품질을 지속적으로 향상시키는 지능형 메뉴 추천 시스템입니다. 과거 사용자들의 반응 데이터를 분석해 메뉴별 가중치를 동적으로 조정하는 **Weighted Random Algorithm**을 적용했습니다. [(웹사이트 실행)](https://yumpick-hu3xzwekjvyewtffh7z4uq.streamlit.app/)

## 주요 기능
- **실시간 날씨 조회:** OpenWeatherMap API를 연동하여 전 세계 도시의 날씨 확인
- **대한민국 도시명 한글 지원:** 서울, 부산, 제주 등 한국어 지명 입력 시 자동 영문 변환
- **메뉴 추천:** 기온과 날씨에 따른 메뉴 추천 알고리즘
- **사용자 피드백:** 추천 메뉴가 마음에 들지 않을 경우 '별로에요' 기능 제공
- **원클릭 검색:** 최종 결정된 메뉴와 지역명을 조합해 **네이버 지도 맛집 검색 링크** 제공

## 핵심 알고리즘: 피드백 기반 가중치
단순 랜덤 추천이 아닌, **사용자 로그 데이터**를 기반으로 추천 확률을 보정하는 알고리즘을 구현했습니다. 기본 점수에 **좋아요**를 클릭할 경우 보상 계수 5점을, **별로에요**를 클릭할 경우 패널티 계쑤 -5점을 부여했습니다. 이 알고리즘을 통해 서비스 사용량이 늘어날수록 네트워크 효과가 발생하고 이를 통해 검증된 메뉴들이 주로 추천될 수 있는 시스템으로 발전하고자 합니다.

## 사용자 실행 화면
1. 초기 화면
<img width="1608" height="967" alt="초기화면" src="https://github.com/user-attachments/assets/72f2f7b9-0ef9-42ae-a033-87786436e5d2" />
2. '좋아요' 선택
<img width="1608" height="967" alt="좋아요" src="https://github.com/user-attachments/assets/78ca976f-2ea7-4d84-9f93-7b07655d73db" />
3. '별로에요' 선택
<img width="1608" height="967" alt="별로에요" src="https://github.com/user-attachments/assets/1957e73c-44d0-4e98-b7e0-3bb8871cedb6" />

## 관리자 페이지 실행 화면
1. 초기 화면
<img width="1608" height="967" alt="관리자 초기화면" src="https://github.com/user-attachments/assets/30df95f8-f2c8-495f-a7ba-ebfff92b2510" />
2. 분석 결과
<img width="1608" height="967" alt="사용자기록" src="https://github.com/user-attachments/assets/c868fe5b-cce1-4321-b47c-e1a66fcad7bd" />

## 개발 과정에서의 고민
- **데이터 지속성 및 학습 루프:** Streamlit은 클릭할 때마다 전체 코드가 재실행되는 특성을 가져 '별로에요' 버튼 클릭 시 기존에 불러온 데이터와 추천 리스트가 **휘발되는 문제**가 발생했습니다. 이를 해결하기 위해 'st.session_state'를 도입하여 메모리상에 날씨 정보와 추천 리스트를 캐싱했습니다. 또한 **SQLite DB Integration**을 통해 세션이 종료된 후에도 데이터를 활용해 **가중치 알고리즘**에 반영되어 추천 품질을 향상시켰습니다.
- **API 안정성 확보:** OpenWeatherMap API가 한글 도시명을 제대로 인식하지 못하는 문제가 있어 이를 해결하고자 국내 도시 데이터를 직접 영문명과 매핑하는 **전처리 로직**을 구축했습니다.
- **사용자 유도형 UX/UI 설계:** 단순 텍스트 추천을 실제 식사 메뉴 선택까지 이어지기 어려워 추천 결과와 위치 정보를 결한한 **네이버 지도 맛집 검색 링크**를 제공했습니다. 또한, 사용자의 편의를 고려해 레이아웃을 수정하였으며 이 과정에서 'st.columns'와 'st.form' 등을 사용했습니다.
- **모듈형 아키텍처:** 초기에는 하나의 파일에 모든 로직을 집중시켰지만 확장성이 낮아 이를 개선하고자 UI, 데이터, 메뉴, 날씨로 코드를 분리해 구조적 완성도를 높였습니다.

## 설치 및 실행 방법
1. 저장소 복제
```bash
git clone [https://github.com/jjoogry/YumPick.git](https://github.com/jjoogry/YumPick.git)
cd YumPick
```
2. 필수 라이브러리 설치
```bash
pip install -r requirements.txt
```
3. API 키 설정 확인 (만료 시 weather.py 코드에 입력)
```python
API_KEY = "키_입력"
```
4. 실행
```bash
streamlit run app.py
```
- 관리자 페이지의 비밀번호는 '1234'로 설정

## 사용 기술
- **Language:** Python3
- **Framework:** Streamlit
- **API:** OpenWeatherMap API
- **Databse:** SQLite3
- **Data Analysis:** Pandas

## 발전 가능성
- 서울, 부산, 제주처럼 넓은 지역의 경우 지역구 단위의 날씨 데이터를 통한 **정교화된 추천 알고리즘** 구현 가능
- 단순 날씨 이외에도 식사 시간대와 함께 먹는 사람 등 **여러 옵션 추가**
- 여러 스폰서드 콘텐츠나 제휴 마케팅, 배너 광고 등을 통해 **수익 창출** 가능
- **사용자 위치 기반** 자동 도시 인식 기능을 도입해 지역 입력 없이 수행 가능
- 현재의 가중치 알고리즘을 RandomForest Classifier로 대체해 **ML 모델 고도화** 가능

## 참고 자료
- [Streamlit Official Documentation](https://docs.streamlit.io)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)

## 라이선스
이 프로젝트는 **MIT License**를 따르므로, 누구나 자유롭게 수정 및 배포가 가능합니다.
