import os

from openpyxl import load_workbook

records = []

# 读取xlxs内容


def loadXlsx():
    wb = load_workbook(filename='adhub.xlsx')
    ws = wb['Sheet']

    print(ws.max_row, ws.max_column)

    records = [[0 for i in range(ws.max_column)] for j in range(ws.max_row)]

    # print(records)
    index = 0

    for row in ws.rows:
        # print(row[0].value, row[1].value, row[2].value, row[3].value)
        records[index][0] = row[0].value
        records[index][1] = row[1].value
        records[index][2] = row[2].value
        records[index][3] = row[3].value
        index = index + 1

    # for index in range(ws.max_row):
    #   records[index][0] = ws.rows[index][0].value
    #   records[index][1] = ws.rows[index][1].value
    #   records[index][2] = ws.rows[index][2].value
    #   records[index][3] = ws.rows[index][3].value

    wb.close()

    createFie(
        r'c:\work_repos\ad-hub-frontend\src\locales\en-US\exception.js', records[0: 10])

# 创建ts/js文件，并写入locales内容


def createFie(fileName, fileRecords):

    if not os.path.exists(os.path.dirname(fileName)):
        os.makedirs(os.path.dirname(fileName))

    if not os.path.exists(fileName):
        os.system(r"touch {}".format(fileName))  # 调用系统命令行来创建文件

    # 读写打开一个UTF-8编码格式文件，如果文件不存在则创建
    file = open(fileName, mode='w+', encoding='UTF-8')
    # open()打开一个文件，返回一个文件对象
    file.write('export default {\n')  # 写入文件

    for r in fileRecords:
        file.write("  '{key}': '{value}',\n".format(key=r[0], value=r[1]))  # 写入文件

    file.write('}')  # 写入文件
    # file.seek(0)  # 光标移动到文件开头
    # file_content = file.read()  # 读取整个文件内容
    # print(file_content)
    file.close()  # 关闭文件


if __name__ == '__main__':
    loadXlsx()
