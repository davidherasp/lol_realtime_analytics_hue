import requests, json
import websocket
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.lol_livestats
collection = db["H2KvsUOL_G2_11-06-17"]

def on_message(ws, message):
    if "send: " not in message:
        jmessage = json.loads(message)
        collection.insert_one(jmessage)
        print "response inserted"

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "open"
    
def get_collection_name():
    return "SPYvsMM"

if __name__ == "__main__":    
    r = requests.get("http://api.lolesports.com/api/issueToken")
    jr = json.loads(r.content)
    issue_token = jr["token"]
    ws_url = "ws://livestats.proxy.lolesports.com/stats?jwt=" + issue_token

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()