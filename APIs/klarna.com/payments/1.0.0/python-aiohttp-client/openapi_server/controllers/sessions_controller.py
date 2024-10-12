from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_session import MerchantSession
from openapi_server.models.session import Session
from openapi_server.models.session_create import SessionCreate
from openapi_server.models.session_read import SessionRead
from openapi_server import util


async def create_credit_session(request: web.Request, body) -> web.Response:
    """Create a new payment session

    Use this API call to create a Klarna Payments session.&lt;br/&gt;When a session is created you will receive the available &#x60;payment_method_categories&#x60; for the session, a &#x60;session_id&#x60; and a &#x60;client_token&#x60;. The &#x60;session_id&#x60; can be used to read or update the session using the REST API. The &#x60;client_token&#x60; should be passed to the browser. Read more on **[Create a new payment session](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/)**.

    :param body: session_request
    :type body: dict | bytes

    """
    body = SessionCreate.from_dict(body)
    return web.Response(status=200)


async def read_credit_session(request: web.Request, session_id) -> web.Response:
    """Read an existing payment session

    Use this API call to read a Klarna Payments session. You can read the Klarna Payments session at any time after it has been created, to get information about it. This will return all data that has been collected during the session. Read more on **[Read an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/check-the-details-of-a-payment-session/)**.

    :param session_id: session_id
    :type session_id: str

    """
    return web.Response(status=200)


async def update_credit_session(request: web.Request, session_id, body) -> web.Response:
    """Update an existing payment session

    Use this API call to update a Klarna Payments session with new details, in case something in the order has changed and the checkout has been reloaded. Including if the consumer adds a new item to the cart or if consumer details are updated. Read more on **[Update an existing payment session](https://docs.klarna.com/klarna-payments/other-actions/update-the-cart/)**.

    :param session_id: session_id
    :type session_id: str
    :param body: session_request
    :type body: dict | bytes

    """
    body = Session.from_dict(body)
    return web.Response(status=200)
