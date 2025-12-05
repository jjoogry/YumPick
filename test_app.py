import unittest
import os
import sqlite3
import pandas as pd
from modules import menus, db

class TestCityMapping(unittest.TestCase):
    """
    1. 도시 이름 매핑 기능 테스트
    사용자가 입력한 한글 도시명이 API 호출용 영문명으로 잘 변환되는지 확인합니다.
    """
    
    def test_major_cities(self):
        """주요 광역시/특별시 매핑 확인"""
        self.assertEqual(menus.city_map.get("서울"), "Seoul")
        self.assertEqual(menus.city_map.get("부산"), "Busan")
        self.assertEqual(menus.city_map.get("대구"), "Daegu")
        self.assertEqual(menus.city_map.get("인천"), "Incheon")
        self.assertEqual(menus.city_map.get("제주"), "Jeju")

    def test_gyeonggi_province(self):
        """경기도 주요 도시 매핑 확인"""
        self.assertEqual(menus.city_map.get("수원"), "Suwon")
        self.assertEqual(menus.city_map.get("성남"), "Seongnam")
        self.assertEqual(menus.city_map.get("용인"), "Yongin")
        self.assertEqual(menus.city_map.get("가평"), "Gapyeong")

    def test_gangwon_province(self):
        """강원도 주요 도시 매핑 확인"""
        self.assertEqual(menus.city_map.get("강릉"), "Gangneung")
        self.assertEqual(menus.city_map.get("춘천"), "Chuncheon")
        self.assertEqual(menus.city_map.get("속초"), "Sokcho")

    def test_invalid_city(self):
        """존재하지 않는 도시 입력 시 None 반환 확인"""
        self.assertIsNone(menus.city_map.get("없는도시"))
        self.assertIsNone(menus.city_map.get("와칸다"))


class TestMenuRecommendationLogic(unittest.TestCase):
    """
    2. 날씨별 메뉴 추천 로직 테스트
    날씨 상태(Rain, Snow 등)와 온도에 따라 적절한 후보군이 선정되는지 확인합니다.
    """

    def test_condition_rain(self):
        """비(Rain)가 올 때 추천 메뉴에 '파전'이 포함되어야 함"""
        candidates, comment = menus.get_menu_candidates("Rain", 20)
        self.assertIn("해물파전", candidates)
        self.assertIn("짬뽕", candidates)
        self.assertIn("비", comment)

    def test_condition_snow(self):
        """눈(Snow)이 올 때 추천 메뉴에 '군고구마'가 포함되어야 함"""
        candidates, comment = menus.get_menu_candidates("Snow", -5)
        self.assertIn("군고구마", candidates)
        self.assertIn("호빵", candidates)
        self.assertIn("눈", comment)

    def test_temp_freezing(self):
        """영하의 날씨(Clear, -5도)일 때 국물 요리 추천 확인"""
        candidates, comment = menus.get_menu_candidates("Clear", -5)
        self.assertIn("순대국", candidates)
        self.assertIn("김치찌개", candidates)
        self.assertNotIn("평양냉면", candidates)

    def test_temp_hot(self):
        """폭염(Clear, 35도)일 때 시원한 요리 추천 확인"""
        candidates, comment = menus.get_menu_candidates("Clear", 35)
        self.assertIn("평양냉면", candidates)
        self.assertIn("물회", candidates)
        self.assertNotIn("알탕", candidates)

    def test_temp_picnic(self):
        """좋은 날씨(Clear, 15도)일 때 피크닉 메뉴 추천 확인"""
        candidates, comment = menus.get_menu_candidates("Clear", 15)
        self.assertIn("샌드위치", candidates)
        self.assertIn("한강 라면", candidates)


class TestMenuDetails(unittest.TestCase):
    """
    3. 메뉴 상세 정보(딕셔너리) 조회 테스트
    MENU_DB에서 데이터를 올바르게 가져오는지 확인합니다.
    """

    def test_get_existing_menu(self):
        """존재하는 메뉴의 상세 정보 조회"""
        details = menus.get_menu_details("해물파전")
        self.assertEqual(details['category'], "한식")
        self.assertIn("#막걸리", details['tags'])

    def test_get_non_existing_menu(self):
        """존재하지 않는 메뉴 조회 시 빈 딕셔너리 반환"""
        details = menus.get_menu_details("랍스터구이")
        self.assertEqual(details, {})


class TestDatabaseOperations(unittest.TestCase):
    """
    4. 데이터베이스 연동 테스트 (Integration Test)
    실제 파일 생성 및 쓰기/읽기를 테스트합니다.
    테스트용 DB 파일(test_yumpick.db)을 별도로 만들어 테스트 후 삭제합니다.
    """
    
    TEST_DB_NAME = "test_yumpick.db"

    def setUp(self):
        """테스트 시작 전: 임시 DB 이름을 설정"""
        db.DB_NAME = self.TEST_DB_NAME
        db.init_db()

    def tearDown(self):
        """테스트 종료 후: 임시 DB 파일 삭제"""
        if os.path.exists(self.TEST_DB_NAME):
            os.remove(self.TEST_DB_NAME)

    def test_db_creation(self):
        """DB 파일이 생성되었는지 확인"""
        self.assertTrue(os.path.exists(self.TEST_DB_NAME))

    def test_add_and_retrieve_log(self):
        """로그 추가 후 조회가 잘 되는지 확인"""
        city = "TestCity"
        weather = "Clear"
        temp = 25.5
        menu = "TestMenu"
        reaction = "like"
        
        db.add_log(city, weather, temp, menu, reaction)

        df = db.get_all_logs()
        
        self.assertFalse(df.empty)
        self.assertEqual(len(df), 1)
        
        last_row = df.iloc[-1]
        self.assertEqual(last_row['city'], city)
        self.assertEqual(last_row['recommended_menu'], menu)
        self.assertEqual(last_row['reaction'], reaction)

if __name__ == '__main__':
    print("========================================")
    print(" YumPick 시스템 자동 테스트를 시작합니다.")
    print("========================================")
    unittest.main()