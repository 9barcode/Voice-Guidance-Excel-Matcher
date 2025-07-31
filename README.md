## Voice-Guidance-Excel-Matcher Tool

자동차 소프트웨어 테스트 업무 중 음성안내 로그만 분류하여 Excel 결과 문서와 매칭.
결과 문서와 실제 음성안내를 비교하는 시간을 절감하기 위해 개발한 Python 기반 자동화 도구입니다.  
Pandas 등 실무에서 사용하는 주요 기술을 적용하여 실제 업무에 투입 가능한 수준으로 구현되었습니다.

---

## 주요 기능

- ✔️ 음성안내만 dlt 로그에서 추출 후 excel 문서의 결과랑 매칭
- ✔️ 로그 정제 및 조건 필터링 기능
- ✔️ 반복작업 자동화
- ✔️ bat 파일을 실행하여 py 파일들을 실행.

---

## 🛠️ 사용 기술

| 분류 | 내용 |
|------|------|
| 언어 | Python 3.13 |
| 라이브러리 | Pandas, openpyxl |
| 배포 환경 | GitHub (Windows 기준 테스트) |
convert_to_txt.py | language 로그를 UTF-8 형식으로 추출하기 위해 txt 파일로 우선 추출하는 과정이며 dlt viewer의 plagin 사용.
sentence_filter_text.py | txt 파일들을 전부 모아 필요한 데이터만 추출하여 csv 파일로 parser 하는 과정.
matching_machine.py | parser한 csv 파일과 Test 엑셀 문서와의 셀 매칭을 통해 음성안내 Test case 처리.


---

## 📂 폴더 구조

```plaintext
kpi_calculator/
├── convert_to_txt.py
├── matching_machine.py
├── sentence_filter_text.py
├── Sentence_matching.bat
└── README.md
```


🎯 개발 배경
해당 도구는 실제 차량 내비게이션 QA 업무 중
KPI 계산, 반복 데이터 필터링 및 보고서 생성의 반자동화를 위해 개발되었습니다.
테스트 자동화 전환 및 데이터 기반 업무 개선을 위한 개인 역량 강화 프로젝트로 활용되었습니다.
Tool의 틀은 동일하나 실제 dlt log 내용을 넣지 않고 dummy 값들을 넣었습니다. 

🙋‍♂️ 개발자 정보
이름: Hyeongju Kwon

경력: 자동차 내비게이션 소프트웨어 QA

관심 분야: QA 자동화, Python 기반 도구 개발, 차량 소프트웨어 테스트
