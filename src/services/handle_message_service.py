import pickle

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        with open('./../dict/mydict.pkl', mode='rb') as f:
            mydict = pickle.load(f)
        print(mydict)
        if (receivedMessage == 'こんにちは'):
            return word['afternoon']
        elif (receivedMessage == 'hello'):
            return word['hello']
        elif (receivedMessage == 'こんにちは') :
            return word['test']
        else:
            return '辞書にない単語です'

