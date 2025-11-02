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

# HERE WE ARE RECIEVING THE MESSAGE FROM THE FRONTEND
    async def recieve(self, message_data):
        # LOAD THE MESSAGE DATA, IN ORDER TO DECODE IT
        data = json.loads(message_data) 
        # EXTRAACT DATA FROM MESSAGE/
        message = data['message']
        username = data['username']
        room = data['room']

        # NOW,WE SEND THIS DATA TO THE CHANNEL LAYER.
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room,
            }
        )

# HERE WE ARE SENDING THE MESSAGE AGAIN TO THE CLIENT. BECAUSE WE HAVE MULTIPLE CLIENTS.
#   
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dump({
            'message':message,
            'username':username,
            'room':room,
        }))
