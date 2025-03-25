from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random
from .back import time_long, volume

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    
    @filter.command("打打我的")
    async def dajiao(self, event: AstrMessageEvent):
        
        time = round(random.uniform(1, 600), 2)
        V = round(random.uniform(0.01,100), 2)
        a = time_long(time)
        b = volume(V)
        user_name = event.get_sender_name()
        yield event.plain_result(f"Hello, {user_name}, 你坚持了{time}s哦，{a}.射出{V}ml,{b}!") 