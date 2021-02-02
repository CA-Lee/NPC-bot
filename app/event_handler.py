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
    lows = [
        "Ub9a35d8d104346abe6d7d88b8d0e587b",
        "Ua6f729e7b736ff096f385e5441091257",
        "Ufbe7ffaa45015be8dff0c6be67438fe8",
        "Ubd42741617886b9beb0a0c5f6f258e0b",
        "U530fe5cda1022b06c1119a3535ad4c3c",
        "U42116a1849870dfe5bcef92d1ced04f7",
        "U65ab393ef9f0c30c90fcc583c67cad4d",
    ]
    mids = [
        "U45623de858046146f67d95e30d0c19d7",
        "Uf3b65fbf5e2b786f7c44149a23a38241",
        "Uf059925dbe8701ef27ef4c7828b9565e",
        "U7c69934c8edddff0b4ef039c85965e1c",
        "U1ff04ba052272478110d45572a9f44c4",
        "Uaf7e5953d20f3452bfa674b65d1ac18b",
        "Uf1921c3d8ba480cd61af06c7b12660c9",
    ]
    highs = [
        "U25c5e7b6ccb183b6e8e69d763b021c6d",
        "Uffd172c984d01beae3555ec6cd951f5e",
        "U99af3297894284c14a22f38af5ab4402",
        "Ue70ae03be881e06fcb8c4b6bfbd074ca",
    ]
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
