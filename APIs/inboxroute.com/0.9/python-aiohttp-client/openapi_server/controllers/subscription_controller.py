from typing import List, Dict
from aiohttp import web

from openapi_server.models.contacts_get401_response_inner import ContactsGet401ResponseInner
from openapi_server.models.contacts_get404_response_inner import ContactsGet404ResponseInner
from openapi_server.models.contacts_get422_response_inner import ContactsGet422ResponseInner
from openapi_server.models.subscription_request import SubscriptionRequest
from openapi_server import util


async def subscription_listid_post(request: web.Request, listid, subscription) -> web.Response:
    """subscription_listid_post

    Subscribe an email address to a list. This api call has the same behavior as a regular subscribe form. However, single opt-in is allowed for system integration purposes.  - If email address does not exist, a new contact will be added to the list. - If email address exists custom fields will be updated and status will be put   to unconfirmed or active depending of singleoptin value. - If current status if Active, this operation will only update the custom fields. - If singleoptin is true, no email confirmation will be sent. In that case,   you must provide the subscribe&#39;s origin ip and confirmation date-time. 

    :param listid: Unique 16 characters ID of the contact list
    :type listid: str
    :param subscription: Subscription request
    :type subscription: dict | bytes

    """
    subscription = SubscriptionRequest.from_dict(subscription)
    return web.Response(status=200)
