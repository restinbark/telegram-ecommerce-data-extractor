
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import pandas as pd

# Replace with your values
api_id = 21085447
api_hash = '49c3733a29561807853641ac3923e40a'
phone = '+25192299044'  # e.g. '+2519XXXXXXXX'

# Create the client and connect
client = TelegramClient('ethio_session', api_id, api_hash)

async def main():
    await client.start(phone)

    # Example channel username or invite link
    channel = await client.get_entity('@Leyueqa')  # change this to a real channel
    messages = []
    
    async for message in client.iter_messages(channel, limit=100):
        if message.message:  # only text messages
            messages.append({
                'date': message.date,
                'text': message.message,
                'views': message.views,
                'sender_id': message.sender_id
            })

    # Convert to DataFrame and save
    df = pd.DataFrame(messages)
    df.to_csv('liyueqa_telegram_messages.csv', index=False)
    print("Saved 100 messages to liyueqa_telegram_messages.csv")

with client:
    client.loop.run_until_complete(main())
