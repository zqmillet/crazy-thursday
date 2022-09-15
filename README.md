# crazy-thursday

![](https://img.shields.io/badge/KFC-Crazy--Thursday-brightgreen)
![](https://img.shields.io/badge/Powered%20by-Github%20Action-brightgreen)

大家好, 我是秦始皇, 其实我并没有死, 我在西安有 100000 吨黄金, 今天肯德基疯狂星期四, 谁可以 V 我 50 元, 我明天直接带部队复活, 让你统领三军!

## 安装 

``` bash
pip3 install crazy-thursday
```

或者
```
python3 -m pip install crazy-thursday
```

## 使用

如果成功安装, 系统中便会存在一个名为 ``crazy-thursday`` 的命令. 直接调用 ``crazy-thursday`` 便会在控制台中输出一段疯狂星期四文案.

``` text
$ crazy-thursday
大家好, 我是秦始皇, 其实我并没有死, 我在西安有 100000 吨黄金, 今天肯德基疯狂星期四, 谁可以 V 我 50 元, 我明天直接带部队复活, 让你统领三军!
```

## 如何贡献

你不需要贡献代码, 只需要[创建 issue](https://github.com/zqmillet/crazy-thursday/issues/new), 并且留下文案即可.
后台有一个定时任务, 定时收集本项目的所有 issue, 并汇总打包成 ``.whl`` 文件, 发布到 [PyPI](https://pypi.org/project/crazy-thursday/) 上.

值得注意的是, 一个 issue 由两部分组成: Title 和 Comment.

- Title 是必填项, 只能有一行.
- Comment 是选填项, 可以有多行, 并且支持 Markdown.

如果你的文案只有一行, 可以把文案写在 Title 中, Comment 留空; 如果你的文案很长, 分段落, 则需要将文案写在 Comment 中.

在执行 ``crazy-thursday`` 命令时, 会优先显示 Comment 中的内容, 如果 Comment 内容为空, 则显示 Title 中的内容.

## 工作原理

本项利用 Github Action 每天自动发布版本, 其工作原理如下图所示.

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#FFFFFF", "primaryBorderColor": "#000000"}}}%%

graph TD
    A("☁️ https://github.com/zqmillet/crazy-thursday") -->|collect issues| B("📄 crazy_thursday/corpus.jsonl")
    B -->|update version| C("📄 crazy_thursday/__init__.py") 
    C --> |commit & push| D("☁️ https://github.com/zqmillet/crazy-thursday")
    D --> |build| E("📦 dist/crazy_thursday-*.whl")
    E --> |publish| F("🌐 https://pypi.org/project/crazy-thursday")
```


