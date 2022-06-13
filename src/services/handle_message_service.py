import json

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        json_file = open("../dict/dict.json", "r")
        print(json_file)
        return receivedMessage + "OK"
