import pickle

class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        with open('mydict.pkl', mode='rb') as f:
            mydict = pickle.load(f)
        print(mydict)
        return receivedMessage

