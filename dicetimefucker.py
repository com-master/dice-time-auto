from pyrogram import Client
import config
import time
api_id = config.api_id
api_hash = config.api_hash

count_accounts = int(input("Input Counts Accounts: "))


for i in range(count_accounts):
    with Client("my_account" + str(i), api_id, api_hash) as app:
        for i in config.chats:
            try:
                try:
                    app.join_chat(i)
                except:
                    pass
                time.sleep(3)
                app.send_message(i, "dice time")
                time.sleep(3)
            except:
                pass
