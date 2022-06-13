import json

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        json_file = open("./../dict/dict.json", "r")
        json_data = json.load(json_file)
        return json_data
