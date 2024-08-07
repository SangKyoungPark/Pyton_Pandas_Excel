import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from PIL import Image as PILImage
from datetime import datetime
# 현재 날짜 얻어오기
now = datetime.now()

formatted_date = now.strftime("%Y%m%d")

print(formatted_date)
strPath = "C:/GLIM_SERVER/LOG/LABEL_SHOT/" + formatted_date + "_BeforeShot.csv"
# strPath = "C:/Users/GLIM.23_30/OneDrive/바탕 화면/label.csv"

# CSV 파일 읽기csv'는 이미지 경로가 포함된 CSV 파일
df = pd.read_csv(strPath, encoding='cp949')

def column_index_to_letter(index):
    """Convert a column index (1-based) to a column letter."""
    result = ""
    while index > 0:
        index, remainder = divmod(index - 1, 26)
        result = chr(65 + remainder) + result
    return result

# 엑셀 워크북과 시트 생성
wb = Workbook()
ws = wb.active

# 헤더 작성
new_col = list(df.columns.values) + ['Crop Image']
ws.append(new_col)

# 각 이미지 경로에 대해 작업 수행
for index, row in df.iterrows():
  img_path = row['ImagePath']

  if '폭' in row['DefectName'] or '공차' in row['DefectName'] or '미스매치' in row['DefectName']:
    continue

  # 이미지 경로를 셀에 작성
  ws.append(list(row) + [""])

  # 이미지 열기
  img = PILImage.open(img_path)

  # 이미지를 엑셀 셀에 삽입
  img_for_excel = Image(img_path)
  img_for_excel.width = 128  # 이미지 너비 설
  img_for_excel.height = 128  # 이미지 높이 설정

  # 이미지 위치 설정 (B열에 이미지 삽입)
  img_cell = column_index_to_letter(len(new_col)) + '{}'.format(index + 2)
  ws.add_image(img_for_excel, img_cell)
  ws.row_dimensions[index].height = 100
  # break

wb.save('images_in_excel.xlsx')

# %%
