import re
import pandas as pd
import os

# 사용자 입력 (폴더 경로)
folder_path = input("텍스트 파일이 들어있는 폴더 경로를 입력하세요: ").strip()
txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

sentences = []
current_group = []

for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    print(f"파일 처리 중: {txt_file}")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # 줄 안에 sentence[숫자] : 값 형태 찾기
            match = re.search(r"voice\s*\[\s*(\d+)\s*\]\s*:\s*(.*)", line, re.IGNORECASE)
            if not match:
                continue

            index = int(match.group(1))
            content = match.group(2).strip()

            # "None"이거나 비어있으면 제외
            if not content or content.lower() == "none":
                continue

            # 문장 내 " - PL,pl" 제거
            content = re.sub(r"\s*-\s*.", "", content)

            # sentence[0] 이면 이전 그룹 저장하고 새 그룹 시작
            if index == 0 and current_group:
                sentences.append(" ".join(current_group))
                current_group = [content]
            else:
                current_group.append(content)

# 마지막 그룹도 저장
if current_group:
    sentences.append(" ".join(current_group))

# DataFrame 생성
df = pd.DataFrame(sentences, columns=["voice"])

# CSV 저장
output_file = os.path.join(folder_path, "result.csv")
df.to_csv(output_file, index=False, encoding="utf-8-sig")

# 결과 출력
print("\n 정제된 문장들:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

print(f"\n CSV 파일 저장 완료: {output_file}")
