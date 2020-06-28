import os
import random
import re

from nonebot.exceptions import CQHttpError

from hoshino import R, Service, priv
from hoshino.util import FreqLimiter, DailyNumberLimiter

_max = 5
EXCEED_NOTICE = f'您今天已经冲过{_max}次了，请明早5点后再来！'
_nlmt = DailyNumberLimiter(_max)
_flmt = FreqLimiter(5)

sv = Service('setu', manage_priv=priv.SUPERUSER, enable_on_default=True, visible=False)
setu_folder = R.img('setu/PixivImage/').path
setu_folderT = R.img('setu/PixivImage/tong/').path


def setu_gener():
    while True:
        filelist = os.listdir(setu_folder)
        random.shuffle(filelist)
        for filename in filelist:
            if os.path.isfile(os.path.join(setu_folder, filename)):
                yield R.img('setu/PixivImage/', filename)

def setu_generT():
    while True:
        filelistT = os.listdir(setu_folderT)
        random.shuffle(filelistT)
        for filename in filelistT:
            if os.path.isfile(os.path.join(setu_folderT, filename)):
                yield R.img('setu/PixivImage/tong', filename)

setu_gener = setu_gener()
setu_generT = setu_generT()

def get_setu():
    return setu_gener.__next__()

def get_setuT():
    return setu_generT.__next__()



@sv.on_rex(r'^(?!.*铜).*(臭鼬|凯露|bot|キャル|猫猫).*(不够[涩瑟色sS]|[涩瑟色sS][图t]|来一?[点份张].*[涩瑟色sS]|再来[点份张]|看过了|kgl|gkd|GKD|有无[涩瑟色sS]图|有无setu|有无st)')
async def setu(bot, ev):
    """随机叫一份涩图，对每个用户有冷却时间"""
    uid = ev['user_id']
    if not _nlmt.check(uid):
        await bot.send(ev, EXCEED_NOTICE, at_sender=True)
        return
    if not _flmt.check(uid):
        await bot.send(ev, '宁冲得太快了，请先攒点再冲', at_sender=True)
        return
    _flmt.start_cd(uid)
    _nlmt.increase(uid)

    # conditions all ok, send a setu.
    pic = get_setu()

    try:
        await bot.send(ev, pic.cqcode)
    except CQHttpError:
        sv.logger.error(f"发送图片{pic.path}失败")
        try:
            await bot.send(ev, '涩图太涩，发不出去力...')
        except:
            pass


@sv.on_rex(r'(.*铜.*)(臭鼬|凯露|bot|キャル|猫猫)(.*)|(.*)(臭鼬|凯露|bot|キャル|猫猫)(.*铜.*)')
async def setu(bot, ev):
   """随机叫一份涩图，对每个用户有冷却时间"""
   uid = ev['user_id']    
   if not _nlmt.check(uid):
       await bot.send(ev, EXCEED_NOTICE, at_sender=True)
       return
   if not _flmt.check(uid):
       await bot.send(ev, '宁冲得太快了，请先攒点再冲', at_sender=True)
       return
   _flmt.start_cd(uid)
   _nlmt.increase(uid)

   picT = get_setuT()

   try:
       await bot.send(ev, picT.cqcode)
   except CQHttpError:
       sv.logger.error(f"发送图片{picT.path}失败")
       try:
           await bot.send(ev, '炼得太纯，进局子里力...')
       except:
           pass

setu_help = f'''
======================
   - setu命令帮助 -   
======================
【发送】
使用关键词“臭鼬|凯露|bot|キャル”+正常的gkd用语可以触发
当关键词包含“铜”时将发送对应类型
【注意事项】
同一QQ号存在5秒冷却间隔时间，一天内只会响应5次
'''.rstrip()

aliases = ('st帮助', 'setu帮助', '瑟图帮助', '涩图帮助', '色图帮助')
@sv.on_fullmatch(aliases, only_to_me=True)
async def st_help(bot, ev):
    await bot.send(ev, setu_help, at_sender=True)