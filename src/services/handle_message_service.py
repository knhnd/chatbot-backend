import json

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        json_file = open('/src/dict/mydict.json', 'r')
        mydict = json.load(json_file)
        print(mydict)
        return receivedMessage

