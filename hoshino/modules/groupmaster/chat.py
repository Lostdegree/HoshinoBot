import re

import random

from nonebot import on_command, on_natural_language, NLPSession

from hoshino import R, Service, priv, util


# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')



# ============================================================== #
sv = Service('chat', visible=False)
# ============================================================== #

waifu_word = ('真 是 可 爱 呢', R.img(f'laopo1.jpg').cqcode, R.img(f'laopo2.jpg').cqcode, R.img(f'laopo3.jpg').cqcode)

laogong_word = ('你给我滚！', R.img(f'laogong.jpg').cqcode)

nmeme_word = ('么...么你个大头鬼啦！', '不许么么！', R.img(f'maomao.jpg').cqcode, R.img(f'laopo1.jpg').cqcode)

meme_word = ('么么~', R.img(f'chieri2.jpg').cqcode)

AI_WORD = (f'不要过来啊啊啊\n{R.img("ai1.jpg").cqcode}', 'キャル知道你是个好人，但是...', f'你正常点，我害怕\n{R.img("me.jpg").cqcode}')

# ============================================================== #



# ============================================================== #


@sv.on_fullmatch(('沙雕机器人', '沙雕機器人', '傻bot', '沙雕bot'))
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_natural_language(keywords={'老婆', 'waifu', 'laopo', '宝贝', '亲爱的'}, only_to_me=False)
async def chat_waifu(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        if not priv.check_priv(session.ctx, priv.SUPERUSER):
            await session.send(random.choice(waifu_word))
        else:
            await session.send('mua~')

@sv.on_natural_language(keywords={'么么哒', '么么'}, only_to_me=False)
async def chat_memeda(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        if not priv.check_priv(session.ctx, priv.ADMIN):
            await session.send(random.choice(nmeme_word))
        else:
            await session.send(random.choice(meme_word))

@sv.on_natural_language(keywords={'爱你', '爱你哟', '我爱你', '喜欢你'}, only_to_me=False)
async def aini(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send(random.choice(AI_WORD), at_sender=True)

@sv.on_natural_language(keywords={'老公'}, only_to_me=False)
async def chat_laogong(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send(random.choice(laogong_word), at_sender=True)

@sv.on_natural_language(keywords={'笨蛋'}, only_to_me=False)
async def chat_bendan(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send('emmm...キャル觉得你也是笨比', at_sender=True)

@sv.on_natural_language(keywords={'mua'}, only_to_me=False)
async def chat_mua(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send('笨蛋~', at_sender=True)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')
    #await util.silence(ev, 30)


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    if random.random() < 0.4:
        await bot.send(ev, '不许好，憋回去！')
    #await util.silence(ev, 30)

@sv.on_natural_language(keywords={'good night', 'Good night', '晚安', '安安'}, only_to_me=False)
async def gnight(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send('安安~キャル现在还要工作不能睡。。。\n为什么为什么为什么为什么为什么为什么为什么为什么为什么为什么不让我睡啊啊啊啊啊啊啊啊啊', at_sender=True)

# ==================================================== #

clanba_word = ('大佬都是堇业先锋，キャルi了i了', R.img(f'dao1.jpg').cqcode, R.img(f'dao2.jpg').cqcode, R.img(f'dao3.jpg').cqcode, R.img(f'dao4.jpg').cqcode)

queshi_word = (R.img(f'qs1.jpg').cqcode, R.img(f'qs2.jpg').cqcode, R.img(f'qs3.png').cqcode, '确实')

niu_word = ('やばいですね！', R.img(f'laji.jpg').cqcode)

neigui_word = ('内鬼不是キャル哦', R.img(f'neigui.png').cqcode)

nyb_player = f'''{R.img('nyb.gif').cqcode}
正在播放：New Year Burst
──●━━━━ 1:05/1:30
⇆ ㅤ◁ ㅤㅤ❚❚ ㅤㅤ▷ ㅤ↻
'''.strip()

# ==================================================== #

@sv.on_keyword(('来点'))
async def laidian(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, '？自己动')


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy', 'y1s1', 'qs'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, random.choice(queshi_word))


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, random.choice(clanba_word))


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, random.choice(neigui_word))


@sv.on_keyword(('春黑', '新黑', '唯一神'))
async def new_year_burst(bot, ev):
    if random.random() < 0.02:
        await bot.send(ev, nyb_player)


@sv.on_keyword(('nb', '牛逼', '牛B', 'yyds', '🐮🍺'))
async def chat_niu(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, random.choice(niu_word))


@sv.on_keyword(('good night', '晚安', '安安'))
async def chat_gnight(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, f'\n都要早点睡哦~\n{R.img("dao2.jpg").cqcode}')


@sv.on_keyword(('啊这'))
async def chat_az(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, f'{R.img("az.jpg").cqcode}')


# ================================================== #

shy_word = ('诶嘿嘿~', '多夸点多夸点~', 'みんな大好き！', 'wwww....ue对不起！', R.img(f'shy1.jpg').cqcode)

ue_word = ('那你水黑必井', '那你春黑必井', '你的下一句话是“我春黑水黑都可以井，但你今晚biss（”')

qq_word = ('先去说声ue对不起嗷', R.img(f'dx1.jpg').cqcode, R.img(f'dbq.jpg').cqcode)

cy_word = ('不是臭鼬，是猫猫！', f'都说了是猫猫。。。\n{R.img("me1.jpg").cqcode}')

mt_word = ('别摸了别摸了再摸头要秃了!!!∑(ﾟДﾟノ)ノ', 'zzz...啊，差点就睡着了。。。', '怎么这么二刺猿害搁着天天摸头呢')

mw_word = ('尾、尾巴那里。。。不行', R.img(f'mw1.jpg').cqcode)

me_word = (f'宁真是老hentai了啊\n{R.img("me.jpg").cqcode}', R.img(f'maomao.jpg').cqcode)

# ================================================== #

@sv.on_natural_language(keywords={'zai', '在', 'z'}, only_to_me=False)
async def n_zai(session:NLPSession):
    arg = session.msg_text.strip()
    rex = re.compile(r'(.*)kkp(.*)')
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    m = rex.search(arg)
    ms = rexs.search(arg)
    if m and ms:
        await session.send('再嘴臭キャル请你吃套餐嗷', at_sender=True)
    elif not m and ms:
        await session.send('在在在，キャル很忙的嗷', at_sender=True)
	
@sv.on_natural_language(keywords={'嗦'}, only_to_me=True)
async def n_suo(session:NLPSession):
    arg = session.msg_text.strip()
    rex = re.compile(r'(.*)(牛|🐮)(.*)')
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    m = rex.search(arg)
    ms = rexs.search(arg)
    if m and ms:
        await session.send('不嗦，好臭好噁！', at_sender=True)
	
@sv.on_natural_language(keywords={'爸'}, only_to_me=False)
async def n_ba(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    ms = rexs.search(arg)
    if ms:
        await session.send('连爸都叫，这是我没想到的', at_sender=True)
	
@sv.on_natural_language(keywords={'不'}, only_to_me=False)
async def n_bu(session:NLPSession):
    arg = session.msg_text.strip()
    rex = re.compile(r'(.*)我(.*)')
    rexs = re.compile(r'臭鼬|凯露|猫猫')
    m = rex.search(arg)
    ms = rexs.search(arg)
    if ms:
        if m and random.random() < 0.2:
            await session.send('不准不！', at_sender=True)
        elif not m and random.random() < 0.1:
            await session.send('天天不不不，让你去真不王国好了（', at_sender=True)
	
@sv.on_natural_language(keywords={'催刀'}, only_to_me=False)
async def n_suo(session:NLPSession):
    arg = session.msg_text.strip()
    rex = re.compile(r'(.*)(无效|不许|不准)(.*)')
    m = rex.search(arg)
    if m:
        await session.send('会长，这人看来想要套餐了~', at_sender=False)
    elif not m and random.random() < 0.2:
        await session.send('多催催，多打打，会长也能早放假', at_sender=False)
	
@sv.on_natural_language(keywords={'工具人'}, only_to_me=False)
async def n_gjr(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'.*(臭鼬|凯露|猫猫).*')
    ms = rexs.search(arg)
    if ms:
        await session.send('那。。。宁来统计出刀怎么样？', at_sender=True)
	
@sv.on_natural_language(keywords={'臭鼬'}, only_to_me=False)
async def n_cy(session:NLPSession):
    if random.random() < 0.1:
        await session.send(random.choice(cy_word), at_sender=True)
	
@sv.on_natural_language(keywords={'亲亲', '啾啾', '对不起'}, only_to_me=False)
async def n_qq(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'.*(臭鼬|凯露|猫猫).*')
    ms = rexs.search(arg)
    if ms:
        await session.send(random.choice(qq_word), at_sender=True)
	
@sv.on_natural_language(keywords={'nb', '牛逼', '牛B', '牛b', 'tql', 'wsl', 'awsl', 'yyds', '永远滴神','可爱', '🐮🍺'}, only_to_me=False)
async def n_praise(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'.*(臭鼬|凯露|猫猫).*')
    rex = re.compile(r'^(?!.*不).*')
    ms = rexs.search(arg)
    m = rex.search(arg)
    if ms and m:
        if random.random() < 0.95:
            await session.send(random.choice(shy_word), at_sender=True)
	
@sv.on_natural_language(keywords={'春田'}, only_to_me=True)
async def chat_ue(session):
    arg = session.msg_text.strip()
    rex = re.compile(r'.*井.*')
    m = rex.search(arg)
    if m:
        await session.send(random.choice(ue_word), at_sender=True)
	
@sv.on_natural_language(keywords={'摸'}, only_to_me=False)
async def n_mt(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'.*(臭鼬|凯露|猫猫).*')
    rexa = re.compile(r'.*头.*')
    rexb = re.compile(r'.*尾.*')
    rexc = re.compile(r'.*耳.*')
    ms = rexs.search(arg)
    ma = rexa.search(arg)
    mb = rexb.search(arg)
    mc = rexc.search(arg)
    if ms:
        if ma:
            await session.send(random.choice(mt_word), at_sender=True)
        elif mb:
            await session.send(random.choice(mw_word), at_sender=True)
        elif mc:
            await session.send(random.choice(me_word), at_sender=True)
        else:
            return


