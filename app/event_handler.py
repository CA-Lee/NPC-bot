from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent
from linebot.models.messages import TextMessage
from linebot.models.send_messages import TextSendMessage

from app.config import LINE_CHANNEL_SECRET, LINE_CHANNEL_TOKEN

handler = WebhookHandler(LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, TextMessage)
def handle_text_message(event: MessageEvent):
    """
    Echo the same message
    """

    actual_answer = "(正解)"
    reply_message = """夢想，可以天花亂墜。
理想，是我們一步一腳印，
踩出來的坎坷道路。"""
    if "思考" in event.message.text:
        reply_message = actual_answer
    if "行動" in event.message.text:
        reply_message = actual_answer
    if "突破" in event.message.text:
        reply_message = actual_answer

    line_bot_api = LineBotApi(LINE_CHANNEL_TOKEN)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(reply_message)
    )
