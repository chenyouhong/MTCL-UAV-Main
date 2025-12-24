import os
import pandas as pd
from pathlib import Path

# 设置路径
root_dir = Path("./dataset/ALFA/train")
output_file = Path("./dataset/ALFA/train.csv")
all_data = []

# 遍历目录
for folder in root_dir.iterdir():
    # 筛选正常样本文件夹 (no_failure 或 no_ground_truth)
    if folder.is_dir() and ("no_failure" in folder.name or "no_ground_truth" in folder.name):
        csv_path = folder / "mavros-imu-data.csv"
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            df['label'] = 0  # 手动添加标签列：0 代表正常
            all_data.append(df)
            print(f"已处理: {folder.name}")

# 合并并保存
if all_data:
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"成功合并 {len(all_data)} 个文件至 {output_file}")