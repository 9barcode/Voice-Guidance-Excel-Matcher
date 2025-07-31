import os
import subprocess

# 사용자 입력
dlt_path = input("Input DLT path: ").strip()
output_path = input("Input path for output .txt file: ").strip()
dlt_viewer_folder = input("Input DLT_Viewer folder path: ").strip()

# dlt-viewer.exe 경로
dlt_viewer_path = os.path.join(dlt_viewer_folder, "dlt-viewer.exe")

# dlt-viewer.exe 확인
if not os.path.exists(dlt_viewer_path):
    print(f'ERROR: "{dlt_viewer_path}" not found!')
    input("Press Enter to exit...")
    exit(1)

# 출력 폴더 생성
os.makedirs(output_path, exist_ok=True)

# DLT 파일 변환
dlt_files = [f for f in os.listdir(dlt_path) if f.lower().endswith(".dlt")]

if not dlt_files:
    print("No .dlt files found in the specified path.")
else:
    for dlt_file in dlt_files:
        input_file = os.path.join(dlt_path, dlt_file)
        output_file = os.path.join(output_path, os.path.splitext(dlt_file)[0] + ".txt")
        print(f"Converting {dlt_file} ...")
        subprocess.run([dlt_viewer_path, "-t", "-u", "-c", output_file, input_file])

print("Done")
input("Press Enter to exit...")
