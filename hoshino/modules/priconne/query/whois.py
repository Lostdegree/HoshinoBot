from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter

from .. import chara
from . import sv
from hoshino import R
import os
from os import path

lmt = FreqLimiter(5)

@sv.on_suffix(('是谁', '是誰'))
@sv.on_prefix(('谁是', '誰是'))
async def whois(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.send(ev, f'兰德索尔花名册冷却中(剩余 {int(lmt.left_time(uid)) + 1}秒)', at_sender=True)
        return
    lmt.start_cd(uid)

    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"谁是"+别称，如"谁是霸瞳"')
        return
    id_ = chara.name2id(name)
    confi = 100
    guess = False
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(name)
        guess = True
    c = chara.fromid(id_)
    
    msg = ''
    if guess:
        lmt.start_cd(uid, 60)
        msg = f'兰德索尔似乎没有叫"{name}"的人...\n角色别称补全计划: github.com/Ice-Cirno/HoshinoBot/issues/5'
        await bot.send(ev, msg)
        msg = f'\n您有{confi}%的可能在找{guess_name} '

    if confi > 60:
        msg += f'{c.icon.cqcode} {c.name}'
        await bot.send(ev, msg, at_sender=True)



@sv.on_prefix(('.ub', '。ub'))
async def ubrec(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.send(ev, f'您〇太快了，请稍等一会儿(剩余 {int(lmt.left_time(uid)) + 1}秒)', at_sender=True)
        return
    lmt.start_cd(uid, 5)

    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"谁是"+别称，如"谁是霸瞳"')
        return
    id_ = chara.name2id(name)
    confi = 100
    guess = False
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(name)
        guess = True
    c = chara.fromid(id_)
    
    msg = ''
    if guess:
        lmt.start_cd(uid, 60)
        msg = f'兰德索尔似乎没有叫"{name}"的人...\n角色别称补全计划: github.com/Ice-Cirno/HoshinoBot/issues/5 \n您有{confi}%的可能在找{guess_name} '
        await bot.send(ev, msg)
        #msg = f'\n您有{confi}%的可能在找{guess_name} '

    if confi > 60 and os.path.isfile(f'E:/1data/1data/res/img/priconne/rec/rec_unit_{id_}_ub.mp3'):
        msg = R.rec(f'priconne/rec/rec_unit_{id_}_ub.mp3').cqcode        
        await bot.send(ev, msg, at_sender=False)

    else:
        await bot.send(ev, f'暂时未收录对应语音，该宁来表演了~', at_sender=True)
