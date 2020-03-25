# クラスのインポート
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

# TrueType
from reportlab.pdfbase import ttfonts

# TrueTypeフォントの登録
pdfmetrics.registerFont(ttfonts.TTFont("UD-Digital", "C:\\windows\\Fonts\\UDDigiKyokashoN-B.ttc"))

# PDFを作る
pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4)

title = "新春セール！"
for moji in title:
    # フォントの大きさは用紙横幅と同じ210mmとする
    # フォントの種類は、TTFFontの1番目の引数に指定したもの
    pdf.setFont("UD-Digital", 210 * unit.mm)
    # 高さ
    h = (297 - 210) / 2 * unit.mm

    pdf.drawString(0 * unit.mm, h, moji)
    pdf.showPage()

# 保存
pdf.save()
