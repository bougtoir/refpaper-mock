import PySimpleGUI as sg
import subprocess

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('pub year(e.g.,"2020")'),sg.InputText()],
            [sg.Text(' pages  (e.g.,"1-10")'),sg.InputText()],
            [sg.Button('OK'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK':
        pub_year = values[0]
        pages = values[1]
        url_ = "https://pubmed.ncbi.nlm.nih.gov/?term={0}[Date - Publication] AND {1}[Pagination]".format(pub_year, pages)
        subprocess.Popen([r'C:\Program Files\Google\Chrome\Application\chrome.exe',url_])
              
window.close()