from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call_user_defined_message import ApiV2010AccountCallUserDefinedMessage
from openapi_server import util


async def create_user_defined_message(request: web.Request, account_sid, call_sid, content, idempotency_key=None) -> web.Response:
    """create_user_defined_message

    Create a new User Defined Message for the given Call SID.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
    :type account_sid: str
    :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
    :type call_sid: str
    :param content: The User Defined Message in the form of URL-encoded JSON string.
    :type content: str
    :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
    :type idempotency_key: str

    """
    return web.Response(status=200)
