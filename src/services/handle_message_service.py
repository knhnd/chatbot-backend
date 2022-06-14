import json

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        json_file = open('/app/src/dict/mydict.json', 'r')
        mydict = json.load(json_file)

        for key in mydict :
            if (receivedMessage == key) :
                return mydict[key]
            else :
                return mydict['except']