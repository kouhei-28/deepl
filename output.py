import deepl
import docx
import glob
import os
import shutil


API_KEY = 'af8b9802-207d-2d98-20e7-05985839ff75:fx' # 自身の API キーを指定
source_lang = 'EN'
target_lang = 'JA'

# イニシャライズ
translator = deepl.Translator(API_KEY)

if glob.glob("*.docx"):
    doc = docx.Document(glob.glob("*.docx")[0])
else:
    doc = docx.Document()

if not glob.glob("Archive"):
    os.mkdir("Archive")

txts = glob.glob("*.txt")

for txt in txts:
    doc.add_paragraph(txt.replace("_", " ").replace(".txt", ""))
    doc.paragraphs[-1].runs[0].bold = True
    doc.paragraphs[-1].runs[0].font.size = docx.shared.Pt(16)

    f = open(txt, 'r', encoding="utf-8")

    for text in f.readlines():
        # 翻訳を実行
        result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
        # 段落の末尾に追加
        doc.add_paragraph(result.text)

    f.close()
    shutil.move(txt, "./Archive/")

doc.save("Sample.docx")