# !/usr/bin/env Python
# coding=utf-8

import sys
import datetime
import os
import codecs
import re
from openpyxl import Workbook
# from openpyxl.utils import get_column_letter


class Record(object):
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def en(self):
        return self._en

    @en.setter
    def en(self, value):
        self._en = value

    @property
    def zh(self):
        return self._zh

    @zh.setter
    def zh(self, value):
        self._zh = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


linePattern = re.compile(r"'(.+)':(?: +)'(.+)'(?:,?)")

localesPaths = []
enUSPaths = []
zhCNPaths = []

filesDict = {}

records = []


def get_locales(path):
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(
        os.path.join(path, i)) and not i.endswith('.umi')]
    if dirs:
        for i in dirs:
            if i.endswith('locales'):
                localesPaths.append(os.path.join(path, i))
            else:
                get_locales(os.path.join(path, i))


def tranverse_file(path_data):
    en_dir = path_data + "\\en-US"
    if os.path.isdir(en_dir) is True:
        for j in os.listdir(en_dir):
            enUSPaths.append(os.path.join(en_dir, j))

    zh_dir = path_data + "\\zh-CN"
    if os.path.isdir(zh_dir) is True:
        for k in os.listdir(zh_dir):
            zhCNPaths.append(os.path.join(zh_dir, k))


def readContent():
    for index in range(0, len(enUSPaths)):
        readFileContent(enUSPaths[index], zhCNPaths[index])


def readFileContent(enPath, zhPath):
    with open(enPath, mode='r', encoding='UTF-8') as files:
        for line in files:
            if not line.strip().startswith(r'//') and linePattern.search(line):
                arr = linePattern.split(line.strip())
                r = Record()
                r.key = arr[1].strip("'")
                r.en = arr[2].strip("'")
                r.path = enPath
                records.append(r)

    with open(zhPath, mode='r', encoding='UTF-8') as files:
        for line in files:
            if not line.strip().startswith(r'//') and linePattern.search(line):
                arr = linePattern.split(line.strip())
                rs = [i for i in records if i.key == arr[1].strip("'")]
                if len(rs) == 1:
                    rs[0].zh = arr[2].strip("'")


def exportXlsx(fileName='adhub.xlsx'):
    data = [['key', 'zh', 'en', 'path']]

    for r in records:
        data.append([r.key, r.en, r.zh, r.path])

    wb = Workbook()
    ws = wb.active
    for r in data:
        ws.append(r)
    wb.save(fileName)


def excetue():
    if len(sys.argv) != 3:
        print('参数个数不对')
        return

    srcPath = str(sys.argv[1])
    xlxsFile = str(sys.argv[2])

    get_locales(srcPath)

    for i in localesPaths:
        tranverse_file(i)

    readContent()

    exportXlsx(xlxsFile)

    print('---finished---')

if __name__ == '__main__':
    excetue()
