import os
from flask import Flask
from flask import request
# import json
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
from libs.handle_message import * 

# generate instance
app = Flask(__name__)

# ローカルサーバで動作確認する場合には LINE の Access Token と Channel Secret は config.json に詰めて読み込む
# json_file = open('./config.json', 'r')
# json_data = json.load(json_file)
# ACCESS_TOKEN = json_data["access_token"]
# CHANNEL_SECRET = json_data["channel_secret"]

# サーバの環境変数
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]

# アクセストークンの取得
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# endpoint
@app.route("/")
def test():
        return "<h1>Success, It Works!</h1>"

# # endpoint from linebot
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# # handle message from LINE
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = HandleMessage_service.generate_reply_message(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))