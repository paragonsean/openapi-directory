from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_call_user_defined_message_subscription import ApiV2010AccountCallUserDefinedMessageSubscription
from openapi_server import util


async def create_user_defined_message_subscription(request: web.Request, account_sid, call_sid, callback, idempotency_key=None, method=None) -> web.Response:
    """create_user_defined_message_subscription

    Subscribe to User Defined Messages for a given Call SID.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
    :type account_sid: str
    :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.
    :type call_sid: str
    :param callback: The URL we should call using the &#x60;method&#x60; to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
    :type callback: str
    :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
    :type idempotency_key: str
    :param method: The HTTP method Twilio will use when requesting the above &#x60;Url&#x60;. Either &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;.
    :type method: str

    """
    return web.Response(status=200)


async def delete_user_defined_message_subscription(request: web.Request, account_sid, call_sid, sid) -> web.Response:
    """delete_user_defined_message_subscription

    Delete a specific User Defined Message Subscription.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
    :type account_sid: str
    :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
    :type call_sid: str
    :param sid: The SID that uniquely identifies this User Defined Message Subscription.
    :type sid: str

    """
    return web.Response(status=200)
