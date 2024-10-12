from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_message_message_feedback import ApiV2010AccountMessageMessageFeedback
from openapi_server.models.message_feedback_enum_outcome import MessageFeedbackEnumOutcome
from openapi_server import util


async def create_message_feedback(request: web.Request, account_sid, message_sid, outcome=None) -> web.Response:
    """create_message_feedback

    Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated Message

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback.
    :type account_sid: str
    :param message_sid: The SID of the Message resource for which to create MessageFeedback.
    :type message_sid: str
    :param outcome: 
    :type outcome: str

    """
    return web.Response(status=200)
