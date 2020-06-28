# HoshinoBot(キャル)

基于酷Q与HoshinoBot的魔改(?)bot


## 简介

**HoshinoBot:** 基于 [nonebot](http://nonebot.cqp.moe) 框架，开源、无公害、非转基因的QQ机器人。



## 功能介绍&搭建方法

HoshinoBot 的功能开发以服务 [公主连结☆Re:Dive](http://priconne-redive.jp) 玩家为核心，详细功能及搭建方法见原版[Hoshino](http://github.com/Ice-Cirno/HoshinoBot)


#### 静态图片&音频资源

> 发送图片的条件：  
> 1. 酷Q Pro版  
> 2. 将`config.py`中的`USE_CQPRO`设为`True`  
> 3. 静态图片资源

> 发送语音的条件：
> 1. 同上1.
> 2. 同上2.
> 3. 已安装酷Q Pro的[语音插件](https://cqp.cc/forum.php?mod=viewthread&tid=21132&highlight=%E8%AF%AD%E9%9F%B3)
> 4. 音频资源

您可能希望看到更为精致的图片版结果，若希望机器人能够发送图片or角色语音，首先需要您购买酷Q Pro版，其次需要准备静态图片&音频资源，其中包括：

- 公主连接角色头像（来自 [干炸里脊资源站](https://redive.estertion.win/) 的拆包）
- 公主连接官方四格漫画
- 公主连接每月rank推荐表
- 表情包杂图
- setu库
- [是谁呼叫舰队](http://fleet.diablohu.com/)舰娘&装备页面截图
- 艦これ人事表
- 整合过的语音包

等资源。自行收集可能较为困难，所以我们准备了一个较为精简的资源包以及下载脚本，可以满足公主连接相关功能的日常使用。如果需要，请加入QQ群 **Hoshino的后花园** 367501912，下载群文件中的`res.zip`。（有关音频资源及下载脚本可以点此访问[度盘连接]）

> 推荐在`__bot__.py`中设置`RES_PROTOCOL`为`file`(方便发送gif类型图片)

-------------




## 友情链接

**干炸里脊资源站**: https://redive.estertion.win/

**公主连结Re: Dive Fan Club - 硬核的竞技场数据分析站**: https://pcrdfans.com/

**yobot**: https://yobot.win/

