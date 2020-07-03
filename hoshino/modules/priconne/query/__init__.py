from hoshino import Service

sv_help = '''
[pcr速查] 常用网址/图书馆
[bcr速查] B服萌新攻略
[日rank] rank推荐表
[台rank] rank推荐表
[陆rank] rank推荐表
[挖矿15001] 矿场余钻
[黄骑充电表] 黄骑1动规律
[角色站位图] 查询角色站位
[一个顶俩] 台服接龙小游戏
[谁是霸瞳] 角色别称查询
[.(或。)ub角色名称]角色ub语音
'''.strip()

sv = Service('pcr-query', help_=sv_help, bundle='pcr查询')

from .query import *
from .whois import *
from .miner import *
