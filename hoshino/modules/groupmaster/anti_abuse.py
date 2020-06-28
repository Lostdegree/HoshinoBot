# TODO: REBEAT_WORD 在json调用

import re
import random
from datetime import timedelta

import nonebot
from nonebot import on_natural_language, NLPSession
from nonebot import Message, MessageSegment, message_preprocessor, on_command
from nonebot.message import _check_calling_me_nickname

import hoshino
from hoshino import R, Service, util, priv

'''
from nonebot.command import CommandManager
def parse_command(bot, cmd_str):
    parse_command = CommandManager().parse_command(bot, cmd_str)


bot = nonebot.get_bot()
BLANK_MESSAGE = Message(MessageSegment.text(''))

@message_preprocessor
async def black_filter(bot, ctx, plugin_manager=None):  # plugin_manager is new feature of nonebot v1.6
    first_msg_seg = ctx['message'][0]
    if first_msg_seg.type == 'hb':
        return  # pass normal Luck Money Pack to avoid abuse
    if ctx['message_type'] == 'group' and hoshino.priv.check_block_group(ctx['group_id']) \
       or hoshino.priv.check_block_user(ctx['user_id']):
        ctx['message'] = BLANK_MESSAGE


def _check_hbtitle_is_cmd(ctx, title):
    ctx = ctx.copy()    # 复制一份，避免影响原有的ctx
    ctx['message'] = Message(title)
    _check_calling_me_nickname(bot, ctx)
    cmd, _ = parse_command(bot, str(ctx['message']).lstrip())
    return bool(cmd)


@bot.on_message('group')
async def hb_handler(ctx):
    self_id = ctx['self_id']
    user_id = ctx['user_id']
    group_id = ctx['group_id']
    first_msg_seg = ctx['message'][0]
    if first_msg_seg.type == 'hb':
        title = first_msg_seg['data']['title']
        if _check_hbtitle_is_cmd(ctx, title):
            hoshino.priv.set_block_group(group_id, timedelta(hours=1))
            hoshino.priv.set_block_user(user_id, timedelta(days=30))
            await util.silence(ctx, 7 * 24 * 60 * 60)
            msg_from = f"{ctx['user_id']}@[群:{ctx['group_id']}]"
            hoshino.logger.critical(f'Self: {ctx["self_id"]}, Message {ctx["message_id"]} from {msg_from} detected as abuse: {ctx["message"]}')
            await bot.send(ctx, "检测到滥用行为，您的操作已被记录并加入黑名单。\nbot拒绝响应本群消息1小时", at_sender=True)
            try:
                await bot.set_group_kick(self_id=self_id, group_id=group_id, user_id=user_id, reject_add_request=True)
                hoshino.logger.critical(f"已将{user_id}移出群{group_id}")
            except:
                pass

'''
# ============================================ #


