# pip install pubnub


from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import os
from pathlib import Path 
import json 

os.chdir(Path(__file__).parent)



# Read Config
with open("./pubnub.json", mode= "r") as file:
    content = file.read()
    json_dict = json.loads(content)



pnconfig = PNConfiguration()

pnconfig.publish_key = json_dict["publish_key"]
pnconfig.subscribe_key = json_dict["subscribe_key"]
pnconfig.uuid = json_dict["app_uuid"]

pnconfig.ssl = True
pubnub = PubNub(pnconfig)



class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        print("from device 1: " + message.message)


def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass
    

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()


## publish a message
while True:
    msg = input("Input a message to publish: ")
    if msg == 'exit': 
        os._exit(1)
    pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)