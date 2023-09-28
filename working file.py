from PIL import Image, ImageDraw, ImageFont
import openpyxl
import pandas
from openpyxl import Workbook, load_workbook
# book = load_workbook('menu.xlsx')
df = pandas.read_excel('menu.xlsx')
# dl = df.parse("Sheet1")

# sheet = book.active
# data = pandas.DataFrame(df, columns = ['ABCD'])
# print(img.size)
data = df['ABCD'][0]

fnt = ImageFont.truetype("consola.ttf", 19)
# fnt = ImageFont.truetype("corbeli.ttf", 19)
# names = sheet['A']
i = int(1)
# print(data[0].value)
for cell in df['ABCD']:
    img = Image.open('b.png')
    d = ImageDraw.Draw(img)
    x = (img.width - (d.textlength(cell, font=fnt))) // 2
    # d.text((160, 183), sheet['A'+str(i+1)].value, font = fnt, fill = (0, 0, 0))
    d.text((x, 185), cell, font = fnt, fill = (0, 0, 0))
    img.save('bb'+str(i+1)+'.png')
    i = i + 1