REBEAT_WORD = (
    'rbq', 'RBQ', '憨批', '废物', '死妈', '崽种', '傻逼', '傻逼玩意', 
    '没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', 'cnm', '爬', 'kkp', 
    'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬', 
    'fnmdp', '哦，那真的牛批', '我不想和狗吵架。', '请你不要用你的排泄器官对我说话，这是很不礼貌的，谢谢！', 
    '你出生的时候是不是被扔起来三次，被接住了两次？', '你应该很喜欢健身吧，看你挺会抬杠的。', 
    '你嘴在化粪池都泡开花了', '你和你妈打电话一定要你先挂电话，不然你妈就会挂掉', '长城要是用你脸皮做的 孟姜女能哭倒才怪', 
    '天冷了，记得给你棺材加床被子别冻着', '你是不是掉过粪坑里，脖子以上全截肢了？', 
    '妈妈告诉我不能骂人，可不是每个人都有妈妈', '脑子转不过弯可以，但别进水', '你在数字界和字母界排行第二', 
    '有没有人说过你美的像个充气娃娃？', '我今天想骂人 所以不骂你', '请问芋泥玛奇朵还要加热吗？因为泥玛凉了', 
    '你是老子见过最他妈大的铅笔盒，装这么多逼不累吗？', '咋滴你管那么多呢？收粪车从你家门前路过你都要拿勺子尝尝咸淡？', 
    '你的嘴简直能给农田施肥', '垃圾都有家，你却没有。', '你的户口本就是一动物百科', '我尊重的是人 不是狗', 
    '尘归尘，土归土，把你骨灰扬了都不配做PM2.5', '你🐎没了嗷', ' 我留你狗命是因为我想保护动物毕竟你做只狗不容易', 
    '做了人类想成仙，生在地上要上天。', ' 你干嘛用屁股挡住脸啊！', '每个人都有妈妈，而你就不一样了，你不是人', 
    '你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了你急了', 
    '你妈跟我分手了，哈哈，骗你的！愚人节快乐！你哪来的妈', '我很讨厌你 就像邻居吃了花椒，麻了隔壁', 
    '老子顶你个肺，塞你个胃，顶到你花开又富贵。', ' 人不犯我我不犯人 人若犯我 我挖你祖坟', 
    '如果长的丑也算残疾的话，那你就不用工作了。'
)

JIAN_WORD = ('宁有剑吗？', f'哦，那💉💧🐮🍺\n{R.img("jian.jpg").cqcode}')

@on_natural_language(keywords={'臭鼬', '凯露', '猫猫'}, only_to_me=False)
async def ban_word(session:NLPSession):
    arg = session.msg_text.strip()
    rex = re.compile(r'.*rbq|RBQ|憨批|废物|死妈|崽种|傻逼|没用东西|傻B|傻b|SB|sb|煞笔|nm|爬|爪巴|kkp|dm|D区|口区|你爹|弱智|NM|你妈|清明|🐎|🐴|傻子|奥利给|奥力给|💩|nt|NT.*')
    m = rex.search(arg)
    if m:
        ctx = session.ctx
        user_id = ctx['user_id']
        msg_from = str(user_id)
        if ctx['message_type'] == 'group':
            msg_from += f'@[群:{ctx["group_id"]}]'
        elif ctx['message_type'] == 'discuss':
            msg_from += f'@[讨论组:{ctx["discuss_id"]}]'
        hoshino.logger.critical(f'Self: {ctx["self_id"]}, Message {ctx["message_id"]} from {msg_from}: {ctx["message"]}')
        await session.send(random.choice(REBEAT_WORD))
        priv.set_block_user(user_id, timedelta(hours=0.01))
    # pic = R.img(f"chieri{random.randint(1, 4)}.jpg").cqcode
    # await session.send(f"不理你啦！バーカー\n{pic}", at_sender=True)
        await util.silence(session.ctx, 60)
	
@on_natural_language(keywords={'剑', '🤺'}, only_to_me=False)
async def ban_jian(session:NLPSession):
    arg = session.msg_text.strip()
    rexs = re.compile(r'.*(臭鼬|凯露|猫猫).*')
    ms = rexs.search(arg)
    if ms:
        ctx = session.ctx
        user_id = ctx['user_id']
        msg_from = str(user_id)
        if ctx['message_type'] == 'group':
            msg_from += f'@[群:{ctx["group_id"]}]'
        elif ctx['message_type'] == 'discuss':
            msg_from += f'@[讨论组:{ctx["discuss_id"]}]'
        hoshino.logger.critical(f'Self: {ctx["self_id"]}, Message {ctx["message_id"]} from {msg_from}: {ctx["message"]}')
        await session.send(random.choice(JIAN_WORD))
        priv.set_block_user(user_id, timedelta(hours=0.01))
    # pic = R.img(f"chieri{random.randint(1, 4)}.jpg").cqcode
    # await session.send(f"不理你啦！バーカー\n{pic}", at_sender=True)
        await util.silence(session.ctx, 60)
