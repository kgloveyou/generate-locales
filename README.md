# generateLocales

#### 介绍
antd pro框架中locales文件夹内容导出xlxs文件，用于核对文案内容；同时，可以利用修改后的xlxs文件，自动生成对应的js/ts文件到项目代码中。

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

2.  运行如下脚本，根据目录中的xlsx文件生成antd pro locales文件。（**注意：自动生成的文件可能与源文件不同，不包含空行、注释行**）

```
python ./input.py ./adhub.xlsx
```

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
