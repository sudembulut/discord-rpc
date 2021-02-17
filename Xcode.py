import rpc
import time
from time import mktime

print("Demo for python-discord-rpc Xcode")
client_id = '811556256384548864'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "i really need some semicolon",  # anything you like
            "details": "Editing a Swift Project",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Swift 5",  # anything you like
                "small_image": "swift",  # must match the image key
                "large_text": "Xcode",  # anything you like
                "large_image": "xcode"  # must match the image key
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(900)
