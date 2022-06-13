word = {
  "test": "正常に可動しています！",
  "sample": "ちゃんと受け取れています！",
  "hello": "Hello, World!",
  "morning": "おはようございます，よい朝ですね！",
  "afternoon": "こんにちは，ごきげんいかがですか？",
  "evening": "こんばんは，いい夜をお過ごしください！"
}


class handle_message_service : 
    def generate_reply_message(receivedMessage) :
        if (receivedMessage == 'こんにちは'):
            return word['afternoon']
        elif (receivedMessage == 'hello'):
            return word['hello']
        elif (receivedMessage == 'こんにちは') :
            return word['test']
        else:
            return '辞書にない単語です'

