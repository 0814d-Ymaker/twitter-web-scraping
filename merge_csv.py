import csv

# 已经合并并去重的前 10540 条数据
files = [
    r'Trump/Trump_all_10540_unique.csv',

    # 最后补抓的 1000 条数据
    r'Trump/2026-09-30 15-21-43-text.csv'
]

rows = []
seen = set()
header = None

for file in files:
    with open(file, 'r', encoding='utf-8-sig', newline='') as f:
        data = list(csv.reader(f))

    if header is None:
        header = data[:2]

    for row in data[2:]:

        # 确保这一行包含完整字段
        if len(row) <= 4:
            continue

        # 只保留正文中明确包含 Trump 的推文
        if 'trump' not in row[4].lower():
            continue

        # 按 Tweet URL 去重
        if row[3] in seen:
            continue

        seen.add(row[3])
        rows.append(row)

print('筛选后符合条件且不重复的推文：', len(rows))

# 只保留前 10000 条
final_rows = rows[:10000]

with open(
    r'Trump/Trump_10000_tweets.csv',
    'w',
    encoding='utf-8-sig',
    newline=''
) as f:
    writer = csv.writer(f)
    writer.writerows(header)
    writer.writerows(final_rows)

print('最终文件已生成')
print('最终推文数量：', len(final_rows))