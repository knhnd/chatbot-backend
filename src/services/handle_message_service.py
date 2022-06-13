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
        return word.hello
