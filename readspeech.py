import os
import json
import csv

def json_to_csv(json_folder, output_csv):
    files = [f for f in os.listdir(json_folder) if f.startswith("Day_") and f.endswith(".json")]
    
    with open(output_csv, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["speech_id", "user_id", "user_name", "speech_corpus", "num_approves", "num_follows", "num_opposes", "published_date", "published_time", "published_place", "source_file"])
        
        for file in files:
            file_path = os.path.join(json_folder, file)
            with open(file_path, 'r', encoding='utf-8-sig') as json_file:
                data = json.load(json_file)
                for speech in data.get("speeches", []):
                    writer.writerow([
                        speech.get("speech_id", ""),
                        speech.get("user_id", ""),
                        speech.get("user_name", ""),
                        speech.get("speech_corpus", ""),
                        speech.get("num_approves", ""),
                        speech.get("num_follows", ""),
                        speech.get("num_opposes", ""),
                        speech.get("published_date", ""),
                        speech.get("published_time", ""),
                        speech.get("published_place", ""),
                        file
                    ])
    
    print(f"CSV 文件已生成：{output_csv}")

# 运行脚本
json_folder = "speechs1001_1449"
output_csv = "output2.csv"
json_to_csv(json_folder, output_csv)