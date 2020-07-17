"""
PCR会战管理命令 v2

猴子也会用的会战管理

命令设计遵循以下原则：
- 中文：降低学习成本
- 唯一：There should be one-- and preferably only one --obvious way to do it.
- 耐草：参数不规范时尽量执行
"""

import json, requests
from typing import List
from matplotlib import pyplot as plt
from aiocqhttp.exceptions import ActionFailed
from nonebot import NoneBot
from nonebot import MessageSegment as ms
from nonebot.typing import Context_T
from hoshino import util, priv

from . import sv, cb_cmd
from .argparse import ArgParser, ArgHolder, ParseResult
from .argparse.argtype import *
from .battlemaster import BattleMaster
from .exception import *

plt.style.use('seaborn-pastel')
plt.rcParams['font.family'] = ['DejaVuSans', 'Microsoft YaHei', 'SimSun', ]



async def _do_show_rankn(bot:NoneBot, ctx:Context_T, args:ParseResult):
    url = 'https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/name/0'
    name = args.name
    data = json.dumps({'clanName': name})
    headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Connection": "keep-alive",
    "Content-Length": "39",
    "Origin": "https://kengxxiao.github.io",
    "Referer": "https://kengxxiao.github.io/Kyouka/",
    "Host": "service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com"
        }
    resp = requests.post(url, data=data, headers=headers)
    if resp.status_code == 200:
        resp_data = json.loads(resp.text)
        if not resp_data['data']:
            await bot.send(ctx, '未找到该行会', at_sender=True)
            return
        msg = ['\n']
        for data in resp_data['data']:
            msg.append(
                f'{data["clan_name"]} 共{data["member_num"]}人:\n会长：{data["leader_name"]} | 当前第{data["rank"]}名 | 合计分数：{data["damage"]}')
        await bot.send(ctx, '\n'.join(msg), at_sender=True)
    else:
        await bot.send(ctx, f'{resp.status_code}查询出错，请稍后重试或使用网页\nhttps://kengxxiao.github.io/Kyouka/', at_sender=True)

async def _do_show_rankl(bot:NoneBot, ctx:Context_T, args:ParseResult):
    url = 'https://service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com/leader/0'
    name = args.name
    data = json.dumps({'leaderName': name})
    headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Connection": "keep-alive",
    "Content-Length": "32",
    "Origin": "https://kengxxiao.github.io",
    "Referer": "https://kengxxiao.github.io/Kyouka/",
    "Host": "service-kjcbcnmw-1254119946.gz.apigw.tencentcs.com"
        }
    resp = requests.post(url, data=data, headers=headers)
    if resp.status_code == requests.codes.ok:
        resp_data = json.loads(resp.text)
        if not resp_data['data']:
            await bot.send(ctx, '未找到该行会', at_sender=True)
            return
        msg = ['\n']
        for data in resp_data['data']:
            msg.append(
                f'{data["clan_name"]} 共{data["member_num"]}人:\n会长：{data["leader_name"]} | 当前第{data["rank"]}名 | 合计分数：{data["damage"]}')
        await bot.send(ctx, '\n'.join(msg), at_sender=True)
    else:
        await bot.send(ctx, f'{resp.status_code}查询出错，请稍后重试或使用网页\nhttps://kengxxiao.github.io/Kyouka/', at_sender=True)

@cb_cmd(
    ('排名公会', '查询排名公会'),
    ArgParser(usage='!排名 <公会名>',
    arg_dict={'': ArgHolder(tip='公会名', type=str, default='自强不息')}))
async def list_remainn(bot:NoneBot, ctx:Context_T, args:ParseResult):
    data = ParseResult({'name': args.get('')})
    await _do_show_rankn(bot, ctx, data)

@cb_cmd(
    ('排名会长', '查询排名会长'),
    ArgParser(usage='!排名 <会长名>',
    arg_dict={'': ArgHolder(tip='公会会长名', type=str, default='墨染朱璃鶸')}))
async def list_remainl(bot:NoneBot, ctx:Context_T, args:ParseResult):
    data = ParseResult({'name': args.get('')})
    await _do_show_rankl(bot, ctx, data)