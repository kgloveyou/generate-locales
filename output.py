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
    def __init__(self, key='', en='', zh='', path=''):
        self._key = key
        self._en = en
        self._zh = zh
        self._path = path

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
linePattern2 = re.compile(r'"(.+)":(?: +)"(.+)"(?:,?)')

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


def get_files(path, lang):
    # print(path)
    if os.path.isfile(path):
        if lang == 'en-US':
            enUSPaths.append(os.path.join(path))
        else:
            zhCNPaths.append(os.path.join(path))
        return

    lsdir = os.listdir(path)
    dirs = [i for i in lsdir]
    if dirs:
        for i in dirs:
            if os.path.isdir(os.path.join(path, i)):
                get_files(os.path.join(path, i), lang)
            else:
                if lang == 'en-US':
                    enUSPaths.append(os.path.join(path, i))
                else:
                    zhCNPaths.append(os.path.join(path, i))


def tranverse_file(path_data):
    en_dir = path_data + "\\en-US"
    # print(en_dir)
    if os.path.isdir(en_dir) is True:
        for j in os.listdir(en_dir):
            # print(os.path.join(en_dir, j))
            get_files(os.path.join(en_dir, j), 'en-US')
    elif os.path.isfile(en_dir +'.ts') is True:
        get_files(os.path.join(en_dir +'.ts'), 'en-US')
    elif os.path.isfile(en_dir +'.js') is True:
        get_files(os.path.join(en_dir +'.js'), 'en-US')

    zh_dir = path_data + "\\zh-CN"
    # print(zh_dir)
    if os.path.isdir(zh_dir) is True:
        for k in os.listdir(zh_dir):
            # print(os.path.join(zh_dir, k))
            get_files(os.path.join(zh_dir, k), 'zh-CN')
    elif os.path.isfile(zh_dir +'.ts') is True:
        get_files(os.path.join(zh_dir + '.ts'), 'zh-CN')
    elif os.path.isfile(zh_dir +'.js') is True:
        get_files(os.path.join(zh_dir + '.js'), 'zh-CN')

def readContent2():
    # 中文文件对应的英文文件
    expectEnPaths = [i.replace('zh-CN', 'en-US') for i in zhCNPaths]

    unionEnPath = set(enUSPaths) | set(expectEnPaths)

    for e in unionEnPath:
        if e in enUSPaths:
            enPath = e
        else:
            enPath = None

        searchCnPath = e.replace('en-US', 'zh-CN')

        if searchCnPath in zhCNPaths:
            cnPath = searchCnPath
        else:
            cnPath = None
        
        readFileContent(enPath, cnPath)

def readContent():
    enCount = len(enUSPaths)
    zhCount = len(zhCNPaths)

    # 英文文件多
    if enCount > zhCount or enCount == zhCount:
        for i in range(0, enCount):
            expectZhPath = enUSPaths[i].replace('en-US', 'zh-CN')
            # 存在同名文件
            if expectZhPath in zhCNPaths:
                index = zhCNPaths.index(expectZhPath)
                readFileContent(enUSPaths[i], zhCNPaths[index])
            else:
                readFileContent(enUSPaths[i], None)

    else:
        # 中文文件多
        for j in range(0, zhCount):
            expectEnPath = zhCNPaths[j].replace('zh-CN', 'en-US')
            # 存在同名文件
            if expectEnPath in enUSPaths:
                index = enUSPaths.index(expectEnPath)
                readFileContent(enUSPaths[index], zhCNPaths[j])
            else:
                readFileContent(None, zhCNPaths[j])


def readFileContent(enPath, zhPath):
    # 中英文文件都存在
    if enPath and zhPath:
        with open(enPath, mode='r', encoding='UTF-8') as files:
            for line in files:
                stripLine = line.strip()
                if not stripLine.startswith(r'//'):
                    if linePattern.search(stripLine):
                        arr = linePattern.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip("'")
                        r.en = arr[2].strip("'")
                        r.path = enPath
                        records.append(r)
                    elif linePattern2.search(stripLine):
                        arr = linePattern2.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip('"')
                        r.en = arr[2].strip('"')
                        r.path = enPath
                        records.append(r)

        with open(zhPath, mode='r', encoding='UTF-8') as files:
            for line in files:
                stripLine = line.strip()
                if not stripLine.startswith(r'//'):
                    if linePattern.search(stripLine):
                        arr = linePattern.split(stripLine)
                        rs = [i for i in records if i.path == zhPath.replace('zh-CN', 'en-US') and i.key == arr[1].strip("'")]
                        if len(rs) == 1:
                            rs[0].zh = arr[2].strip("'")
                        # 中文存在，英文不存在
                        elif len(rs) == 0:
                            r = Record()
                            r.key = arr[1].strip("'")
                            r.zh = arr[2].strip("'")
                            r.path = enPath
                            records.append(r)
                    elif linePattern2.search(stripLine):
                        arr = linePattern2.split(stripLine)
                        rs = [i for i in records if i.path == zhPath.replace('zh-CN', 'en-US') and i.key == arr[1].strip('"')]
                        if len(rs) == 1:
                            rs[0].zh = arr[2].strip('"')
                        # 中文存在，英文不存在
                        elif len(rs) == 0:
                            r = Record()
                            r.key = arr[1].strip('"')
                            r.zh = arr[2].strip('"')
                            r.path = enPath
                            records.append(r)            

    # 只有英文文件                            
    if enPath and not zhPath:
        with open(enPath, mode='r', encoding='UTF-8') as files:
            for line in files:
                stripLine = line.strip()
                if not stripLine.startswith(r'//'):
                    if linePattern.search(stripLine):
                        arr = linePattern.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip("'")
                        r.en = arr[2].strip("'")
                        r.path = enPath
                        records.append(r)
                    elif linePattern2.search(stripLine):
                        arr = linePattern2.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip('"')
                        r.en = arr[2].strip('"')
                        r.path = enPath
                        records.append(r)
    # 只有中文文件
    if not enPath and zhPath:
        with open(zhPath, mode='r', encoding='UTF-8') as files:
            for line in files:
                stripLine = line.strip()
                if not stripLine.startswith(r'//'):
                    if linePattern.search(stripLine):
                        arr = linePattern.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip("'")
                        r.zh = arr[2].strip("'")
                        r.path = zhPath
                        records.append(r)
                    elif linePattern2.search(stripLine):
                        arr = linePattern2.split(stripLine)
                        r = Record()
                        r.key = arr[1].strip('"')
                        r.zh = arr[2].strip('"')
                        r.path = zhPath
                        records.append(r)

def exportXlsx(fileName='adhub.xlsx'):
    data = [['key', 'zh-CN', 'en-US', 'path']]

    for r in records:
        data.append([r.key, r.zh, r.en, r.path])

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

    # for i in localesPaths:
    #     print(i)

    for i in localesPaths:
        tranverse_file(i)

    # for i in enUSPaths:
    #     print(i)
    # for i in zhCNPaths:
    #     print(i)

    # readContent()
    readContent2()

    exportXlsx(xlxsFile)

    print('---finished---')


if __name__ == '__main__':
    excetue()
