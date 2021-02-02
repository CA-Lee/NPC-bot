from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent
from linebot.models.messages import TextMessage
from linebot.models.send_messages import TextSendMessage
import httpx

from app.config import (
    LINE_CHANNEL_SECRET,
    LINE_CHANNEL_TOKEN,
    group,
    lows,
    mids,
    highs,
)

handler = WebhookHandler(LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, TextMessage)
def handle_text_message(event: MessageEvent):
    """
    Echo the same message
    """

    actual_answer = "遠在天邊，近在眼前。"
    reply_message = """夢想，可以天花亂墜。
理想，是我們一步一腳印，
踩出來的坎坷道路。"""
    if (
        (("思考" in event.message.text) and (event.source.user_id in lows))
        or (("行動" in event.message.text) and (event.source.user_id in mids))
        or (("突破" in event.message.text) and (event.source.user_id in highs))
    ):
        reply_message = actual_answer
        httpx.post(
            "https://script.google.com/macros/s/AKfycbxnHqeOUccfYFuivVYFbU4XaCAaXl3v9mylkCJV5s6qXreyDnPqSKpdNQ/exec",
            json={"group": group[event.source.user_id]},
        )

    line_bot_api = LineBotApi(LINE_CHANNEL_TOKEN)
    if event.source.type == "user" or reply_message == actual_answer:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(reply_message)
        )
