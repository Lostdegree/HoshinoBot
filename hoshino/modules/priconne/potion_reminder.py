import pytz
from datetime import datetime
import random
import hoshino
from hoshino.service import Service
from hoshino import R

svpotion = Service('pcr-reminder-potion', enable_on_default=False, help_='商店买药提醒（台B）', bundle='pcr订阅')
tz = pytz.timezone('Asia/Shanghai')
list = [ 0, 6, 12, 18 ]

@svpotion.scheduled_job('cron', hour='*')
async def pcr_reminder_potion():
    now = datetime.now(tz)
    if ( now.hour not in list ):
        return  # 宵禁 免打扰
    pic = R.img(f"potion{random.randint(1, 4)}.jpg").cqcode
    msg = f'{pic}'
    await svpotion.broadcast(msg, 'pcr-reminder-potion', 0)