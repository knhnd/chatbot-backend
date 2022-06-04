from flask import Flask
import json
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

# generate instance
app = Flask(__name__)

# ローカルサーバを起動する場合は LINE Bot の Access Token と Secret は config.json に詰める
# json_file = open('../config.json', 'r')
# json_data = json.load(json_file)
# access_token = json_data["access_token"]
# channel_secret = json_data["channel_secret"]

# linebot token
# line_bot_api = LineBotApi(access_token)
# handler = WebhookHandler(channel_secret)

# endpoint
@app.route("/")
def test():
        return "<p>It Works!</p>"

# endpoint from linebot
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)
#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))
