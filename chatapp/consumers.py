from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

#CONSUMER ALLOWS US TO CREATE FUNCTIONS TO HANDLE EACH & EVERY EVENT. 
class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #CONNECTING TO A PARTICULAR ROOM
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept() #ACCEPTS THE INCOMING CONNECTION.

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.channel_layer,
            self.room_group_name
        )
