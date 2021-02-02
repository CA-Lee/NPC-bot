from linebot import WebhookHandler, LineBotApi
from linebot.models import MessageEvent
from linebot.models.messages import TextMessage
from linebot.models.responses import Profile
from linebot.models.send_messages import TextSendMessage

from app.config import LINE_CHANNEL_SECRET, LINE_CHANNEL_TOKEN

handler = WebhookHandler(LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, TextMessage)
def handle_text_message(event: MessageEvent):
    """
    Echo the same message
    """

    member_list = []

    line_bot_api = LineBotApi(LINE_CHANNEL_TOKEN)
    for mentionee in event.message.mention.mentionees:
        profile: Profile = line_bot_api.get_group_member_profile(
            event.source.group_id, mentionee.user_id
        )
        member_list.append({profile.user_id: profile.display_name})

    line_bot_api.push_message(
        "Ue70ae03be881e06fcb8c4b6bfbd074ca",
        TextSendMessage(event.message.text + "\n\n" + str(member_list)),
    )

    #     actual_answer = "(正解)"
    #     reply_message = """夢想，可以天花亂墜。
    # 理想，是我們一步一腳印，
    # 踩出來的坎坷道路。"""
    #     if "思考" in event.message.text:
    #         reply_message = actual_answer
    #     if "行動" in event.message.text:
    #         reply_message = actual_answer
    #     if "突破" in event.message.text:
    #         reply_message = actual_answer

    # line_bot_api.reply_message(
    #     event.reply_token, TextSendMessage(reply_message)
    # )
