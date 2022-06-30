import json

class HandleMessage : 
    def generate_reply_message(receivedMessage) :
        json_file = open('/app/libs/mydict.json', 'r')
        mydict = json.load(json_file)

        for key in mydict :
            if (receivedMessage == key) :
                return mydict[key]
        return mydict['except']