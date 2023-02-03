import PyPDF2
import sys
import subprocess


DEFAULT_OUTPUT_NAME = 'merge'
EXT = 'pdf'

merger = PyPDF2.PdfMerger()

paths=[]
if sys.argv[1:] != []:
    paths = sys.argv[1:] # DDされた全ファイルをpathsに格納
    paths.sort()
else:
    print('結合する順で、入力PDFをD&Dしてください')
    flag = True
    j=0
    while flag:
        j += 1
        input_path = input(f'{j}) ')
        if input_path == '': flag = False
        else:
            input_path = input_path.strip("'").strip('"') # 両端の''と""を削除
            paths.append(input_path)
    if paths == []: sys.exit()
    print() # 改行用


list = ''
for i, path in enumerate(paths, 1):
    list += str(i)+') '+path.replace('\\', '/')+'\n'
    try:
        merger.append(path)
    except PyPDF2.errors.PdfReadError: 
        print('==================================')
        print('⚠PDFファイル以外が含まれています')
        print('==================================\n')
        sys.exit()
    except FileNotFoundError:
        print('============================')
        print('⚠ファイルが見つかりません')
        print('============================\n')
        sys.exit()

subprocess.run('cls', shell=True)
print('入力PDF\n=======================')
print(list)

print(f'出力PDFの名前を入力してください (デフォルト値: {DEFAULT_OUTPUT_NAME})')
output = input(': ')
if output == '': output = DEFAULT_OUTPUT_NAME # input()が空ならデフォルト値をセット

output = ''.join(output.rsplit(EXT, 1)) # 末尾にEXT(=.pdf)がついていた場合削除する

merger.write(f'{output}.{EXT}')
merger.close()
