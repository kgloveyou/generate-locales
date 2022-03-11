# generateLocales

#### 介绍
- antd pro框架中locales文件夹内容导出xlxs文件，用于核对文案内容；
- 利用修改后的xlxs文件，自动生成对应的js/ts文件到项目代码中；
- 比较新旧xlxs文档，并在新文件中标记出变更（新增/修改）过的行；

#### 依赖
- python 3.8
- openpyxl


#### 安装教程

1.  安装python3.8

2.  安装对应的第三方库

```
pip install -r requirements.txt
```

#### 使用说明

1.  运行如下脚本，导出xlxs文件。

```
python ./output.py D:\\work_repos\\ad-hub-frontend\\src adhub.xlsx
```
**注意：**

admagic导出xlxs文件，请用专属脚本：

```bash
# admagic 导出专用
python ./export.py D:\\work_repos\\ad-magic-frontend\\annot-ui\\src admagic-ui.xlsx
python ./export.py D:\\work_repos\\ad-magic-frontend\\annot-core\\src admagic-core.xlsx
```

2.  运行如下脚本，根据目录中的xlsx文件生成antd pro locales文件。（**注意：自动生成的文件可能与源文件不同，不包含空行、注释行**）

```
python ./input.py ./adhub.xlsx
```

​	3.运行如下脚本，对比两份xlsx文件的差异。（第2个参数是旧文件路径，第3个参数是新文件路径）

```sh
python ./compare.py ./adhub-202201061032.xlsx ./adhub-20220121151836.xlsx
```

**说明：**

- 使用前尽可能确保en-US、zh-CN文件夹的目录结构相同，文件中的数据能对应上。（如果一种语言文件中记录缺失，则会根据另一种语言文件内容进行自动补充，Value将与Key保持一致）
- locales文件中，key和value使用的引号必须相同，即同时为单引号或双引号；不匹配的记录，导出excel时，将会丢弃。

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
