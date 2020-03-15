from flask import Flask,request,abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import(
    LineBotApi,WebhookHandler
)

from linebot.exceptions import(
    InvalidSignatureError,LineBotApiError
)

### Script start ###
from linebot.models import MessageEvent,TextMessage,TextSendMessage

app=Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('GiTfOtfEvvDvrVZypikWKfGaE8+TmokunZS1pkMlrn3ZSSrYUquK0Cx0w/qvPHHzNnWLMp1fAMEC16J/CcypzUzXMzOnob0u16UJo66HjdADfEi8PSipETK/KYrCHA8Us+j4BGqVFE4i5Jd5QKEEHwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5ee7810ceead2ff88247f1c1f2ff9d75')



# 監聽所有來自 / 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature=request.headers['X-Line-Signature']
    # get request body as text
    body=request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        print("Invalid signature, pls check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

import os
if __name__=="__main__":
    #port=int(os.environ.get('PORT',5000))
    #app.run(host='0.0.0.0',port=port)
    app.run()
